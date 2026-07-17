from pydantic import BaseModel

class AnalyzeSchema(BaseModel):
    sender:str
    message:str
    language:str