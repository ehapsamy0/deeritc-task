#include "Logger.h"
#include <iostream>

int main() {
    Logger& logger = Logger::getInstance();
    
    logger.log(Logger::INFO, "Application started.");
    logger.log(Logger::WARN, "Low memory warning.");
    logger.log(Logger::ERROR, "An unexpected error occurred.");

    std::cout << "Logging completed. Check logs/application.log file." << std::endl;

    return 0;
}
