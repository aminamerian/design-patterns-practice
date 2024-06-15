class WeatherData:
    def __init__(self):
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0
        self.phone_display = None
        self.tv_display = None
        self.computer_display = None

    def set_temperature(self, temperature):
        self.temperature = temperature
        self.notify_displays()

    def set_humidity(self, humidity):
        self.humidity = humidity
        self.notify_displays()

    def set_pressure(self, pressure):
        self.pressure = pressure
        self.notify_displays()

    def notify_displays(self):
        if self.phone_display:
            self.phone_display.update(self.temperature, self.humidity, self.pressure)
        if self.tv_display:
            self.tv_display.update(self.temperature, self.humidity, self.pressure)
        if self.computer_display:
            self.computer_display.update(self.temperature, self.humidity, self.pressure)

class PhoneDisplay:
    def update(self, temperature, humidity, pressure):
        print(f"Phone Display - Temperature: {temperature}, Humidity: {humidity}, Pressure: {pressure}")

class TVDisplay:
    def update(self, temperature, humidity, pressure):
        print(f"TV Display - Temperature: {temperature}, Humidity: {humidity}, Pressure: {pressure}")

class ComputerDisplay:
    def update(self, temperature, humidity, pressure):
        print(f"Computer Display - Temperature: {temperature}, Humidity: {humidity}, Pressure: {pressure}")

# Usage
weather_data = WeatherData()
phone_display = PhoneDisplay()
tv_display = TVDisplay()
computer_display = ComputerDisplay()

weather_data.phone_display = phone_display
weather_data.tv_display = tv_display
weather_data.computer_display = computer_display

weather_data.set_temperature(25)
weather_data.set_humidity(60)
weather_data.set_pressure(1013)
