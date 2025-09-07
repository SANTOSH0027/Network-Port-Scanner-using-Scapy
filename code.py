from scapy.all import *

# Step 1: Get user input
target_ip = input("Enter target IP: ")

ports=list(map(int,input("Give me port numbers").split()))
results = []

# Step 2: Perform port scan
for port in ports:
    packet = IP(dst=target_ip) / TCP(dport=port, flags="S")
    response = sr1(packet, timeout=1, verbose=0)

    if response:
        if  response[TCP].flags == "SA":
            status = "OPEN"
        elif response[TCP].flags == "RA":
            status = "CLOSED"
    else:
        status = "NO RESPONSE"

    results.append((port, status))

# Step 3: Save results to file
with open("scan_results.txt", "w") as f:
    for port, status in results:
        f.write(f"Port {port}: {status}\n")

print("\nScan complete. Results saved to scan_results.txt")
