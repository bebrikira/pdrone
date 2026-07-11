from fleet import Fleet
from sample_data import fleet_data
from mission import assign_mission

fleet = Fleet()

for drone in fleet_data:
    fleet.add(drone)

assign_mission(fleet.drones[0], "Bridge Inspection")
assign_mission(fleet.drones[3], "Field Survey")

fleet.report()
