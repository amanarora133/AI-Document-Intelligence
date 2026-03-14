import base64
from typing import Type
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from schemas import InvoiceSchema, MedicalRecordSchema

class DocumentProcessor:
    def __init__(self, model_name: str = "gpt-4o"):
        self.llm = ChatOpenAI(model=model_name)

    def _encode_image(self, image_path: str):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    def extract_data(self, file_path: str, schema: Type[BaseModel]):
        """Extract structured data from a document image or PDF."""
        base64_image = self._encode_image(file_path)
        
        # Structure the prompt based on the Pydantic schema
        schema_desc = schema.model_json_schema()
        
        message = HumanMessage(
            content=[
                {"type": "text", "text": f"Extract all details from this document following this exact JSON schema: {schema_desc}"},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
            ]
        )
        
        # Use structured output capabilities (with tools/functions)
        structured_llm = self.llm.with_structured_output(schema)
        result = structured_llm.invoke([message])
        return result

if __name__ == "__main__":
    # Example usage
    # processor = DocumentProcessor()
    # invoice = processor.extract_data("invoice.jpg", InvoiceSchema)
    # print(invoice.model_dump_json(indent=2))
    pass