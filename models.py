import uuid
from datetime import datetime
from typing import List, Optional, Union
from pydantic import BaseModel, Field

class Topic(BaseModel):
  topic: str
  description: str
  requestUrl: str
  createdAt: int
  updatedAt: Optional[int]
  lastSync: Optional[int]
  available: bool

class CrawlerSource(BaseModel):
  id: str = Field(default_factory=uuid.uuid4, alias="_id")
  name: str = Field(...)
  description: str = Field(...)
  topics: Optional[List[Topic]]
  sourceDomain: str = Field(...)
  crawlerSchema: str = Field(...)
  createdAt: int = Field(...)
  updatedAt: Optional[int]
  scheduleSync: Optional[int]
  lastSync: Optional[int]
  enabled: bool = Field(...)

  class Config:
    # 指定映射的 MongoDB 集合名稱
    collection = "crawler_source"
    allow_population_by_field_name = True
    schema_extra = {
      "example": {
        "_id":"066de609-b04a-4b30-b46c-32537c7f1f6e",
        "name":"○○雜誌",
        "description":"○○雜誌，是台灣第一本專業的新聞財經雜誌",
        "topics":[{
          "topic":"美國銀行",
          "description":"因為美國矽谷銀行倒閉事件...",
          "requestUrl":"https://www.google.com/search?q=美國銀行+site:cw.com.tw&tbm=nws",
          "createdAt": 1682480123767,
          "updatedAt": None,
          "lastSync": None,
          "available": False
        }],
        "sourceDomain":"crawler-domain.com",
        "crawlerSchema":"",
        "createdAt": 1682480123767,
        "updatedAt": None,
        "scheduleSync":None,
        "lastSync": 1682481844407,
        "enabled": True
      }
    }

class Meta(BaseModel):
    metaKey: str
    metaValue: List[str]
    available: bool

class CrawlerData(BaseModel):
    _id: str = Field(default_factory=uuid.uuid4, alias="_id")
    sourceId: str = Field(default_factory=uuid.uuid4, alias="_id")
    sourceName: str = Field(...)
    topic: str = Field(...)
    sourceUrl: str = Field(...)
    sourceUpdatedAt: Optional[int]
    sourceAvailable: bool = Field(...)
    title: str = Field(...)
    content: str = Field(...)
    featuredImage: str = Field(...)
    images: Optional[List[str]]
    metas: Optional[List[Meta]]
    createdAt: int = Field(...)
    updatedAt: Optional[int]
    lastSync: Optional[int]
    available: bool = Field(...)

    class Config:
        # 指定映射的 MongoDB 集合名稱
        collection = "crawler_data"
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6f",
                "sourceId": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "sourceName": "○○雜誌",
                "topic": "美國銀行",
                "sourceUrl": "/article/5124997",
                "sourceUpdatedAt": None,
                "sourceAvailable": True,
                "title": "矽谷銀行爆雷，美國銀行股全線跳水，發生什麼事？",
                "content": "",
                "featuredImage": "",
                "images": [],
                "metas": [
                    {
                        "metaKey": "tags",
                        "metaValue": [],
                        "available": True
                    }
                ],
                "createdAt": 1682483219896,
                "updatedAt": None,
                "lastSync": 1682483219896,
                "available": True
            }
        }