## Document Management


In this example, we have a system that processes different types of documents, such as PDFs and Word documents, but it needs to be able to handle additional document types in the future. 

In the `original.py`, the code is tightly coupled to specific document types (PDF and Word documents). This version is harder to extend with new document types and violates the **Open/Closed Principle (OCP)**. 
Additionally, there is no common interface for different document types, making it difficult to process them uniformly.

In the `refactored.py`, we leverage **polymorphism** to define a common interface for all document types. Each document type implements this interface, allowing the system to process them uniformly. This version adheres to the **Open/Closed Principle (OCP)** and is easier to extend with new document types.

If we cannot modify the existing document classes, we can use the **Adapter** pattern to adapt them to a common interface. This way, we can still process different document types uniformly without changing their existing implementations. In the `refactored2.py`, we demonstrate how to use the **Adapter** pattern to achieve this.