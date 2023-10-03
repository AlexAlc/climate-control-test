#include "../inc/coolingActuator.h"

// Constructor with optional parameter
CoolingActuator::CoolingActuator(int init_condenser = 0) {
    compressor = OFF;
    condenser_fans = init_condenser;
    fan_max = 100;
    fan_min = 0;
}

int CoolingActuator::saturate(int val) {
    if (val < fan_min) {
        return fan_min;
    } else if (val > fan_max) {
        return fan_max;
    } else {
        return val;
    }
}

void CoolingActuator::setCooling(int value) {
    // Saturate values between the working range
    condenser_fans = saturate(value);

    // Calculate corresponding working mode as discretization of the whole range.
    int fuzzy_value = 1 + condenser_fans / (100 / 3);

    // Saturate value
    if (fuzzy_value >= 4) {
        fuzzy_value = 3;
    }

    compressor = static_cast<compressor_states>(fuzzy_value);

    // After setting up, send the actual command to set hardware working state
    placeholderCoolingHW();
}

void CoolingActuator::placeholderCoolingHW() {
    // Empty function to simulate a real call to hardware actuator or corresponding subsystem
}

compressor_states CoolingActuator::getCompressorState() const {
    return compressor;
}