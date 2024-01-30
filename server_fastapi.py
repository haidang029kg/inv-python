import asyncio

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from tortoise import Tortoise

import src.settings as settings
from src.api.fastapi import PurchaseRouter, SaleOrderRouter

app = FastAPI(version=settings.VERSION, title="Pet Store")
app.add_middleware(
    CORSMiddleware,
    # TODO: Change this to the frontend URL
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def root():
    return {"message": "Hello World"}


app.include_router(PurchaseRouter(), prefix="/purchases", tags=["purchases"])
app.include_router(
    SaleOrderRouter(), prefix="/sale-orders", tags=["sale-orders"]
)


@app.on_event("startup")
async def startup():
    if not await settings.check_db_connection(uri=settings.DATABASE_URI):
        raise Exception("Can not connect to the database")
    await Tortoise.init(config=settings.TORTOISE_ORM)


@app.on_event("shutdown")
async def shutdown():
    await Tortoise.close_connections()


async def run_command():
    await startup()
    await shutdown()


if __name__ == "__main__":
    asyncio.run(run_command())
