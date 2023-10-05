# Networking Basics 2.0

This project is part two of the series introducing networking concepts. In this project, we explore the OSI model, types of networks, MAC and IP addresses, and TCP/UDP protocols. Additionally, there are practical scripts to inspect listening ports and check if a host is on the network.

## Tasks 

### 0. OSI Model
    A text file answering questions about the OSI model.
  - What is the OSI model?
    1. Set of specifications that network hardware manufacturers must respect
    2. The OSI model is a conceptual model that characterizes the communication functions of a telecommunication system without regard to their underlying internal structure and technology.
    3. The OSI model is a model that characterizes the communication functions of a telecommunication system with a strong regard for their underlying internal structure and technology.
  - How is the OSI model organized?
    1. Alphabetically
    2. From the lowest to the highest level
    3. Randomly

### 1. Types of Network
    A text file answering questions about types of networks.
  - What type of network is a computer in a local connected to?
    1. Internet
    2. WAN
    3. LAN
  - What type of network could connect an office in one building to another office in a building a few streets away?
    1. Internet
    2. WAN
    3. LAN
  - What network do you use when you browse www.google.com from your smartphone (not connected to the WiFi)?
    1. Internet
    2. WAN
    3. LAN

### 2. MAC and IP Address
    A text file answering questions about MAC and IP addresses.
  - What is a MAC address?
    1. The name of a network interface
    2. The unique identifier of a network interface
    3. A network interface
  - What is an IP address?
    1. Is to devices connected to a network what postal address is to houses
    2. The unique identifier of a network interface
    3. Is a number that network devices use to connect to networks

### 3. UDP and TCP
    A text file answering questions about UDP and TCP protocols.
  - Which statement is correct for the TCP box:
    1. It is a protocol that is transferring data in a slow way but surely
    2. It is a protocol that is transferring data in a fast way and might lose data along in the process
  - Which statement is correct for the UDP box:
    1. It is a protocol that is transferring data in a slow way but surely
    2. It is a protocol that is transferring data in a fast way and might lose data along in the process
  - Which statement is correct for the TCP worker:
    1. Have you received boxes x, y, z?
    2. May I increase the rate at which I am sending you boxes?

### 4. TCP and UDP Ports
    A Bash script that displays listening ports.
  - Displays only listening sockets.
  - Shows the PID and name of the program to which each socket belongs.

### 5. Is the Host on the Network
    A Bash script that pings an IP address received as an argument 5 times.
  - Usage: `5-is_the_host_on_the_network {IP_ADDRESS}`.
