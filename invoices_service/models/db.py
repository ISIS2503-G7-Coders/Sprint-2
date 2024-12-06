import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient(
    "mongodb://localhost:27017/"
)
db = client.get_database("invoices_db")
invoices_collection = db.get_collection("invoices")

async def set_invoices_db():
    # Crea índices únicos en `institution_code` y `_id`
    await invoices_collection.create_index("institution_code", unique=True)


# Representa un ObjectId en la base de datos
PyObjectId = Annotated[str, BeforeValidator(str)]