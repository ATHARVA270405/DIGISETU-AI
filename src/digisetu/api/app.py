from fastapi import FastAPI
from digisetu.config.settings import settings
app = FastAPI(
    title=settings.app_name,
    description="DigiSetu Backend Here",
    version='0.1.0'
)

@app.get("/health")
def health_check()->dict[str,str]:
    return{
        "status":"Healthy",
        "application":settings.app_name,
    }