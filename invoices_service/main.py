import uvicorn
from fastapi import FastAPI
from models import db
from views import invoices_view

def create_app():
    app = FastAPI(
        docs_url="/invoices/docs",
        openapi_url="/invoices/openapi.json",
        redoc_url=None,
    )

    @app.on_event("startup")
    async def on_startup():
        await db.set_invoices_db()
        
    @app.get("/health-check")
    async def health_check():
        return {"status": "OK"}    

    app.include_router(invoices_view.router, prefix="/api")

    return app


if __name__ == "__main__":
    app = create_app()
    uvicorn.run(app, host="0.0.0.0", port=8080)
