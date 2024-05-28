# Basic Intrusion Detection System (IDS)

## Overview
This Python script implements a basic Intrusion Detection System (IDS) that monitors network traffic on a specified port to detect potentially malicious activities. The system logs connection attempts and flags any suspicious behavior based on the frequency of attempts from the same IP address within a short time frame.

## Features
- **Real-time Monitoring**: Listens for incoming TCP connections on a user-defined port.
- **Attack Detection**: Identifies potential attacks by monitoring the frequency of connections from the same IP address.
- **Logging**: Logs each connection attempt with its timestamp for further analysis.

## Requirements
- Python 3.x
- Access to a network interface that can accept connections (root privileges may be required for ports below 1024).

## Installation
No additional libraries are required beyond the Python Standard Library. To use the script, simply download the `basic_ids.py` file to your local machine.

## Usage
To run the script, execute the following command in your terminal:

## Bash
python basic_ids.py

## Configuring the Script

You can configure the following parameters directly in the script:

    host: IP address to bind the server to (default is '0.0.0.0' which listens on all interfaces).
    port: Port number to listen on (default is 5000).
    threshold: Number of allowed connections from the same IP within one minute before flagging as suspicious (default is 10).

## Example

ids = BasicIDS(host='0.0.0.0', port=5000, threshold=10)
ids.monitor_connections()

## Output

The script outputs connection logs directly to the console. If an IP address exceeds the threshold for connection attempts, a potential attack is flagged with a warning message.