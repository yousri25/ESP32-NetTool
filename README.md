# ESP32 Wi-Fi Scanner & AP (MicroPython)

A minimal **ESP32 Wi-Fi tool** written in **MicroPython**.  
Scan nearby Wi-Fi networks or start an **Access Point**, selectable at runtime.

---

## Features

**Wi-Fi Scan**
- SSID, MAC, Channel, RSSI (dBm)
- Security type (OPEN, WEP, WPA/WPA2…)
- Hidden network flag
- Auto refresh every 2 seconds

**Access Point**
- Create ESP32 AP with custom SSID
- Open or WPA/WPA2-PSK
- Interactive stop prompt

---

## Example Output

WIFI: MyWiFi | MAC: aa:bb:cc:dd:ee:ff | Ch: 6 | RSSI: -55 | Sec: WPA2-PSK | Hidden: False  
------------------------------------------------------------

---

## Requirements

- ESP32 board
- MicroPython firmware
- Thonny IDE

---

## Usage

1. Run the script
2. Select mode:

1 = WiFi Scan | 2 = AP Mode


---

## AP Config

```python
ap.config(
    ssid="Usri-Esp32-AP",
    password="12345678",   # optional (8–63 chars)
    authmode=network.AUTH_WPA2_PSK
)
```

Notes

AP mode = local network only (no internet)

Great for learning ESP32 networking & Wi-Fi basics
