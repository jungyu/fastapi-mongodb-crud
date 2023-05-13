from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models import CrawlerSource, CrawlerData

router = APIRouter()


@router.post("/crawlersources",
             response_description="Create a new crawler source",
             status_code=status.HTTP_201_CREATED,
             response_model=CrawlerSource)
def create_crawler_source(request: Request, source: CrawlerSource = Body(...)):
  source = jsonable_encoder(source)
  new_source = request.app.database["crawler_source"].insert_one(source)
  created_source = request.app.database["crawler_source"].find_one(
    {"_id": new_source.inserted_id})
  return created_source


@router.get("/crawlersources",
            response_description="List all crawler sources",
            response_model=List[CrawlerSource])
def list_crawler_sources(request: Request):
  sources = list(request.app.database["crawler_source"].find(limit=100))
  return sources


@router.get("/crawlersources/{id}",
            response_description="Get a single crawler source by id",
            response_model=CrawlerSource)
def find_crawler_source(id: str, request: Request):
  if (source :=
      request.app.database["crawler_source"].find_one({"_id":
                                                        id})) is not None:
    return source

  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                      detail=f"Crawler source with ID {id} not found")


@router.put("/crawlersources/{id}",
            response_description="Update a crawler source",
            response_model=CrawlerSource)
def update_crawler_source(id: str,
                          request: Request,
                          source: CrawlerSource = Body(...)):
  source = {k: v for k, v in source.dict().items() if v is not None}

  if len(source) >= 1:
    update_result = request.app.database["crawler_source"].update_one(
      {"_id": id}, {"$set": source})

    if update_result.modified_count == 0:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                          detail=f"Crawler source with ID {id} not found")

  if (existing_source :=
      request.app.database["crawler_source"].find_one({"_id":
                                                        id})) is not None:
    return existing_source

  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                      detail=f"Crawler source with ID {id} not found")


@router.delete("/crawlersources/{id}",
               response_description="Delete a crawler source")
def delete_crawler_source(id: str, request: Request, response: Response):
  delete_result = request.app.database["crawler_source"].delete_one(
    {"_id": id})

  if delete_result.deleted_count == 1:
    response.status_code = status.HTTP_204_NO_CONTENT
    return response

  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                      detail=f"Crawler source with ID {id} not found")


# CrawlerData CRUD
@router.post("/crawlerdata",
             response_description="Create a new crawler data",
             status_code=status.HTTP_201_CREATED,
             response_model=CrawlerData)
def create_crawler_data(request: Request,
                        crawler_data: CrawlerData = Body(...)):
  crawler_data = jsonable_encoder(crawler_data)
  new_crawler_data = request.app.database["crawler_data"].insert_one(
    crawler_data)
  created_crawler_data = request.app.database["crawler_data"].find_one(
    {"_id": new_crawler_data.inserted_id})

  return created_crawler_data


@router.get("/crawlerdata",
            response_description="List all crawler data",
            response_model=List[CrawlerData])
def list_crawler_data(request: Request):
  crawler_data = list(request.app.database["crawler_data"].find(limit=100))
  return crawler_data


@router.get("/crawlerdata/{id}",
            response_description="Get a single crawler data by id",
            response_model=CrawlerData)
def find_crawler_data(id: str, request: Request):
  if (crawler_data :=
      request.app.database["crawler_data"].find_one({"_id": id})) is not None:
    return crawler_data

  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                      detail=f"Crawler data with ID {id} not found")


@router.put("/crawlerdata/{id}",
            response_description="Update a crawler data",
            response_model=CrawlerData)
def update_crawler_data(id: str,
                        request: Request,
                        crawler_data: CrawlerData = Body(...)):
  crawler_data = {
    k: v
    for k, v in crawler_data.dict().items() if v is not None
  }

  if len(crawler_data) >= 1:
    update_result = request.app.database["crawler_data"].update_one(
      {"_id": id}, {"$set": crawler_data})

    if update_result.modified_count == 0:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                          detail=f"Crawler data with ID {id} not found")

  if (existing_crawler_data :=
      request.app.database["crawler_data"].find_one({"_id": id})) is not None:
    return existing_crawler_data

  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                      detail=f"Crawler data with ID {id} not found")


@router.delete("/crawlerdata/{id}",
               response_description="Delete a crawler data")
def delete_crawler_data(id: str, request: Request, response: Response):
  delete_result = request.app.database["crawler_data"].delete_one({"_id": id})

  if delete_result.deleted_count == 1:
    response.status_code = status.HTTP_204_NO_CONTENT
    return response

  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                      detail=f"Crawler data with ID {id} not found")
