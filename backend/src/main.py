import uvicorn
from fastapi import FastAPI

from db.engine import init_db
from routers.activite import router as user
init_db()

app = FastAPI()
app.include_router(user)

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8009)