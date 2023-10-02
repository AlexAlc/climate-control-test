
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
        
