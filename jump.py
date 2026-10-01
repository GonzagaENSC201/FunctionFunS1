def calculate_jump_distance(speed, airtime):
    """Computes the horizontal distance traveled during a jump.

    Args:
        speed(float): Horizontal speed in meters per second
        airtime(float): Time in the air in seconds

    Returns:
        float: Horizontal distance traveled in meters

    Notes:
        Pre-conditions:
            - speed >= 0
            - airtime >= 0
    """
    distance = speed * airtime
    return distance

def calculate_horizontal_speed(distance, airtime):
    """Calculates horizontal speed for a stunt given 
    known horizontal distance and airtime.

    Args:
        - distance(float): horizontal distance
        - airtime(float): known airtime

    Returns:
        - float: required horizontal speed

    Notes:
        - Pre-conditions:
            - distance >= 0
            - airtime > 0
    """
    return distance / airtime

# 7. practice
def get_user_speed_airtime():
    user_speed = float(input("Enter horizontal speed in m/s: "))
    user_airtime = float(input("Enter airtime in seconds: "))
    return user_speed, user_airtime

def main():
    # 7. practice
    user_speed, user_airtime = get_user_speed_airtime()
    jump_distance = calculate_jump_distance(user_speed, user_airtime)

    print(f"Speed: {user_speed} m/s")
    print(f"Airtime: {user_airtime} seconds")
    print(f"Jump distance: {jump_distance: .2f} meters")

    # TODO: call calculate_horizontal_speed() to test it

main()