from typing import List, Optional

import databases, aiofiles, sqlalchemy, os

from pydantic import BaseModel
from fastapi import FastAPI, File, Form, UploadFile, responses
from fastapi.middleware.cors import CORSMiddleware

DATABASE_URL = "sqlite:///./core.db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

images = sqlalchemy.Table(
    "images",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("mimetype", sqlalchemy.String),
)


engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)


class Image(BaseModel):
    id: int
    name: Optional[str] = None
    mimetype: Optional[str] = None


app = FastAPI()

origins = [
    'http://localhost:8000',
    'http://localhost:3000',
    'http://localhost',
    'https://elaborate-pastelito-70d2ac.netlify.app',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/api/images/", response_model=List[Image])
async def read_images():
    query = images.select()
    return await database.fetch_all(query)


@app.get("/api/images/{id}")
async def read_images(id: int):
    query = images.select().where(images.c.id == id)
    image = await database.fetch_one(query)
    abs_fn = os.path.join("./assets", image.name)
    if image.name.lower().endswith((".jpg", ".png", ".gif")) and os.path.isfile(abs_fn):
        return responses.StreamingResponse(open(abs_fn, "rb"), media_type=image.mimetype)
    else:
        return {"error": "File not found", "status": 404}


@app.post("/api/images/")
async def create_image(image: UploadFile = File(...)):
    if image is None:
        return { "error": "No file uploaded" }

    if not image.filename.lower().endswith((".jpg", ".png", ".gif")):
        return {"error": "Only JPG, PNG and GIF files are allowed", "status": 400}

    async with aiofiles.open(f"./assets/{image.filename}", "wb") as out_image:
        try:
            filesize = await os.path.getsize(f"./assets/{image.filename}")
            if filesize > 1024 * 1024 * 10:
                return {"error": "File size too large", "status": 400}
        except OSError:
            return {"error": "File not found", "status": 404}
        while content := await image.read(1024):
            await out_image.write(content)

    query = images.insert().values(name=image.filename, mimetype=image.content_type)
    last_record_id = await database.execute(query)
    if last_record_id is None:
        return {"error": "Failed to upload file", "status": 404}

    return {"id": last_record_id, "name": image.filename, "mimetype": image.content_type, "status": 200}
