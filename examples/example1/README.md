# Logging System

This project demonstrates the implementation of a logging system.  

In the `original.py`, the logging system directly handles different types of log messages (info, warning, error) and routes them to different destinations (console, file, email). This version is tightly coupled and harder to extend.

In the `refactored.py`, the logging system uses the **Factory** and **Chain of Responsibility** design patterns to decouple the log message handling and routing logic. This version is more flexible and easier to extend with new log handlers and adheres to the **Single Responsibility Principle (SRP)** and **Open/Closed Principle (OCP)**.