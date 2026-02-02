# Fast-API-MongoDB-CRUD
A clean, production‑style FastAPI + MongoDB CRUD project, structured


## 📁 Project Structure

```text
fastapi-mongo-crud/
│
├── app/
│   ├── main.py
│   │
│   ├── core/
│   │   └── config.py
│   │
│   ├── database/
│   │   └── mongo.py
│   │
│   ├── models/
│   │   └── user_model.py
│   │
│   ├── services/
│   │   └── user_service.py
│   │
│   ├── controllers/
│   │   └── user_controller.py
│   │
│   └── routers/
│       └── user_router.py
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## 🚀 main.py (Application Entry Point)

```python
from fastapi import FastAPI
from app.routers.user_router import user_router

app = FastAPI(title="User CRUD API")

app.include_router(user_router)
```

---

## ⚙️ config.py

```python
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
DB_NAME = os.getenv("DB_NAME")
```

---

## 🗄️ MongoDB Connection (database/mongo.py)

```python
from pymongo import MongoClient
from app.core.config import MONGO_URL, DB_NAME

client = MongoClient(MONGO_URL)
database = client[DB_NAME]

user_collection = database.get_collection("users")
```

---

## 🧩 Entity / Model (models/user_model.py)

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str
```

(Think of this as **Entity class** like Spring Boot)

---

## 🧠 Service Layer (services/user_service.py)

```python
from bson import ObjectId
from app.database.mongo import user_collection

def create_user(user: dict):
    user_collection.insert_one(user)
    return user


def get_all_users():
    users = []
    for user in user_collection.find():
        user["id"] = str(user["_id"])
        del user["_id"]
        users.append(user)
    return users


def update_user(user_id: str, data: dict):
    user_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": data}
    )


def delete_user(user_id: str):
    user_collection.delete_one({"_id": ObjectId(user_id)})
```

(Exactly like **Service class in Spring Boot**)

---

## 🎯 Controller / Router (routers/user_router.py)

```python
from fastapi import APIRouter
from app.models.user_model import User
from app.services.user_service import (
    create_user,
    get_all_users,
    update_user,
    delete_user
)

user_router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
def create(user: User):
    create_user(user.dict())
    return {"message": "User created"}


@router.get("/")
def get_all():
    return get_all_users()


@router.put("/{id}")
def update(id: str, user: User):
    update_user(id, user.dict())
    return {"message": "User updated"}


@router.delete("/{id}")
def delete(id: str):
    delete_user(id)
    return {"message": "User deleted"}
```

---

## 📦 requirements.txt

```text
fastapi
uvicorn
pymongo
python-dotenv
```

---

## 🔐 .env

```env
MONGO_URL=mongodb://localhost:27017
DB_NAME=fastapi_crud
```

---

## 🧪 Run the App

```bash
uvicorn app.main:app --reload
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

