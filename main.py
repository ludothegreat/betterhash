import subprocess
import os
from scapy.all import rdpcap
from scapy.layers.dot11 import Dot11Beacon, Dot11Elt

def extract_ssids_from_pcap(file_path):
    ssids = set()
    try:
        packets = rdpcap(file_path)
        for packet in packets:
            if packet.haslayer(Dot11Beacon):
                elt = packet[Dot11Elt]
                while elt:
                    if elt.ID == 0:  # SSID
                        ssid = elt.info.decode(errors="ignore")
                        if '\x00' not in ssid:  # Skip SSIDs with null bytes
                            ssids.add(ssid)
                    elt = elt.payload
    except Exception as e:
        print(f"Error reading pcap file: {e}")
    return ssids

def convert_pcap_to_hc2200(pcap_file, hc2200_file):
    command = f"hcxpcapngtool -o {hc2200_file} {pcap_file}"
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Converted {pcap_file} to {hc2200_file}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to convert pcap file: {e}")

def filter_hc2200_by_essid(hc2200_file, essid, output_file):
    command = f"hcxhashtool -i {hc2200_file} --essid={essid} -o {output_file}"
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Filtered {hc2200_file} for ESSID {essid} to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to filter hc2200 file for ESSID {essid}: {e}")

def main(pcap_file, output_directory):
    ssids = extract_ssids_from_pcap(pcap_file)
    print("Found SSIDs:", ssids)

    hc2200_file = os.path.join(output_directory, "combined.hc2200")
    convert_pcap_to_hc2200(pcap_file, hc2200_file)

    for ssid in ssids:
        output_file = os.path.join(output_directory, f"{ssid}.hc2200")
        filter_hc2200_by_essid(hc2200_file, ssid, output_file)

# Example usage
pcap_file_path = "/path/to/your/bettercap.pcap"  # Replace with your pcap file path
output_dir_path = "/path/to/output/directory"   # Replace with your desired output directory path
main(pcap_file_path, output_dir_path)
