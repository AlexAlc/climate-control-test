from actuators import evaporatorActuator
from actuators import coolingActuator
from actuators import heatingActuator
from actuators import temperatureSensor
from simple_pid.pid import PID

import csv

log_file = 'climate_log.csv'

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

        # Controller logic. Tune to specification.
        pid = PID(5, 0.01, 0.1, setpoint=desired_temperature)
        pid.output_limits = (0, 100)
        controller_output = pid(current_temperature)

        if controller_output < 0:
            # Cooling control
            self.cooler.setCooling(abs(controller_output))              # Set actuator value
            self.evaporator.setEvaporatorFans(abs(controller_output))   # Set actuator value

        elif controller_output > 0:
            # Heating control
            self.heater.setHeating(abs(controller_output))              # Set actuator value
            self.evaporator.setEvaporatorFans(abs(controller_output))   # Set actuator value

        else:
            # Stop actuation
            # TODO Add a timer or deadband to include hysteresis (don't jump from cooling to heating)
            self.cooler.setCooling(0)               # Set min value
            self.heater.setHeating(0)               # Set min value
            self.evaporator.setEvaporatorFans(10)   # Set min value

        # Dict for storing the status of each variable to show. Debugging pourpouses.
        status_dict = {
            "desired_temperature": desired_temperature, 
            "compressor": self.cooler.compressor, 
            "condenser_fans": self.cooler.condenser_fans, 
            "resistor": self.heater.resistor, 
            "water_pump": self.heater.water_pump, 
            "evaporator_fans": self.evaporator.evaporator_fans, 
            "temperature": self.tempSensor.temperature
        }

        return status_dict
    
if __name__ == "__main__":

    ccu = ClimateControlUnit()

    # List for storing the records of each time step
    registers = []

    # Simulation of the system for a range of time
    total_time = 60000  # miliseconds
    time_step = 1000    # miliseconds
    setpoint = 23       # Celsius

    for epoch in range(0, total_time, time_step):
        results = ccu.update(setpoint)
        results.update({"time": epoch})
        registers.append(results)
        
    # Save the results of the simulation on a CSV file
    with open(log_file, mode="w", newline="") as csv_file:
        fields = list(registers[0].keys())
        writer = csv.DictWriter(csv_file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(registers)

    print(f"Complete simulation. Results saved in {log_file}")
