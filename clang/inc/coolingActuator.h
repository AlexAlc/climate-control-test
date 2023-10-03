#ifndef _COOLER_H_
#define _COOLER_H_

typedef enum{
    OFF = 0U,
    MIN,
    MED,
    MAX 
} compressor_states;

class CoolingActuator {
private:
    compressor_states compressor;              // Current assigned state of operation
    int condenser_fans;                        // Fans of cooling stage. Possible values between 0 (min) and 100 (max)
    int fan_max;                               // Maximum allowed value
    int fan_min;                               // Minimum allowed value

public:
    // Constructor with optional parameter
    CoolingActuator(int init_condenser);

    // Function to saturate values within the working range
    int saturate(int val);

    // Function to set cooling parameters
    void setCooling(int value);

    // Function to simulate a real call to hardware actuator or corresponding subsystem
    void placeholderCoolingHW();

    // Getter for compressor state
    compressor_states getCompressorState() const;

    int getCondenserFans();
};

#endif //_COOLER_H_