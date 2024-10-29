#include "Logger.h"
#include <iostream>
#include <thread>
#include <vector>
using namespace std;

void logMessages(const string& message, Logger::LogLevel level) {
    Logger& logger = Logger::getInstance();
    for (int i = 0; i < 10; ++i) {
        logger.log(level, message + " " + to_string(i));
    }
}

int main() {
    vector<thread> threads;
    
    threads.push_back(thread(logMessages, "Message from thread 1", Logger::INFO));
    threads.push_back(thread(logMessages, "Message from thread 2", Logger::WARN));
    threads.push_back(thread(logMessages, "Message from thread 3", Logger::ERROR));
    
    for (auto& t : threads) {
        t.join();
    }

    cout << "Logging completed. Check the logs/application.log file." << endl;
    return 0;
}
