from pydantic import BaseModel


class FastSAMRequest(BaseModel):
    image_path: str


# class FastSAMResponse(list):
#     result: list
