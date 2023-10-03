#include "../inc/climate_control.h"

#include <unordered_map>

// Include the header files for the actuators
#include "../inc/coolingActuator.h"
#include "../inc/heatingActuator.h"
#include "../inc/evaporatorActuator.h"
#include "../inc/temperatureSensor.h"
#include "../lib/PID_v1.h" // Include the header file for the PID controller

ClimateControlUnit::ClimateControlUnit() {}

std::unordered_map<std::string, int> ClimateControlUnit::update(int desired_temperature) {
    // Control loop to run continuously

    // Read ambient temperature from sensor
    int current_temperature = tempSensor.readTemperatureSensor();

    // Controller logic. Tune to specification.
    PID pid(5, 0.01, 0.1);
    pid.setOutputLimits(0, 100);
    double controller_output = pid.compute(current_temperature, desired_temperature);

    if (controller_output < 0) {
        // Cooling control
        cooler.setCooling(std::abs(controller_output));              // Set actuator value
        evaporator.setEvaporatorFans(std::abs(controller_output));   // Set actuator value

    } else if (controller_output > 0) {
        // Heating control
        heater.setHeating(std::abs(controller_output));              // Set actuator value
        evaporator.setEvaporatorFans(std::abs(controller_output));   // Set actuator value

    } else {
        // Stop actuation
        // TODO: Add a timer or deadband to include hysteresis (don't jump from cooling to heating)
        cooler.setCooling(0);               // Set min value
        heater.setHeating(0);               // Set min value
        evaporator.setEvaporatorFans(10);   // Set min value
    }

    // Dictionary for storing the status of each variable for debugging purposes.
    std::unordered_map<std::string, int> status_dict = {
        {"desired_temperature", desired_temperature},
        {"compressor", cooler.getCompressorState()},
        {"condenser_fans", cooler.getCondenserFans()},
        {"resistor", heater.getResistorState()},
        {"water_pump", heater.getWaterPump()},
        {"evaporator_fans", evaporator.getEvaporatorFans()},
        {"temperature", tempSensor.readTemperatureSensor()}
    };

    return status_dict;
}
