class Logger:
    def log(self, message, log_type):
        if log_type == 'info':
            self.log_to_console(message)
        elif log_type == 'warning':
            self.log_to_file(message)
        elif log_type == 'error':
            self.send_email_alert(message)
        else:
            print("Invalid log type")

    def log_to_console(self, message):
        print(f"Console Log: {message}")

    def log_to_file(self, message):
        with open("log.txt", "a") as file:
            file.write(f"File Log: {message}\n")

    def send_email_alert(self, message):
        print(f"Email Alert: {message}")

# Usage
logger = Logger()
logger.log("This is an informational message", 'info')
logger.log("This is a warning message", 'warning')
logger.log("This is an error message", 'error')
