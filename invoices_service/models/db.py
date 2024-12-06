import motor.motor_asyncio
from typing import Annotated
from pydantic.functional_validators import BeforeValidator

client = motor.motor_asyncio.AsyncIOMotorClient(
    "mongodb://admin:isis2503@10.128.0.88:27017?retryWrites=true&w=majority"
)
db = client.get_database("invoices_db")
invoices_collection = db.get_collection("invoices")

async def set_invoices_db():
    # Crea índices únicos en `institution_code` y `_id`
    await invoices_collection.create_index("institution_code", unique=True)


# Representa un ObjectId en la base de datos
PyObjectId = Annotated[str, BeforeValidator(str)]