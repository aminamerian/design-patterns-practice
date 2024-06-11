from abc import ABC, abstractmethod


class Document(ABC):

    @abstractmethod
    def open(self, file_path: str):
        pass

    @abstractmethod
    def read(self):
        pass


class PDFDocument(Document):

    def open(self, file_path: str):
        print(f"Opening PDF document from file: {file_path}")

    def read(self):
        print("Reading PDF document")


class WordDocument(Document):

    def open(self, file_path: str):
        print(f"Loading Word document from file: {file_path}")

    def read(self):
        print("Parsing Word document")


class DocumentProcessor:

    def process_document(self, document: Document, file_path: str):
        document.open(file_path)
        document.read()


# Usage
pdf_document = PDFDocument()
word_document = WordDocument()

processor = DocumentProcessor()
processor.process_document(pdf_document, "example.pdf")
processor.process_document(word_document, "example.docx")
