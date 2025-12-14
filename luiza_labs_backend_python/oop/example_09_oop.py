from abc import ABC, abstractmethod, abstractproperty


class RemoteControl(ABC):
    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass

    @property
    @abstractmethod
    def brand(self):
        pass


class TVRemoteControl(RemoteControl):
    def on(self):
        print("Turn on the TV...")
        print("On!")

    def off(self):
        print("Turn off the TV...")
        print("Off!")

    @property
    def brand(self):
        return "TV Brand: Samsung"

class AirConditioningRemoteControl(RemoteControl):
    def on(self):
        print("Turn on the air conditioning...")
        print("On!")

    def off(self):
        print("Turn off the air conditioning...")
        print("Off!")

    @property
    def brand(self):
        return "Air Conditioning Brand : Samsung"

remote_control = TVRemoteControl()
remote_control.on()
remote_control.off()

air_conditioning_control = AirConditioningRemoteControl()
air_conditioning_control.on()
air_conditioning_control.off()

print(remote_control.brand)
print(air_conditioning_control.brand)