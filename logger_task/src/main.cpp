#include "Logger.h"
#include <iostream>
using namespace std;

int main() {
    Logger& logger = Logger::getInstance();
    
    logger.log(Logger::INFO, "Application started.");
    logger.log(Logger::WARN, "Low memory warning.");
    logger.log(Logger::ERROR, "An unexpected error occurred.");

    cout << "Logging completed. Check logs/application.log file." << endl;

    return 0;
}
