
class evaporatorActuator:
    """
    Simple simulation of an evaporator system which can create air with fans.
    """

    def __init__(self):
        self.evaporator_fans = 10   # Possible values between 10 (min) and 100 (max)

    def setEvaporatorFans(self, value):
        # Saturate values between working range
        if value < 10:
            self.evaporator_fans = 10
        elif value > 100:
            self.evaporator_fans = 100
        else:
            self.evaporator_fans = value

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

    def __init__(self):
        self.compressor_states = ['OFF','MIN','MED','MAX']  # Different states of operation possible for compressor
        self.compressor = self.compressor_states[0]         # Current assigned state of operation
        self.condenser_fans = 0                             # Fans of cooling stage. Possible values between 0 (min) and 100 (max)

    def setCooling(self, value):
        # Saturate values between working range
        if value < 0:
            self.condenser_fans = 0
        elif value > 100:
            self.condenser_fans = 100
        else:
            self.condenser_fans = value

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

    def __init__(self):
        self.resistor_states = ['OFF','MIN','MED','MAX']    # Different states of operation possible for resistor
        self.resistor = self.resistor_states[0]             # Current assigned state of operation
        self.water_pump = 0                                 # Pump of heating stage. Possible values between 0 (min) and 100 (max)

    def setHeating(self, value):
        # Saturate values between working range
        if value < 0:
            self.water_pump = 0
        elif value > 100:
            self.water_pump = 100
        else:
            self.water_pump = value

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
        
