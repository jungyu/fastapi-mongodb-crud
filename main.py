import os
from fastapi import FastAPI
from pymongo import MongoClient
from routes import router as api_router

app = FastAPI()


# Default root endpoint
@app.get("/")
async def root():
  return {"message": "Hello Crawler API"}


@app.on_event("startup")
def startup_db_client():
  username = os.getenv('USERNAME')
  password = os.getenv('PASSWORD')
  clustername = os.getenv('MONGODB_CLUSTER')
  database = os.getenv('DATABASE')
  atlasUri = f"mongodb+srv://{username}:{password}@{clustername}/?retryWrites=true&w=majority"
  print(atlasUri)
  app.mongodb_client = MongoClient(atlasUri, serverSelectionTimeoutMS=5000)
  app.database = app.mongodb_client[database]
  # 呼叫 list_database_names() 方法檢查是否連線成功
  if database in app.mongodb_client.list_database_names():
    print("連線成功！")
  else:
    print("連線失敗！")


@app.on_event("shutdown")
def shutdown_db_client():
  app.mongodb_client.close()


app.include_router(api_router, tags=["api"], prefix="/api")
