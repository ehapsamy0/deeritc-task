#ifndef LOGGER_H
#define LOGGER_H

#include <fstream>
#include <mutex>
#include <string>

class Logger {
public:
    // Logging levels
    enum LogLevel { INFO, WARN, ERROR };

    // Static method to get the singleton instance
    static Logger& getInstance();

    // Delete copy constructor and assignment operator to prevent duplicates
    Logger(const Logger&) = delete;
    Logger& operator=(const Logger&) = delete;

    // Log a message with specified log level
    void log(LogLevel level, const std::string& message);

private:
    // Private constructor and destructor
    Logger();
    ~Logger();

    // Method to write log entry to file
    void writeLogEntry(const std::string& entry);

    // Mutex for thread-safe logging
    std::mutex logMutex;

    // Log file stream
    std::ofstream logFile;

    // Format the log message
    std::string formatLogMessage(LogLevel level, const std::string& message);
};

#endif // LOGGER_H
