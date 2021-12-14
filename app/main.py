from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.api import api_router
from app.core.config  import settings
 
app = FastAPI()
 
app.add_middleware(
   CORSMiddleware,
   allow_origins=["*"],
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"],
)
 
app.include_router(api_router, prefix=settings.API_V1_STR)
@app.get("/")
async def root():
    return {"message": "Hello World"}
    
@app.get("/health-check")
def health_check():
   return "OK"
