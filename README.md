Solution in climate_control.py file. (actuators.py auxiliary file). Results of simulation saved in climate_log.csv.

# Introduction
Test for a climate control flow using heating and cooling to monitor desired ambient temperature.

A climate control system is an automated system that is responsible for regulating the environmental conditions in an enclosed space, such as a house, an office or a bus, to maintain a comfortable and suitable environment for the people in that space. The system can cool or heat, depending on the temperature value desired by the person and its difference with the temperature of the area to be controlled.

The person has the possibility to set the zone temperature between 18 and 30 degrees Celsius. This system when at rest has a low and high pressure value of 5 bar. As soon as cold is demanded, the high pressure starts to rise and the low pressure starts to fall. The high pressure can reach 25 bar pressure, while the low pressure can be as low as 0.5 bar.

## Subsystems

### Cooling
The cooling subsystem is composed of the following components:

- *Compressor*: It is activated when cooling is required and can be in 4 states OFF-MIN-MED-MAX. It is OFF when cooling is not required and the rest depends on the cooling demand.
- *Condenser* fans: They are activated when the compressor is activated and varies from 0-100, being 0 when no cooling is required and 100 when the cooling demand is maximum.

### Heating
The heat subsystem is composed of the following components:

- *Water pump*: activated when heat is required in the control zone to circulate water. It can range from 0-100, with 0 being no heat required and 100 being maximum heat demand.
- *Electric resistance*: It is activated when heat is required in the control zone to heat the water. It can be in three different states OFF-MIN-MED-MAX. It is OFF when no heat is demanded and the rest depends on the heat demand.

### Common elements

- *Zone temperature sensor*: measures the temperature of the zone to be controlled.
- *Evaporator fans*: They are used to introduce air into the climate control zone, both for cooling and heating. Their value varies from 10-100, being 10 when the desired temperature has been reached.

## Problem to solve
Having a program with a control algorithm for this system. To display the solution, the program must return an output file (csv, json), showing a set of values of each element for an input temperature value. In addition, it must be possible to observe on screen the behavior of the system for a desired input temperature value, showing the corresponding value of the rest of the system.

# Proposed solution

- Controller: As a controller a PID is used. The output value is discriminated depending on the sign activating cooling or heating. Constants should be tuned to be in practice a PI controller since heat/temperature has such a high inertia. Also when using higher order or advanced control techniques such as state space feedback or LQR maximum power can't probably be achieved wasting too much energy, so a slower approach is preferred.

- The power of the discrete elements is modeled as a fuzzy logic like manner. Insted a more simplier discretization of fixed step is used for the working range.

- The algorithm resembles a software simulator for software in the loop, but physics equation of the model are not implemented here only ideal ones.

- An Object Oriented design approach is used.