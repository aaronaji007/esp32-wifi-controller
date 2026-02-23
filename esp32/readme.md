# ESP32 Firmware Setup

This folder contains the firmware for the ESP32 controller.  
The ESP32 connects to a Wi-Fi network and sends control data to a Python server running on a computer.

---

## Configuration Required

Before uploading the firmware, update the network and server settings inside the code.

Open the main firmware file (`main.ino` or `.cpp`) and locate the configuration section.

Example:

```cpp
const char* WIFI_SSID = "YOUR_WIFI_NAME";
const char* WIFI_PASSWORD = "YOUR_WIFI_PASSWORD";

const char* SERVER_IP = "192.168.1.100";  // IP address of PC running server
const int SERVER_PORT = 4210;             // Must match Python server port
