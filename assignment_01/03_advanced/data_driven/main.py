from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from databases import Database
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

app = FastAPI()
templates = Jinja2Templates(directory="templates")

DATABASE_URL = "sqlite:///./test.db"
database = Database(DATABASE_URL)
metadata = MetaData()

# Define a simple table
items = Table(
    "items",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("description", String),
)

engine = create_engine(DATABASE_URL)
metadata.create_all(engine)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/", response_class=HTMLResponse)
async def read_items(request: Request):
    query = items.select()
    results = await database.fetch_all(query)
    return templates.TemplateResponse("index.html", {"request": request, "items": results})


@app.post("/add", response_class=HTMLResponse)
async def add_item(request: Request, name: str = Form(...), description: str = Form(...)):
    query = items.insert().values(name=name, description=description)
    await database.execute(query)
    return await read_items(request)
