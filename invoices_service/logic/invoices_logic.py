from models.db import invoices_collection
from models.models import Invoice, InvoiceCollection
from fastapi import HTTPException

async def generate_invoice(invoice: Invoice):
    """
    Generar una nueva factura para una institución
    """
    try:
        new_invoice = await invoices_collection.insert_one(
            invoice.model_dump(by_alias=True)
        )
        created_invoice = await invoices_collection.find_one({"_id": new_invoice.inserted_id})
        return created_invoice

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al generar factura: {str(e)}")


async def get_invoices():
    """
    Obtener todas las facturas
    """
    invoices = await invoices_collection.find().to_list(1000)
    return InvoiceCollection(invoices=invoices)
