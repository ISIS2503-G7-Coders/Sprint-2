import motor.motor_asyncio
from typing import Annotated
from pydantic.functional_validators import BeforeValidator

client = motor.motor_asyncio.AsyncIOMotorClient(
    "mongodb://admin:isis2503@10.128.0.86:27017?retryWrites=true&w=majority"
)
db = client.get_database("invoices_db")
invoices_collection = db.get_collection("invoices")

async def set_invoices_db():
    # Elimina el índice único existente si existe
    existing_indexes = await invoices_collection.index_information()
    if "institution_code_1" in existing_indexes:
        await invoices_collection.drop_index("institution_code_1")

    # Crea un índice no único en institution_code (si lo necesitas)
    await invoices_collection.create_index("institution_code")


# Representa un ObjectId en la base de datos
PyObjectId = Annotated[str, BeforeValidator(str)]