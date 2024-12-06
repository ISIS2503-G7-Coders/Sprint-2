from pydantic import BaseModel, Field, ConfigDict
from typing import List
from models.db import PyObjectId
from typing import Optional

# Modelo de factura individual
class Invoice(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    institution_code: str = Field(..., description="Código de la institución")
    amount: float = Field(..., description="Monto total de la factura")
    date: str = Field(..., description="Fecha de emisión")

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "institution_code": "INST001",
                "amount": 1500.75,
                "date": "2024-01-01"
            }
        },
    )


# Colección de facturas
class InvoiceCollection(BaseModel):
    invoices: List[Invoice] = Field(...)