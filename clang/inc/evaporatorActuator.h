#ifndef _EVAPORATOR_H_
#define _EVAPORATOR_H_

class EvaporatorActuator {
private:
    int evaporator_fans;  // Evaporator fans level
    int fan_max;          // Maximum allowed value
    int fan_min;          // Minimum allowed value

public:
    // Constructor with optional parameter
    EvaporatorActuator(int init_fans);

    // Function to saturate values within the working range
    int saturate(int val);

    // Function to set the evaporator fans level
    void setEvaporatorFans(int value);
    // Function to simulate a real call to hardware actuator or corresponding subsystem
    void placeholderEvaporatorFansHW(void);

    // Getter for evaporator_fans
    int getEvaporatorFans(void) const;
};

#endif //_EVAPORATOR_H_