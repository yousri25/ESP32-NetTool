import network
import time

def banner():
    print("""
                                                            
                                 .--,-``-.                  
    ,---,.                      /   /     '.       ,----,   
  ,'  .' |            ,-.----. / ../        ;    .'   .' \\  
,---.'   |            \\    /  \\\\ ``\\  .`-    ' ,----,'    | 
|   |   .'  .--.--.   |   :    |\\___\\/   \\   : |    :  .  ; 
:   :  |-, /  /    '  |   | .\\ :     \\   :   | ;    |.'  /  
:   |  ;/||  :  /`./  .   : |: |     /  /   /  `----'/  ;   
|   :   .'|  :  ;_    |   |  \\ :     \\  \\   \\    /  ;  /    
|   |  |-, \\  \\    `. |   : .  | ___ /   :   |  ;  /  /-,   
'   :  ;/|  `----.   \\:     |`-'/   /\\   /   : /  /  /.`|   
|   |    \\ /  /`--'  /:   : :  / ,,/  ',-    ./__;      :   
|   :   .''--'.     / |   | :  \\ ''\\        ;|   :    .'    
|   | ,'    `--'---'  `---'.|   \\   \\     .' ;   | .'       
`----'                  `---`    `--`-,,-'   `---'          
                                                            
""")

    print("""
 _    _ _  __ _   _____                                 
| |  | (_)/ _(_) /  ___|                                
| |  | |_| |_ _  \\ `--.  ___ __ _ _ __  _ __   ___ _ __ 
| |/\\| | |  _| |  `--. \\/ __/ _` | '_ \\| '_ \\ / _ \\ '__|
\\  /\\  / | | | | /\\__/ / (_| (_| | | | | | | |  __/ |   
 \\/  \\/|_|_| |_| \\____/ \\___\\__,_|_| |_|_| |_|\\___|_|   
                                                        
                                                        
""")




    print("""
______        __   __                   _ 
| ___ \\       \\ \\ / /                  (_)
| |_/ /_   _   \\ V /___  _   _ ___ _ __ _ 
| ___ \\ | | |   \\ // _ \\| | | / __| '__| |
| |_/ / |_| |   | | (_) | |_| \\__ \\ |  | |
\\____/ \\__, |   \\_/\\___/ \\__,_|___/_|  |_|
        __/ |                             
       |___/                              
""")





print("\033[2J\033[H")  # clear screen
banner()


wlan = network.WLAN(network.STA_IF)
wlan.active(True)

AUTH_MODES = {
    0: "OPEN",
    1: "WEP",
    2: "WPA-PSK",
    3: "WPA2-PSK",
    4: "WPA/WPA2-PSK",
    5: "WPA2-ENTERPRISE"
}

def value(x):
    return AUTH_MODES.get(x, "UNKNOWN")

while True:
    nets = wlan.scan()

    for net in nets:
        print("##########################")
        ssid = net[0].decode('utf-8', 'ignore')
        bssid = ':'.join('%02x' % b for b in net[1])
        channel = net[2]
        rssi = net[3]
        auth = net[4]
        hidden = net[5]

        print(
            "WIFI:", ssid,
            "| MAC:", bssid,
            "| Channel:", channel,
            "| Signal (dBm):", rssi,
            "| Security:", value(auth),
            "| Hidden:", hidden
        )

    print("-" * 50)
    time.sleep(2)

