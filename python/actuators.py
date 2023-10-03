
class evaporatorActuator:
    """
    Simple simulation of an evaporator system which can create air with fans.
    """

    def __init__(self, init_fans=10):
        self.evaporator_fans = init_fans    # Possible values between 10 (min) and 100 (max)
        self.fan_max = 100                  # Maximun alowed value
        self.fan_min = 10                   # Minimum alowed value

    def saturate(self, val):
        if val < self.fan_min:
            sat_val = self.fan_min
        elif val > self.fan_max:
            sat_val = self.fan_max
        else:
            sat_val = val
        
        return sat_val

    def setEvaporatorFans(self, value):
        # Saturate values between working range
        self.evaporator_fans = self.saturate(value)

        # After setting up, send actual command to set hardware working state
        self.placeholderEvaporatorFansHW()

    def placeholderEvaporatorFansHW(self):
        # Empty function to simulate a real call to hardware actuator or corresponding subsystem
        pass
        

class coolingActuator:
    """
    Simple simulation of a cooling system which can create cool air.
    TODO: Future implementation using abstract class with generic structure common to cooling and heating and create derived class using inheritance.
    """

    def __init__(self, init_condenser=0):
        self.compressor_states = ['OFF','MIN','MED','MAX']  # Different states of operation possible for compressor
        self.compressor = self.compressor_states[0]         # Current assigned state of operation
        self.condenser_fans = init_condenser                # Fans of cooling stage. Possible values between 0 (min) and 100 (max)
        self.fan_max = 100                                  # Maximun alowed value
        self.fan_min = 0                                    # Minimum alowed value

    def saturate(self, val):
        if val < self.fan_min:
            sat_val = self.fan_min
        elif val > self.fan_max:
            sat_val = self.fan_max
        else:
            sat_val = val
        
        return sat_val

    def setCooling(self, value):
        # Saturate values between working range
        self.condenser_fans = self.saturate(value)

        # Calculate corresponding working mode as discretization of whole range.
        fuzzy_value = 1 + self.condenser_fans / (100 / 3);

        # Saturate value
        if fuzzy_value >= 4:
            fuzzy_value = 3

        self.compressor = self.compressor_states[int(fuzzy_value)]

        # After setting up, send actual command to set hardware working state
        self.placeholderCoolingHW()

    def placeholderCoolingHW(self):
        # Empty function to simulate a real call to hardware actuator or corresponding subsystem
        pass
        

class heatingActuator:
    """
    Simple simulation of a heating system which can create hot air.
    TODO: Future implementation using abstract class with generic structure common to cooling and heating and create derived class using inheritance.
    """

    def __init__(self, init_pump=0):
        self.resistor_states = ['OFF','MIN','MED','MAX']    # Different states of operation possible for resistor
        self.resistor = self.resistor_states[0]             # Current assigned state of operation
        self.water_pump = init_pump                         # Pump of heating stage. Possible values between 0 (min) and 100 (max)
        self.pump_max = 100                                 # Maximun alowed value
        self.pump_min = 0                                   # Minimum alowed value

    def saturate(self, val):
        if val < self.pump_min:
            sat_val = self.pump_min
        elif val > self.pump_max:
            sat_val = self.pump_max
        else:
            sat_val = val
        
        return sat_val

    def setHeating(self, value):
        # Saturate values between working range
        self.water_pump = self.saturate(value)

        # Calculate corresponding working mode as discretization of whole range.
        fuzzy_value = 1 + self.water_pump / (100 / 3);

        # Saturate value
        if fuzzy_value >= 4:
            fuzzy_value = 3
            
        self.resistor = self.resistor_states[int(fuzzy_value)]

        # After setting up, send actual command to set hardware working state
        self.placeholderHeatingHW()

    def placeholderHeatingHW(self):
        # Empty function to simulate a real call to hardware actuator or corresponding subsystem
        pass
        
class temperatureSensor:
    """
    Simple simulation of a temperature sensor.
    """

    def __init__(self, init_temp=20):
        self.temperature = init_temp    # Sensed temperature
        self.temp_max = 100             # Maximun alowed value
        self.temp_min = -100            # Minimum alowed value

    def saturate(self, val):
        if val < self.temp_min:
            sat_val = self.temp_min
        elif val > self.temp_max:
            sat_val = self.temp_max
        else:
            sat_val = val
        
        return sat_val

    def setTemperatureSensor(self, value):
        # Placeholder for a real hardware sensor. Used only within simulation.
        self.temperature = self.saturate(value)


    def readTemperatureSensor(self):
        # Empty function to simulate a real call to hardware actuator or corresponding subsystem
        return self.temperature


if __name__ == "__main__":
    evaporator = evaporatorActuator(0)
    evaporator.setEvaporatorFans(33)

    print(f"Evaporators condenser fans: {evaporator.evaporator_fans}")

    cooler = coolingActuator(0)
    cooler.setCooling(20)

    print(f"Cooling compressor: {cooler.compressor}")
    print(f"Cooling condenser fans: {cooler.condenser_fans}")

    heater = heatingActuator(0)
    heater.setHeating(55)

    print(f"Heating resistor: {heater.resistor}")
    print(f"Heating water_pump: {heater.water_pump}")
