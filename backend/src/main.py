import uvicorn
from fastapi import FastAPI

from db.engine import init_db, drop_db
from routers import router as user
from auth.routers import auth_app

init_db()

app = FastAPI()

app.include_router(user)
app.include_router(auth_app)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
