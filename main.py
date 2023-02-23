import colorama
import base64
import pystyle
import time
import os

from colorama import *
from pystyle import *

print (Fore.RED + '1 - B64 Encoder')
print (Fore.BLUE + '2 - B64 Decoder')

b = Write.Input("Kodom File Ro Load Bedam? -> ", Colors.red_to_purple, interval=0.0025)
Write.Print(f"Successfully Selected {b} !", Colors.green_to_yellow, interval=0.05)

if b=='1' :
    print(' | Sabr Daram Load Midam...')
    time.sleep(1)
    os.system('cmd /k "python scripts/encoder.py"')

if b=='2' :
    print(' | Sabr Daram Load Midam...')
    time.sleep(1)
    os.system('cmd /k "python scripts/decoder.py"')
