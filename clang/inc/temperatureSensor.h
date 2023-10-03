#ifndef _TEMPERATURE_SENSOR_H_
#define _TEMPERATURE_SENSOR_H_

class TemperatureSensor {
private:
    int temperature;      // Sensed temperature
    int temp_max;         // Maximum allowed value
    int temp_min;         // Minimum allowed value

public:
    // Constructor with optional parameter
    TemperatureSensor(int init_temp);

    // Function to saturate values within the working range
    int saturate(int val);

    // Function to set the temperature of the sensor
    void setTemperatureSensor(int value);

    // Function to read the temperature from the sensor
    int readTemperatureSensor() const;
};

#endif //_TEMPERATURE_SENSOR_H_