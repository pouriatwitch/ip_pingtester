import subprocess
import platform
import time

def ping_ip(ip):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', ip]
    
    start_time = time.time()
    try:
        response = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        end_time = time.time()
        
        if response.returncode == 0:
            duration = round((end_time - start_time) * 1000)
            return duration
        return None
    except Exception:
        return None

def main():
    print("--- Network IP Scanner & Ping Tester ---")
    
    ip_list = [
        "1.1.1.1",
        "8.8.8.8",
        "9.9.9.9",
        "4.2.2.4",
    ]
    
    results = {}
    
    print("\nScanning IPs...")
    for ip in ip_list:
        print(f"Checking {ip}...", end="", flush=True)
        ping_time = ping_ip(ip)
        if ping_time:
            print(f" [Online: {ping_time}ms]")
            results[ip] = ping_time
        else:
            print(" [Timeout/Offline]")
            
    print("\n--- Results Summary ---")
    if results:
        sorted_results = sorted(results.items(), key=lambda x: x[1])
        for rank, (ip, ping) in enumerate(sorted_results, 1):
            print(f"{rank}. IP: {ip} | Ping: {ping}ms")
            
        print(f"\n Best IP to use: {sorted_results[0][0]} ({sorted_results[0][1]}ms)")
    else:
        print("No online IPs found.")

if __name__ == "__main__":
    main()
