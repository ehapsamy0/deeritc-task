# Logger Project

This project demonstrates a `Logger` class in C++ that handles concurrent logging from multiple threads or processes.

## Project Structure

- `src/Logger.h` - Header file for the `Logger` class.
- `src/Logger.cpp` - Implementation of the `Logger` class.
- `src/LoggerTest.cpp` - Test cases to demonstrate concurrent logging.
- `src/main.cpp` - Example usage of the `Logger`.
- `logs/application.log` - Log file (generated at runtime).
- `CMakeLists.txt` - CMake configuration.

## Building and Running

### Prerequisites

- Ensure you have CMake installed.

### Steps

1. **Create the Logs Directory**
   Ensure the `logs` directory exists where the log file will be saved:
   ```bash
   mkdir -p logs
   chmod +w logs
    ```


2. **Build the Project**
   ```bash
    mkdir build
    cd build
    cmake ..
    make
    ```
3. **Run the Example**

```bash
./LoggerProject
```

4. **Run the Tests**

```bash

./LoggerTest
```
5. **Check the Log File**

The log file will be created at logs/application.log.


### Explanation of the Design

1. **Singleton Pattern**: Ensures only one instance of `Logger` exists.
2. **Thread Safety**: Uses `std::mutex` to lock critical sections during log writes, preventing race conditions.
3. **Formatted Logging**: Includes timestamp and log levels for each entry.
4. **Test Cases**: `LoggerTest.cpp` demonstrates multithreaded usage of `Logger`.

This architecture provides a robust, thread-safe logging system suitable for use in concurrent C++ applications.
