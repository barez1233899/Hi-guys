#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from six.moves import input  # تەنها ئەم وەرگرتنە بەسە
import sys, os, time
from pathlib import Path
from scapy.all import *
from contextlib import contextmanager, redirect_stdout

# ===== ناوەکانی تایبەت بە تۆ =====
SCRIPT_NAME = "destroying"
AUTHOR_NAME = "ئەڵماس"
# ===============================

starttime = time.time()

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        with redirect_stdout(devnull):
            yield

class color:
    HEADER = "\033[95m"
    ENDC = "\033[0m"

keys = Path(f"./{SCRIPT_NAME.lower()}_api.key")

# لۆگۆی تەواوکراو:
logo = color.HEADER + f"""
  ____          _           _____ _           _     _ 
 / ___|___   __| | ___     / ____| |__   ___ | |   | |
| |   / _ \ / _` |/ _ \   | (___ | '_ \ / _ \| |   | |
| |__| (_) | (_| |  __/    \___ \| | | | (_) | |   | |
 \____\___/ \__,_|\___|    _____) |_| |_|\___/|_|___|_|
                                 {SCRIPT_NAME} v4.0
""" + color.ENDC + f"""
Author: {AUTHOR_NAME}
"""

DISCLAIMER = f"""
******************************************************* DISCLAIMER *******************************************************
{SCRIPT_NAME} is a research tool created by {AUTHOR_NAME} for educational purposes ONLY. 
This tool demonstrates vulnerabilities in misconfigured memcached servers. 
I am NOT responsible for any misuse or illegal activities.
******************************************************* {'*'*len(SCRIPT_NAME)} *******************************************************
"""

print(logo)
print(DISCLAIMER)

# پشکنین بۆ پاکەتی شۆدان
try:
    import shodan
except ImportError:
    print(f"[{AUTHOR_NAME}] Installing shodan...")
    os.system("pip install shodan")
    import shodan

# پشکنینی بوونی فایل و خوێندنەوە
if keys.exists():
    with open(keys, "r") as file:
        SHODAN_API_KEY = file.read().strip()  # read() بەکاربهێنە لەبری readline()
        print(f"[{AUTHOR_NAME}] Using API key from {keys}")
else:
    SHODAN_API_KEY = input(f"[{AUTHOR_NAME}] Please enter your Shodan API Key: ")
    with open(keys, "w") as file:
        file.write(SHODAN_API_KEY)
    print(f"[{AUTHOR_NAME}] API key saved to {keys}")

# پشکنینی API
try:
    api = shodan.Shodan(SHODAN_API_KEY)
    results = api.search("memcached", limit=1)
    print(f"[{AUTHOR_NAME}] Shodan API connected successfully")
    print(f"[{AUTHOR_NAME}] Total vulnerable servers: {results['total']}")
except Exception as e:
    print(f"[{AUTHOR_NAME}] API Error: {e}")
    sys.exit(1)

# ... (بەشی دیکەی کۆدەکە) ...