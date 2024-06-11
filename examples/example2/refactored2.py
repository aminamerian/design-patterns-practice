from abc import ABC, abstractmethod


class PDFDocument:
    def open(self, file_path):
        print(f"Opening PDF document from file: {file_path}")

    def read(self):
        print("Reading PDF document")


class WordDocument:
    def load(self, file_path):
        print(f"Loading Word document from file: {file_path}")

    def parse(self):
        print("Parsing Word document")


# Adapter pattern: Document interface
class Document(ABC):

    @abstractmethod
    def open(self, file_path):
        pass

    @abstractmethod
    def read(self):
        pass


# Adapter pattern: Adapters
class PDFDocumentAdapter(Document):

    def __init__(self, pdf_document):
        self.pdf_document = pdf_document

    def open(self, file_path):
        self.pdf_document.open(file_path)

    def read(self):
        self.pdf_document.read()


class WordDocumentAdapter(Document):

    def __init__(self, word_document):
        self.word_document = word_document

    def open(self, file_path):
        self.word_document.load(file_path)

    def read(self):
        self.word_document.parse()


class DocumentProcessor:

    def process_document(self, document: Document, file_path: str):
        document.open(file_path)
        document.read()


# Usage
pdf_document = PDFDocument()
word_document = WordDocument()

pdf_adpter = PDFDocumentAdapter(pdf_document)
word_adapter = WordDocumentAdapter(word_document)

processor = DocumentProcessor()
processor.process_document(pdf_adpter, "example.pdf")
processor.process_document(word_adapter, "example.docx")
