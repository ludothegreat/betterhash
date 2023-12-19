# Pcap to HC2200 Converter

I couldn't find a way to get Bettercap to create indavidual pcap files for each hash. This Python script automates the process of extracting ESSIDs from a .pcap file and creating individual .hc2200 files for each ESSID.
## Overview

The script performs the following steps:
1. Extracts all ESSIDs from the provided pcap file.
2. Converts the pcap file to a single .hc2200 file using `hcxpcapngtool`.
3. Filters the .hc2200 file for each extracted ESSID using `hcxhashtool`, creating a separate .hc2200 file for each ESSID.

## Prerequisites

- Python 3.x
- `scapy` Python library
- `hcxpcapngtool`
- `hcxhashtool`

Ensure that `hcxpcapngtool` and `hcxhashtool` are installed and accessible from your command line.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ludothegreat/betterhash.git
   ```
2. Navigate to the cloned repository:
   ```bash
   cd betterhash
   ```
3. Install `scapy`:
   ```bash
   pip install scapy
   ```

## Usage

1. Place your pcap file in a known directory.
2. Run the script with the path to your pcap file and the desired output directory:
   ```bash
   python main.py
   ```

Replace `/path/to/your/bettercap.pcap` and `/path/to/output/directory` in the script with the actual paths to your pcap file and the desired output directory.

After running the script, you will find individual .hc2200 files for each ESSID in the specified output directory.
