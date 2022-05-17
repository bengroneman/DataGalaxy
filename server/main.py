from fastapi import FastAPI, File, Form, UploadFile


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("api/images/add")
async def add_image(file: bytes = File(), fileb: UploadFile = File()):
    return {"message": "add image"}
