from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message":"Hello world"}

@app.get("/items/")
def read_items():
    return{
            "items": ["item1", "item2", "item3"]
        }




