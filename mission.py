def assign_mission(drone, mission):

    if drone.is_ready():
        drone.status = f"Mission: {mission}"
        return True

    return False
