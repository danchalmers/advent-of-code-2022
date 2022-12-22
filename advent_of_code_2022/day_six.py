def day_six():
    with open("data/input/day_six.txt", "r") as f:
        signal = f.readline()
    position = start_position_in_signal(signal, 4)
    print(f"day six part one: {position}")
    position = start_position_in_signal(signal, 14)
    print(f"day six part two: {position}")

def start_position_in_signal(signal: str, group_of: int) -> int:
    for position in range(group_of-1, len(signal)):
        if len(set(signal[position-group_of:position])) == group_of:
            return position
