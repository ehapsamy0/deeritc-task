#include "Logger.h"
#include <chrono>
#include <ctime>
#include <iomanip>
#include <sstream>
using namespace std;


Logger::Logger() {
    logFile.open("../logs/application.log", ios::out | ios::app);
    if (!logFile) {
        throw runtime_error("Unable to open log file.");
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

void Logger::log(LogLevel level, const string& message) {
    lock_guard<mutex> lock(logMutex);
    string logEntry = formatLogMessage(level, message);
    writeLogEntry(logEntry);
}

string Logger::formatLogMessage(LogLevel level, const string& message) {
    auto now = chrono::system_clock::now();
    time_t now_c = chrono::system_clock::to_time_t(now);

    // Format log level
    string levelStr;
    switch (level) {
        case INFO: levelStr = "INFO"; break;
        case WARN: levelStr = "WARN"; break;
        case ERROR: levelStr = "ERROR"; break;
    }

    ostringstream oss;
    oss << put_time(localtime(&now_c), "%Y-%m-%d %X") << " [" << levelStr << "] " << message;
    return oss.str();
}

void Logger::writeLogEntry(const string& entry) {
    if (logFile.is_open()) {
        logFile << entry << endl;
    }
}
