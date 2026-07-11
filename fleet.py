from battery import average_battery, low_battery


class Fleet:

    def __init__(self):
        self.drones = []

    def add(self, drone):
        self.drones.append(drone)

    def report(self):

        print("=" * 45)
        print("DRONE FLEET REPORT")
        print("=" * 45)

        for drone in self.drones:
            print(drone)

        print("-" * 45)
        print(f"Fleet size: {len(self.drones)}")
        print(f"Average battery: {average_battery(self.drones)}%")

        warning = low_battery(self.drones)

        print(f"Low battery drones: {len(warning)}")
