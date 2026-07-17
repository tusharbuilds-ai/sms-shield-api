import uvicorn
import joblib
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import v1_api
from schemas.return_schema import ReturnResponse
from fastapi import status


app = FastAPI(title="SMS Gaurd backend")
app.include_router(v1_api.router_v1,prefix="/api/v1",tags=["v1"])



app.add_middleware(
    CORSMiddleware,
    allow_headers=["*"],
    allow_methods=["*"],
    allow_origins=["*"],
)

@app.get("/")
def health():
    return ReturnResponse(
        status_code=status.HTTP_200_OK,
        status=True,
        message="SMS Gaurd backend is running"
    )




if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=8080,reload=True)