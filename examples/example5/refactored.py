from abc import ABC, abstractmethod
from typing import List


class Observer(ABC):

    @staticmethod
    def update(self, subject: "Subject") -> None:
        pass


class Subject(ABC):

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class WeatherData(Subject):

    def __init__(self):
        self._observers: List[Observer] = []
        self._temperature: float = 0.0
        self._humidity: float = 0.0
        self._pressure: float = 0.0

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def set_measurements(
        self, temperature: float = None, humidity: float = None, pressure: float = None
    ) -> None:
        if temperature is not None:
            self._temperature = temperature
        if humidity is not None:
            self._humidity = humidity
        if pressure is not None:
            self._pressure = pressure

        if temperature is not None or humidity is not None or pressure is not None:
            self.notify()

    @property
    def temperature(self) -> float:
        return self._temperature

    @property
    def humidity(self) -> float:
        return self._humidity

    @property
    def pressure(self) -> float:
        return self._pressure


class PhoneDisplay(Observer):

    def update(self, subject: Subject) -> None:
        if isinstance(subject, WeatherData):
            print(
                f"Phone Display - Temperature: {subject.temperature}, Humidity: {subject.humidity}, Pressure: {subject.pressure}"
            )


class TVDisplay(Observer):

    def update(self, subject: Subject) -> None:
        if isinstance(subject, WeatherData):
            print(
                f"TV Display - Temperature: {subject.temperature}, Humidity: {subject.humidity}, Pressure: {subject.pressure}"
            )


class ComputerDisplay(Observer):

    def update(self, subject: Subject) -> None:
        if isinstance(subject, WeatherData):
            print(
                f"Computer Display - Temperature: {subject.temperature}, Humidity: {subject.humidity}, Pressure: {subject.pressure}"
            )


weather_data = WeatherData()
weather_data.attach(PhoneDisplay())
weather_data.attach(TVDisplay())
weather_data.attach(ComputerDisplay())

weather_data.set_measurements(temperature=25)
weather_data.set_measurements(humidity=60)
weather_data.set_measurements(pressure=1013)
