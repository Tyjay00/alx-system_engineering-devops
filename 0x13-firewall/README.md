# Firewall Setup with UFW

This repository provides instructions for setting up a basic firewall using UFW (Uncomplicated Firewall) on a Linux system. UFW is a user-friendly interface for managing iptables, making it easier to configure a firewall.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Rules](#rules)
- [Verification](#verification)
- [Contributing](#contributing)
- [License](#license)

## Introduction

A firewall is a network security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules. UFW simplifies the process of configuring iptables rules and is commonly used for managing firewalls on Linux systems.

## Prerequisites

Before you begin, ensure that you have:

- A Linux system (e.g., Ubuntu, Debian) with sudo privileges.
- Access to the terminal.

## Installation

If UFW is not installed on your system, you can install it using the following command:

```bash
sudo apt-get update
sudo apt-get install ufw

1.Check UFW Status:
sudo ufw status

2.Enable UFW (if not active):
sudo ufw enable

3.Set Default Policies:
sudo ufw default deny incoming
sudo ufw default allow outgoing

4.Allow Specific Ports:
sudo ufw allow 22/tcp   # SSH
sudo ufw allow 443/tcp  # HTTPS
sudo ufw allow 80/tcp   # HTTP

5.Verify Rules:
sudo ufw show added

6.Enable UFW:
sudo ufw enable
