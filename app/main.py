from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.api import api_router
from app.database.session import engine, Base
from app.core.config  import settings
 
app = FastAPI()
 
app.add_middleware(
   CORSMiddleware,
   allow_origins=["http://localhost:8080"],
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"],
)
 
app.include_router(api_router, prefix=settings.API_V1_STR)
 
@app.get("/health-check")
def health_check():
   return "OK"
