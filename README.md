# Temperature Monitor and Alarm Checker

## What it does
This Python program asks the user for a safe temperature limit and 5 temperature readings from a machine. It stores them in a list, then prints the highest, lowest and average reading. It warns the user about every reading above the safe limit.

## How to run it
Install Python 3, then run: python temperature_monitor.py

## Sample output
=== Temperature Monitor and Alarm Checker ===
Enter the safe temperature limit in C: 60
Enter temperature reading 1 in C: 45
Enter temperature reading 2 in C: 52.5
Enter temperature reading 3 in C: 70
Enter temperature reading 4 in C: abc
Invalid input. Please type a number, for example 45.5
Enter temperature reading 4 in C: 48
Enter temperature reading 5 in C: 65

--- Results ---
Readings: [45.0, 52.5, 70.0, 48.0, 65.0]
Highest : 70.0 C
Lowest  : 45.0 C
Average : 56.1 C
WARNING: reading of 70.0 C is above the safe limit of 60.0 C
WARNING: reading of 65.0 C is above the safe limit of 60.0 C
Readings over limit: 2 out of 5
Machine status: WARNING - some readings are above the safe limit.

## My own twist
The user sets their own safe limit. The program also counts how many readings are over the limit and gives an overall machine status: NORMAL, WARNING or DANGER. The user can also check several sets of readings without restarting.

## What I learned
I learned to check user input with try/except so the program does not crash when someone types a letter instead of a number. I also learned how to use functions to keep code organised.

## Author
Daniel Victory Chimemerie, ND1 Mechatronics Engineering, YabaTech.
