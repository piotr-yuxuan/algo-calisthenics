from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/greedy",
    tags=["Greedy"]
)


class RequestBody(BaseModel):
    pass


class ResponseBody(BaseModel):
    pass


@router.get(
    "/",
    response_model=ResponseBody,
    summary="This is my summary",
    description="This is my description",
    response_description="This is my response description")
async def endpoint(requestBody: RequestBody):
    return requestBody
