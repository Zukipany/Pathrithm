# Source code is private. This file shows only its classes and function signatures.

"""WorldStreet Algorithm Lab - FastAPI Backend"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router as api_router
app = ...


@app.get('/health')
async def health_check():
    ...
