from models.db import invoices_collection
from models.models import Invoice, InvoiceCollection
from fastapi import HTTPException
from bson import ObjectId

async def generate_invoice(invoice: Invoice):
    """
    Generar una nueva factura para una institución
    """
    try:
        invoice_data = invoice.model_dump(by_alias=True, exclude_unset=True)
        result = await invoices_collection.insert_one(invoice_data)
        created_invoice = await invoices_collection.find_one({"_id": result.inserted_id})
        if created_invoice:
            created_invoice["_id"] = str(created_invoice["_id"])  # Convertir ObjectId a str
        return created_invoice

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al generar factura: {str(e)}")


async def get_invoices():
    """
    Obtener todas las facturas
    """
    invoices = await invoices_collection.find().to_list(1000)
    for invoice in invoices:
        invoice["_id"] = str(invoice["_id"])  # Convertir ObjectId a str
    return InvoiceCollection(invoices=invoices)
