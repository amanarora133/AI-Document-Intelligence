from pydantic import BaseModel, Field
from typing import List, Optional

class InvoiceItem(BaseModel):
    description: str = Field(..., description="Description of the item or service")
    quantity: float = Field(..., description="The quantity provided")
    unit_price: float = Field(..., description="The price per unit")
    total: float = Field(..., description="The total amount for this item")

class InvoiceSchema(BaseModel):
    invoice_number: str = Field(..., description="The unique invoice identifier")
    date: str = Field(..., description="The date of the invoice")
    vendor_name: str = Field(..., description="Name of the company providing the service")
    vendor_address: Optional[str] = Field(None, description="Physical address of the vendor")
    customer_name: str = Field(..., description="Name of the customer or recipient")
    items: List[InvoiceItem] = Field(..., description="List of items or services billed")
    total_amount: float = Field(..., description="The grand total of the invoice")
    currency: str = Field("USD", description="The currency of the invoice")
    tax_amount: Optional[float] = Field(None, description="The total tax amount billed")

class MedicalRecordSchema(BaseModel):
    patient_name: str = Field(..., description="The full name of the patient")
    date_of_birth: str = Field(..., description="The patient's date of birth")
    diagnoses: List[str] = Field(..., description="List of medical diagnoses mentioned")
    medications: List[str] = Field(..., description="List of medications prescribed")
    vital_signs: Optional[dict] = Field(None, description="Dictionary of vital signs like blood pressure, heart rate")