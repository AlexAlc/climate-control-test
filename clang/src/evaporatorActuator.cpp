#include "../inc/evaporatorActuator.h"

EvaporatorActuator::EvaporatorActuator(int init_fans = 10) {
    evaporator_fans = init_fans;
    fan_max = 100;
    fan_min = 10;
}

int EvaporatorActuator::saturate(int val) {
    if (val < fan_min) {
        return fan_min;
    } else if (val > fan_max) {
        return fan_max;
    } else {
        return val;
    }
}

void EvaporatorActuator::setEvaporatorFans(int value) {
    // Saturate values between the working range
    evaporator_fans = saturate(value);

    // After setting up, send the actual command to set hardware working state
    placeholderEvaporatorFansHW();
}

void EvaporatorActuator::placeholderEvaporatorFansHW() {
    // Empty function to simulate a real call to hardware actuator or corresponding subsystem
}

int EvaporatorActuator::getEvaporatorFans() const {
    return evaporator_fans;
}
