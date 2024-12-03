from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# get all todos

# get single todo

# create a todo

# update a todo

# delete a todo