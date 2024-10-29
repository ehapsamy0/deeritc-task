#ifndef LOGGER_H
#define LOGGER_H

#include <fstream>
#include <mutex>
#include <string>
using namespace std;


class Logger {
public:
    enum LogLevel { INFO, WARN, ERROR };

    static Logger& getInstance();

    Logger(const Logger&) = delete;
    Logger& operator=(const Logger&) = delete;

    void log(LogLevel level, const string& message);

private:
    Logger();
    ~Logger();

    void writeLogEntry(const string& entry);

    mutex logMutex;

    ofstream logFile;

    string formatLogMessage(LogLevel level, const string& message);
};

#endif
