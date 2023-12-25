from fastapi import APIRouter
from config.db import conn
from models.index import users

user = APIRouter

@user.get("/")
async def read_data():
    return conn.execute(users.select()).fetchall()

@user.get("/{id}")
async def read_data(id:int):
    return conn.execute(users.select().where(users.c.id==id)).fetchall()

@user.get("/")
async def read_data():
    return conn.execute(users.select()).fetchall()

@user.get("/")
async def read_data():
    return conn.execute(users.select()).fetchall()

@user.get("/")
async def read_data():
    return conn.execute(users.select()).fetchall()