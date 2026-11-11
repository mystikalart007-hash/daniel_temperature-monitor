"""
Temperature Monitor and Alarm Checker
Reads 5 temperature readings from a machine, stores them in a list,
prints the highest, lowest and average, and warns if any reading
is above a safe limit.

My own twist: the user sets their own safe limit, and the program
also reports how many readings were over the limit and the status
of the machine (NORMAL, WARNING or DANGER).
"""


def get_number(message):
    """Keep asking until the user types a valid number, then return it as a float."""
    while True:  # loop repeats until we get a valid number
        text = input(message)
        try:
            return float(text)  # convert the text to a decimal number
        except ValueError:
            # runs if the user types a letter or symbol instead of a number
            print("Invalid input. Please type a number, for example 45.5")


def check_readings(readings, limit):
    """Print the highest, lowest, average and any alarm warnings."""
    highest = max(readings)
    lowest = min(readings)
    average = sum(readings) / len(readings)

    print("\n--- Results ---")
    print("Readings:", readings)
    print("Highest :", highest, "C")
    print("Lowest  :", lowest, "C")
    print("Average :", round(average, 2), "C")

    # Count and warn about readings above the safe limit
    over_limit = 0
    for reading in readings:
        if reading > limit:
            over_limit += 1
            print("WARNING: reading of", reading, "C is above the safe limit of", limit, "C")

    # Twist: decide the overall machine status using if/elif/else
    if over_limit == 0:
        status = "NORMAL - all readings are safe."
    elif over_limit < 3:
        status = "WARNING - some readings are above the safe limit."
    else:
        status = "DANGER - most readings are above the safe limit! Shut down the machine."

    print("Readings over limit:", over_limit, "out of", len(readings))
    print("Machine status:", status)


def main():
    """Run the program and let the user repeat it if they want."""
    print("=== Temperature Monitor and Alarm Checker ===")

    while True:
        limit = get_number("Enter the safe temperature limit in C: ")

        readings = []  # empty list to store the 5 readings
        for i in range(1, 6):  # loop 5 times
            value = get_number("Enter temperature reading " + str(i) + " in C: ")
            readings.append(value)  # add the reading to the list

        check_readings(readings, limit)

        again = input("\nCheck another set of readings? (yes/no): ").strip().lower()
        if again != "yes":
            print("Goodbye!")
            break  # leave the loop and end the program


main()56