#include "Logger.h"
#include <iostream>
#include <thread>
#include <vector>

// Test function for multithreaded logging
void logMessages(const std::string& message, Logger::LogLevel level) {
    Logger& logger = Logger::getInstance();
    for (int i = 0; i < 10; ++i) {
        logger.log(level, message + " " + std::to_string(i));
    }
}

int main() {
    std::vector<std::thread> threads;
    
    // Create multiple threads for concurrent logging
    threads.push_back(std::thread(logMessages, "Message from thread 1", Logger::INFO));
    threads.push_back(std::thread(logMessages, "Message from thread 2", Logger::WARN));
    threads.push_back(std::thread(logMessages, "Message from thread 3", Logger::ERROR));
    
    for (auto& t : threads) {
        t.join();
    }

    std::cout << "Logging completed. Check the logs/application.log file." << std::endl;
    return 0;
}
