from pydantic import BaseModel, Field


class CreateResponse(BaseModel):
    card_title: str = Field(
        description="Title of Card. Card represents the theme."
    )
    point_content: str = Field(
        description="Content of Point. Should be brief capturing the essence of the point."
    )
