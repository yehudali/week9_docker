from typing import Dict, Optional
from fastapi import FastAPI
from pathlib import Path
from pydantic import BaseModel
import uvicorn
import json
import os 
from contextlib import asynccontextmanager

from fastapi import FastAPI

    
BASE_DIR = Path(__file__).resolve().parent            # .../server2
DB_PATH = BASE_DIR / "db" / "shopping_list.json"      # .../server2/db/shopping_list.json


app = FastAPI()   #lifespan=startup_event

class Item(BaseModel):
    id : Optional[int]
    name : str
    quantity : int

def load_database():
    try:
        with open(DB_PATH , 'r') as f:
            dict_data_base = json.load(f)
            return dict_data_base
    except Exception:
        raise ValueError(f"i cnat be open and endcoding dhe DB_PATH{DB_PATH}")
    

def save_data(data):
    with open(DB_PATH, "w") as f:
        json.dump(data, f)




@app.get("/")
def root():
    return {"message": "Welcome to the Items API!", "database": str(DB_PATH)}

@app.get("/items")
def return_all_items():
    deta = load_database()
    return  deta

# @app.post("/items")
# def add_new_item(parm_item: Item):
#     data = load_database()
#     items = data


#     id = str(len(data) + 1)
#     items[id] = dict(parm_item)
    
    
#     data = items
#     save_data(data)
#     return {
#         "message": "Item created successfully",
#         "item_id": id,
#         "item": items[id],
#     }



# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="localhost", port=8001)