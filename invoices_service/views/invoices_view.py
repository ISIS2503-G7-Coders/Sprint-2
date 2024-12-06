from fastapi import APIRouter, status, Body
from models.models import Invoice, InvoiceCollection
import logic.invoices_logic as invoice_service

router = APIRouter()
ENDPOINT_NAME = "/invoices"

@router.post(
    "/",
    response_description="Generar una nueva factura",
    response_model=Invoice,
    status_code=status.HTTP_201_CREATED,
)
async def generate_invoice(invoice: Invoice = Body(...)):
    return await invoice_service.generate_invoice(invoice)


@router.get(
    "/",
    response_description="Obtener todas las facturas",
    response_model=InvoiceCollection,
    status_code=status.HTTP_200_OK,
)
async def get_invoices():
    return await invoice_service.get_invoices()
