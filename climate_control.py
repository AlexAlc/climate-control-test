from actuators import evaporatorActuator
from actuators import coolingActuator
from actuators import heatingActuator
from actuators import temperatureSensor

class ClimateControlUnit:
    """
    Climate control unit including a sensor to read the ambient temperature, a cooling subsystem, a heating subsystem and evaporator fans.
    """

    def __init__(self):
        self.cooler = coolingActuator()         # Cooling unit
        self.heater = heatingActuator()         # Heating unit
        self.evaporator = evaporatorActuator()  # Evaporator unit
        self.tempSensor = temperatureSensor()   # Temperature sensor

    def update(self, desired_temperature):
        # Control loop to run continuosly
        
        # Read ambient temperature from sensor
        current_temperature = self.tempSensor.readTemperatureSensor()

        # Calculates the temperature difference
        temperature_difference = desired_temperature - current_temperature

        # Controller logic
        controller_output = 0

        if controller_output < 0:
            # Cooling control
            pass
        elif controller_output > 0:
            # Heating control
            pass
        else:
            # Stop actuation
            # TODO Add a timer or deadband to include hysteresis (don't jump from cooling to heating)
            self.cooler.setCooling(0)               # Set min value
            self.heater.setHeating(0)               # Set min value
            self.evaporator.setEvaporatorFans(10)   # Set min value

