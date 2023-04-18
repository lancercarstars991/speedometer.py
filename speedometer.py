import time

def get_speed(distance, elapsed_time):
    """Calculate speed given distance and elapsed time."""
    return distance / elapsed_time

def display_speed(speed):
    """Display speed in a formatted string."""
    print(f"Current speed: {speed:.2f} meters per second")

def main():
    # Sample usage
    distance = 100  # meters
    start_time = time.time()
    time.sleep(2)  # simulate 2 seconds of travel time
    elapsed_time = time.time() - start_time
    speed = get_speed(distance, elapsed_time)
    display_speed(speed)

if __name__ == "__main__":
    main()
