# AI Document Intelligence 📄🧠

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Multimodal](https://img.shields.io/badge/Multimodal-GPT--4o_/_Gemini-purple)](https://openai.com/)
[![Pydantic](https://img.shields.io/badge/Pydantic-Type_Safe-red)](https://docs.pydantic.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**AI Document Intelligence** is a production-ready multimodal pipeline designed to transform unstructured documents (Invoices, Receipts, Medical Records, Hand-written notes) into high-fidelity, structured JSON data. By leveraging Multimodal Large Language Models (LLMs) and Pydantic's strict schema enforcement, this project ensures type-safety and data integrity for downstream applications.

## 🌟 Key Features

- **🖼️ Multimodal Extraction**: Processes both text-heavy PDFs and visual-heavy images (JPG/PNG/TIFF).
- **🛡️ Type-Safe Output**: Uses **Pydantic** to define strict schemas, ensuring extracted data matches expected formats (dates, currencies, nested lists).
- **✍️ Handwriting Recognition**: Superior performance on hand-written documents compared to traditional OCR.
- **🧩 Schema-Driven Prompting**: Automatically generates optimized prompts based on your Pydantic models.
- **📈 Scalable Pipeline**: Designed to handle batch processing with error handling and retry logic.

## 🏗️ How it Works

1.  **Ingestion**: Files are converted into base64 encoded images or passed directly as multimodal inputs.
2.  **Schema Definition**: You define a Pydantic model (e.g., InvoiceSchema).
3.  **Inference**: The Multimodal LLM (GPT-4o/Gemini) analyzes the visual layout and text content.
4.  **Validation**: Pydantic validates the LLM's output against your schema.
5.  **Serialization**: The final validated data is returned as a clean JSON/Dict object.

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- OpenAI API Key or Google AI Studio API Key

### Installation
`ash
git clone https://github.com/amanarora133/AI-Document-Intelligence.git
cd AI-Document-Intelligence
pip install -r requirements.txt
`

### Usage
`python
from main import DocumentProcessor
from schemas import InvoiceSchema

processor = DocumentProcessor(model_name="gpt-4o")
data = processor.extract_data(
    file_path="sample_invoice.pdf", 
    schema=InvoiceSchema
)

print(data.model_dump_json(indent=2))
`

## 🛠️ Tech Stack
- **Core LLM**: GPT-4o, Gemini 1.5 Pro, Claude 3.5 Sonnet
- **Validation**: Pydantic V2
- **Processing**: Pillow, PyMuPDF (fitz)
- **Framework**: LangChain / Instructor

---
Developed with ❤️ by [Aman Arora](https://github.com/amanarora133)