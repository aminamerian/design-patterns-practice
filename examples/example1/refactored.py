from abc import ABC, abstractmethod


# Chain of Responsibility pattern: Abstract Handler
class LogHandler(ABC):

    def __init__(self):
        self._next_handler = None

    def set_next_handler(self, next_handler):
        self._next_handler = next_handler
        return next_handler

    @abstractmethod
    def handle_log(self, message: str, type: str):
        if self._next_handler:
            self._next_handler.handle_log(message, type)


# Chain of Responsibility pattern: Concrete Handlers
class ConsoleLogHandler(LogHandler):

    def handle_log(self, message: str, type: str):
        if type == "info":
            print(f"Console Log: {message}")
        else:
            super().handle_log(message, type)


class FileLogHandler(LogHandler):

    def handle_log(self, message: str, type: str):
        if type == "warning":
            with open("log.txt", "a") as file:
                file.write(f"File Log: {message}\n")
        else:
            super().handle_log(message, type)


class EmailLogHandler(LogHandler):

    def handle_log(self, message: str, type: str):
        if type == "error":
            print(f"Email Alert: {message}")
        else:
            super().handle_log(message, type)


# Factory pattern
class LoggerFactory:
    @staticmethod
    def create_logger_chain():
        console_log_handler = ConsoleLogHandler()
        file_log_handler = FileLogHandler()
        email_log_handler = EmailLogHandler()

        console_log_handler.set_next_handler(file_log_handler).set_next_handler(
            email_log_handler
        )
        return console_log_handler


# Usage
logger_chain = LoggerFactory.create_logger_chain()

logger_chain.handle_log(message="This is an informational message", type="info")
logger_chain.handle_log(message="This is a warning message", type="warning")
logger_chain.handle_log(message="This is an error message", type="error")
