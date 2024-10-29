#ifndef LOGGER_H
#define LOGGER_H

#include <fstream>
#include <mutex>
#include <string>

class Logger {
public:
    enum LogLevel { INFO, WARN, ERROR };

    static Logger& getInstance();

    Logger(const Logger&) = delete;
    Logger& operator=(const Logger&) = delete;

    void log(LogLevel level, const std::string& message);

private:
    Logger();
    ~Logger();

    void writeLogEntry(const std::string& entry);

    std::mutex logMutex;

    std::ofstream logFile;

    std::string formatLogMessage(LogLevel level, const std::string& message);
};

#endif
