## Weather Station

In this example, we have a weather station that notifies various displays (e.g., a phone display, a TV display, and a computer display) whenever the weather data changes.

In the `original.py`
 - The `WeatherData` class is tightly coupled to the display classes.
-  It is difficult to add new types of displays or change the existing ones without modifying the `WeatherData` class, violating the **Open/Closed Principle (OCP)**.

In the `refactored.py`, the weather station uses the **Observer** design pattern to decouple the weather data from the display classes.
The `WeatherData` class maintains a list of observers (display classes) and notifies them when the weather data changes. Each display class implements the `Observer` interface to receive updates from the weather station.
- Open/Closed Principle (OCP) is adhered to by allowing new display classes to be added without modifying the `WeatherData` class.
- The Observer pattern allows for a loosely coupled design where the weather data and display classes can vary independently.