from fastapi import FastAPI, HTTPException
import uvicorn

from App.HTTP_logic.CRUD_attestation import router_attestation
from App.HTTP_logic.routers import list_routers
from data_base_property import init_db, db

app = FastAPI()

for i in list_routers:
    app.include_router(i)


def start_app(app=app, host='0.0.0.', port=8000):
    init_db(db)
    uvicorn.run(app, host='0.0.0.0', port=8000)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
