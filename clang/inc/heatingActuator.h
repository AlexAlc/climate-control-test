#ifndef _HEATER_H_
#define _HEATER_H_

typedef enum{
    OFF = 0U,
    MIN,
    MED,
    MAX 
} resistor_states;

class HeatingActuator {
private:
    resistor_states resistor;                 // Current assigned state of operation
    int water_pump;                           // Pump of heating stage. Possible values between 0 (min) and 100 (max)
    int pump_max;                             // Maximum allowed value
    int pump_min;                             // Minimum allowed value

public:
    // Constructor with optional parameter
    HeatingActuator(int init_pump);

    // Function to saturate values within the working range
    int saturate(int val);

    // Function to set heating parameters
    void setHeating(int value);

    // Function to simulate a real call to hardware actuator or corresponding subsystem
    void placeholderHeatingHW();

    // Getter for resistor state
    resistor_states getResistorState() const;
};


#endif //_HEATER_H_