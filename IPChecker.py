import requests
import ctypes

try:
    #Fetches User IP Address from ipify with a time out exception. Saves the IP address in the User_IP var.
    User_IP = requests.get("https://api64.ipify.org", timeout=5).text
except:
    # Displays a message box if the IP address cannot be obtained
    ctypes.windll.user32.MessageBoxW(0, "Unable to Fetch IP Address. Check Your Internet Connection and Try Again.", "Results", 16)
    User_IP = None  # Set to None to indicate failure
if User_IP:
    ctypes.windll.user32.MessageBoxW(0, f"Your IP address is: {User_IP}", "Public IP Address:", 1)
