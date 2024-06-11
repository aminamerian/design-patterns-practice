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


class DocumentProcessor:
    def process_document(self, document, file_path):
        if isinstance(document, PDFDocument):
            document.open(file_path)
            document.read()

        elif isinstance(document, WordDocument):
            document.load(file_path)
            document.parse()


# Usage
pdf_document = PDFDocument()
word_document = WordDocument()

processor = DocumentProcessor()
processor.process_document(pdf_document, "example.pdf")
processor.process_document(word_document, "example.docx")
