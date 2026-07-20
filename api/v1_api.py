from fastapi import APIRouter
from api.routes import analize
from api.routes import analytics
router_v1 = APIRouter()


router_v1.include_router(analize.router,prefix="/analize")
router_v1.include_router(analytics.router,prefix="/analytics")