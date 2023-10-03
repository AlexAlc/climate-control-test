#include "../inc/heatingActuator.h"

// Constructor with optional parameter
HeatingActuator::HeatingActuator(int init_pump = 0) {
    resistor = OFF;
    water_pump = init_pump;
    pump_max = 100;
    pump_min = 0;
}

// Function to saturate values within the working range
int HeatingActuator::saturate(int val) {
    if (val < pump_min) {
        return pump_min;
    } else if (val > pump_max) {
        return pump_max;
    } else {
        return val;
    }
}

// Function to set heating parameters
void HeatingActuator::setHeating(int value) {
    // Saturate values between the working range
    water_pump = saturate(value);

    // Calculate corresponding working mode as discretization of the whole range.
    int fuzzy_value = 1 + water_pump / (100 / 3);

    // Saturate value
    if (fuzzy_value >= 4) {
        fuzzy_value = 3;
    }

    resistor = static_cast<resistor_states>(fuzzy_value);

    // After setting up, send the actual command to set hardware working state
    placeholderHeatingHW();
}

// Function to simulate a real call to hardware actuator or corresponding subsystem
void HeatingActuator::placeholderHeatingHW() {
    // Empty function to simulate a real call to hardware actuator or corresponding subsystem
}

// Getter for resistor state
resistor_states HeatingActuator::getResistorState() const {
    return resistor;
}
