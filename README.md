# Python Scripting for DevOps

This repository contains my hands-on Python learning journey focused on
Linux administration, DevOps automation, scripting, APIs, SSH/SFTP,
monitoring and infrastructure automation.

## Day 1 - Python Fundamentals

Topics covered:

- Python basics
- print()
- Variables
- Data types
- type()
- Type conversion
- input()
- f-strings
- Basic arithmetic operations
- Formatted output

## Project 1 - Server Inventory

`server_inventory.py` is an interactive Python script that collects
basic server information from the user.

### Information collected

- Hostname
- OS Distribution
- Server Role
- CPU Cores
- Memory
- Environment

The script also calculates a sample server upgrade:

- Upgraded CPU Cores
- Upgraded Memory

### Example

```text
========================
Server Inventory
========================
Hostname is:  app01
OS Distro is: rhel
Role is:  App
No. of CPU is:  8
Memory is: 12 GB
Environment is: prod
Upgraded CPU Core is: 12
Upgraded memory is: 20 GB
========================
