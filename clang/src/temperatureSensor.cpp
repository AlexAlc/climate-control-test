#include "../inc/temperatureSensor.h"

TemperatureSensor::TemperatureSensor(int init_temp = 20) {
    temperature = init_temp;
    temp_max = 100;
    temp_min = -100;
}

int TemperatureSensor::saturate(int val) {
    if (val < temp_min) {
        return temp_min;
    } else if (val > temp_max) {
        return temp_max;
    } else {
        return val;
    }
}

void TemperatureSensor::setTemperatureSensor(int value) {
    // Placeholder for a real hardware sensor. Used only within simulation.
    temperature = saturate(value);
}

int TemperatureSensor::readTemperatureSensor() const {
    return temperature;
}
