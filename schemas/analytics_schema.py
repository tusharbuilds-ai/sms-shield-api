from pydantic import BaseModel,Field


class AnalyticsSchema(BaseModel):
    senders:list[str] = Field(...,description="Enter Sender")
    messages:list[str] = Field(...,description="Enter Message")
    timestamps:list[int] = Field(...,description="Enter TimeStamps")
