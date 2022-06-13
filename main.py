import uvicorn
from fastapi import FastAPI

from endpoints.house import router as building_router

app = FastAPI(
    title="Constructor",
    docs_url="/constructor/docs",
    openapi_url="/constructor/openapi.json")

app.include_router(building_router, prefix="/constructor")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5000)

