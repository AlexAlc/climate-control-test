#ifndef _CLIMATE_CONTROL_H_
#define _CLIMATE_CONTROL_H_

#include <unordered_map>

// Include the header files for the actuators
#include "coolingActuator.h"
#include "heatingActuator.h"
#include "evaporatorActuator.h"
#include "temperatureSensor.h"
#include "../lib/PID_v1.h" // Include the header file for the PID controller

class ClimateControlUnit {
private:
    CoolingActuator cooler;      // Cooling unit
    HeatingActuator heater;      // Heating unit
    EvaporatorActuator evaporator;  // Evaporator unit
    TemperatureSensor tempSensor;   // Temperature sensor

public:
    // Constructor
    ClimateControlUnit();

    // Update method
    std::unordered_map<std::string, int> update(int desired_temperature);
};


#endif //_CLIMATE_CONTROL_H_