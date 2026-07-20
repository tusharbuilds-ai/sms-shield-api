from fastapi import APIRouter
from schemas.analytics_schema import AnalyticsSchema
from util import info,success
from schemas.return_schema import ReturnResponse
from services.agent_service import ai_analytics

router = APIRouter()

@router.post("")
def perform_analytics(payload:AnalyticsSchema):
    info("Request incoming for analytics.")

    result = ai_analytics(payload.messages,payload.senders,payload.timestamps)
    info(f"Analytics returned - > {result}")
    success("Analytics returned successfully.")
    return ReturnResponse(
        status_code=200,
        status=True,
        message="Analytics performed successfully!",
        data=result
    )


