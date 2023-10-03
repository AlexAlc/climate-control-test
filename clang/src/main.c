#include <iostream>
#include <vector>
#include <unordered_map>
#include <fstream>
#include <string>

#include "../inc/climate_control.h"

int main() {
    ClimateControlUnit ccu;

    // Vector for storing the records of each time step
    std::vector<std::unordered_map<std::string, int>> registers;

    // Simulation of the system for a range of time
    int total_time = 60000;  // milliseconds
    int time_step = 1000;    // milliseconds
    int setpoint = 23;       // Celsius

    for (int epoch = 0; epoch < total_time; epoch += time_step) {
        std::unordered_map<std::string, int> results = ccu.update(setpoint);
        results["time"] = epoch;
        registers.push_back(results);
    }

    std::string log_file = "simulation_results.csv";

    // Save the results of the simulation to a CSV file
    std::ofstream csv_file(log_file);
    if (csv_file.is_open()) {
        std::vector<std::string> fields;
        for (const auto &entry : registers[0]) {
            fields.push_back(entry.first);
        }

        // Write CSV header
        for (size_t i = 0; i < fields.size(); ++i) {
            csv_file << fields[i];
            if (i < fields.size() - 1) {
                csv_file << ",";
            } else {
                csv_file << std::endl;
            }
        }

        // Write CSV data
        for (const auto &record : registers) {
            for (size_t i = 0; i < fields.size(); ++i) {
                csv_file << record[fields[i]];
                if (i < fields.size() - 1) {
                    csv_file << ",";
                } else {
                    csv_file << std::endl;
                }
            }
        }

        csv_file.close();
        std::cout << "Complete simulation. Results saved in " << log_file << std::endl;
    } else {
        std::cerr << "Error: Unable to open the CSV file for writing." << std::endl;
    }

    return 0;
}
