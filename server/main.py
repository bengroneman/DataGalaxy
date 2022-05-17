from typing import List, Optional

from fastapi import FastAPI, File, Form, UploadFile

import databases, aiofiles, sqlalchemy

from pydantic import BaseModel

# SQLAlchemy specific code, as with any other app
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


@app.post("/api/images/", response_model=Image)
async def create_image(image: UploadFile = File(...)):
    async with aiofiles.open(f"./assets/{image.filename}", "wb") as out_image:
        while content := await image.read(1024):
            await out_image.write(content)

    query = images.insert().values(name=image.filename, mimetype=image.content_type)
    print(query)
    last_record_id = await database.execute(query)
    return {"id": last_record_id, "name": image.filename, "mimetype": image.content_type}
