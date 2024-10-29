#include "Logger.h"
#include <chrono>
#include <ctime>
#include <iomanip>
#include <sstream>

Logger::Logger() {
    logFile.open("../logs/application.log", std::ios::out | std::ios::app);
    if (!logFile) {
        throw std::runtime_error("Unable to open log file.");
    }
}

Logger::~Logger() {
    if (logFile.is_open()) {
        logFile.close();
    }
}

Logger& Logger::getInstance() {
    static Logger instance;
    return instance;
}

void Logger::log(LogLevel level, const std::string& message) {
    std::lock_guard<std::mutex> lock(logMutex);
    std::string logEntry = formatLogMessage(level, message);
    writeLogEntry(logEntry);
}

std::string Logger::formatLogMessage(LogLevel level, const std::string& message) {
    auto now = std::chrono::system_clock::now();
    std::time_t now_c = std::chrono::system_clock::to_time_t(now);

    // Format log level
    std::string levelStr;
    switch (level) {
        case INFO: levelStr = "INFO"; break;
        case WARN: levelStr = "WARN"; break;
        case ERROR: levelStr = "ERROR"; break;
    }

    std::ostringstream oss;
    oss << std::put_time(std::localtime(&now_c), "%Y-%m-%d %X") << " [" << levelStr << "] " << message;
    return oss.str();
}

void Logger::writeLogEntry(const std::string& entry) {
    if (logFile.is_open()) {
        logFile << entry << std::endl;
    }
}
