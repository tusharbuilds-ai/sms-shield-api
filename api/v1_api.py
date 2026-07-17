from fastapi import APIRouter
from api.routes import analize

router_v1 = APIRouter()


router_v1.include_router(analize.router,prefix="/analize")