# Drone Fleet Manager

A lightweight Python application for managing a fleet of drones.

## Overview

Drone Fleet Manager is a console application that tracks drone status, battery levels, and mission assignments.

The project demonstrates object-oriented programming, modular design, and basic fleet management logic.

## Features

- Register drones
- Monitor battery levels
- Assign missions
- Fleet statistics
- Readiness check

## Project Structure

```
.
├── main.py
├── drone.py
├── fleet.py
├── battery.py
├── mission.py
├── sample_data.py
└── README.md
```

## Example Output

```
============= DRONE FLEET REPORT =============

DJI Mini 4 (92%) - Mission: Bridge Inspection
Autel EVO Lite (65%) - Idle
Parrot Anafi (18%) - Charging
DJI Air 3 (54%) - Mission: Field Survey
Skydio X2 (25%) - Maintenance

---------------------------------------------
Fleet size: 5
Average battery: 50.8%
Low battery drones: 2
```

## Technologies

- Python 3
- Git
- GitHub

## Future Improvements

- GPS coordinates
- Flight history
- Weather integration
- Mission scheduling
- JSON storage

