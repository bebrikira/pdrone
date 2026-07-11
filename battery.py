def average_battery(drones):

    if not drones:
        return 0

    total = sum(drone.battery for drone in drones)
    return round(total / len(drones), 1)


def low_battery(drones):

    return [drone for drone in drones if drone.battery < 30]
