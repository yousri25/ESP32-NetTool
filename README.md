# ESP32 Wi-Fi Scanner

A simple and lightweight Wi-Fi scanning tool for the **ESP32** using **MicroPython**. This script allows your ESP32 to detect nearby Wi-Fi networks, display their details, and continuously update the scan results in real-time.

---

## Features

- Scans for all nearby Wi-Fi networks.
- Displays detailed information for each network:
  - **SSID** (Network Name)
  - **MAC Address**
  - **Channel**
  - **Signal Strength (RSSI)**
  - **Security Type**
  - **Hidden/Visible Status**
- Colorful and visually appealing **ASCII banners** on startup.
- Runs continuously with automatic updates every 2 seconds.
- Easy-to-read output suitable for debugging and learning purposes.

---

## Example

```text
##########################
WIFI: MyHomeWiFi | MAC: aa:bb:cc:dd:ee:ff | Channel: 6 | Signal (dBm): -55 | Security: WPA2-PSK | Hidden: 0
##########################
WIFI: GuestNetwork | MAC: 11:22:33:44:55:66 | Channel: 11 | Signal (dBm): -72 | Security: OPEN | Hidden: 0
--------------------------------------------------


---

## Hardware Requirements

- ESP32 Development Board
- USB cable to connect ESP32 to your PC
- Optional: Breadboard and LEDs if extending the project

---

## Software Requirements

- [Thonny IDE](https://thonny.org/) or any other MicroPython-compatible IDE
- MicroPython firmware flashed on ESP32
- Python knowledge (basic) to run and modify the script

---

## Installation

1. **Flash MicroPython** onto your ESP32:
   - Download MicroPython firmware for ESP32 from [MicroPython Downloads](https://micropython.org/download/esp32/).
   - Use `esptool.py` to flash the firmware:
     ```bash
     esptool.py --port /dev/ttyUSB0 erase_flash
     esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 esp32-xxxx.bin
     ```

2. **Upload Script to ESP32**:
   - Connect your ESP32 to your PC.
   - Open Thonny IDE → Select **ESP32** as the interpreter.
   - Copy and paste the script (`main.py`) into Thonny and save it to your ESP32.

3. **Run the Script**:
   - Press **Run** in Thonny or reset your ESP32 to execute the script.
   - The Wi-Fi scanner will start automatically and display detected networks.

---

## Usage

1. Connect ESP32 to your PC.
2. Run the script.
3. Observe the list of nearby Wi-Fi networks.
4. Modify the script to add features like filtering by signal strength or saving results to a file.
