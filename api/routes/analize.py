from fastapi import APIRouter, Depends
from util import get_model,get_vectorization
from schemas.analize_schema import AnalyzeSchema
from schemas.return_schema import ReturnResponse
from services.agent_service import ai_explaination

router = APIRouter()


@router.post("")
def analize(payload:AnalyzeSchema,model = Depends(get_model),vectorizor = Depends(get_vectorization)):
        vector_message = vectorizor.transform([payload.message])
        prediction = model.predict(vector_message)[0]

        ai_explain = ai_explaination(
            payload.message,
            payload.sender,
            prediction,
            payload.language
        )

        return ReturnResponse(
            status_code=200,
            status=True,
            message="Message analyzed!",
            data={"AI Explanation":ai_explain}
        )
