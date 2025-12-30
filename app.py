
import network

import time

# ================== AUTH MODE ==================

def value(x):
    AUTH_MODES = {
        0: "OPEN",
        1: "WEP",
        2: "WPA-PSK",
        3: "WPA2-PSK",
        4: "WPA/WPA2-PSK",
        5: "WPA2-ENTERPRISE"
    }
    return AUTH_MODES.get(x, "UNKNOWN")

# ================== WIFI SCAN ==================

def wifiscan():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    print("Scanning WiFi networks...")

    while True:
        nets = wlan.scan()

        for net in nets:
            ssid = net[0].decode("utf-8", "ignore") 
            bssid = ":".join("{:02x}".format(b) for b in net[1])
            channel = net[2]
            rssi = net[3]
            auth = net[4]
            hidden = net[5]

            print(
                "WIFI:", ssid,
                "| MAC:", bssid,
                "| Channel:", channel,
                "| Signal:", rssi, "dBm",
                "| Security:", value(auth),
                "| Hidden:", hidden
            )

        print("-" * 60)
        time.sleep(2)
        
    wlan.active(False)
    
# ================== AP MODE ==================

def apmode():
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(
        ssid="Usri-Esp32-AP", ## esm el wifi
        ## password ="12345678"   Must be 8<=passowrd<=63   ascii characters
        authmode=network.AUTH_OPEN ## AUTH_WPA2_PSK --- AUTH_WEP --- AUTH_WPA_PSK
    )

    print("Access Point started")
    print("SSID: Usri-Esp32-AP")
    q="n"
    while q =="n" :
        q=input("would you like to stop the ap mode : ")
        while q!="n" and q!= "y":
            q=input("error ! y or n are allowed")
    ap.active(False)

# ================== Programme Principale ==================


n = int(input("Select mode: 1 = WiFi Scan | 2 = AP Mode: "))

while n not in (1, 2):
    n = int(input("Error! Only 1 or 2 allowed: "))

if n == 1:
    wifiscan()
else:
    apmode()

