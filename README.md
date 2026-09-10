# Python Scripting for DevOps

This repository contains my hands-on Python learning journey focused on Linux, DevOps, automation, scripting, APIs, SSH/SFTP, Flask and cloud automation.

## Learning Goal

- Learn Python from zero to advanced DevOps automation
- Write Python scripts independently without relying on autocomplete
- Build 50+ practical DevOps scripts
- Automate Linux administration and operational tasks
- Work with APIs, SSH, SFTP and cloud platforms
- Build practical Flask dashboards
- Prepare Python skills for DevOps/SRE interviews

---

# Day 1 - Python Fundamentals

Topics covered:

- Python environment setup
- Virtual environment
- Python interpreter and REPL
- `print()`
- Variables
- Strings
- Integers
- Floats
- Boolean
- `type()`
- Type conversion
- `input()`
- `int()`, `float()`, `str()`
- f-strings
- Comments
- Basic calculations

### Practical

- Server information input
- Server inventory script
- CPU and memory upgrade calculation

### Project

`server_inventory.py`

---

# Day 2 - Conditions and Decision Making

Topics covered:

- Comparison operators
- `=`
- `==`
- `>`
- `<`
- `>=`
- `<=`
- `!=`
- `if`
- `if-else`
- `if-elif-else`
- Logical operators
- `and`
- `or`
- `not`
- Nested `if`
- Boolean handling with user input
- Threshold checking
- Resource alerts

### Practical

- CPU classification
- Memory/resource checking
- Service status checking
- Critical resource alerts
- Nested server health checks

### Project

`server_health.py`

---

# Day 3 - Loops and Automation Logic

Topics covered:

- `while` loop
- `for` loop
- `range()`
- Start/stop/step
- Reverse loops
- Loop with conditions
- `break`
- `continue`
- Nested loops
- User input with loops
- Nested loop conditions
- Per-server validation

### Practical

- Server checks
- CPU checks
- Memory checks
- Service checks
- Skip checks using `continue`
- Stop checks using `break`
- Resource scanning
- Multiple server monitoring

### Project

`server_monitor.py`

---

# Day 4 - Lists and Tuples

Topics covered:

## Lists

- Creating lists
- List indexing
- Negative indexing
- Modifying list elements
- `append()`
- `insert()`
- `remove()`
- `pop()`
- `len()`
- `in` operator
- List iteration
- List filtering
- `min()`
- `max()`
- `sum()`
- Average calculation
- List slicing
- Nested lists
- Dynamic list input

## Tuples

- Creating tuples
- Tuple indexing
- Tuple iteration
- Tuple immutability
- Difference between lists and tuples
- List of tuples
- Tuple-based server records

### Practical

Created dynamic server inventory using a list containing tuple records.

Example:

```python
servers = [
    ("app01", 95, 65),
    ("app02", 54, 43)
]
