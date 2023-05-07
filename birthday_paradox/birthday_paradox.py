"""Birthday Paradox Simulation"""

import datetime, random


def GetBirthdays(NumberOfBirthdays):
    """Returns a list of number random date objects for birthdays"""
    birthdays = []
    for i in range(NumberOfBirthdays):
        # The year is unimportant for the simulation as long as
        # all birthdays have the same year
        start_of_year = datetime.date(2001, 1, 1)

        # Get a random day into the year
        random_number_of_days = datetime.timedelta(random.randint(0, 364))
        birthday = start_of_year + random_number_of_days
        birthdays.append(birthday)
    return birthdays

def GetMatch(birthdays):
    """Returns the date object of a birthday that occurs more than once
    in the birthday list"""
    if len(birthdays) == len(set(birthdays)):
        return None # All birthdays are unique, so return None.

    # Compare each birthday to every other birthday
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA # Return the matching birthday

# Display the intro
print("""Birthday Paradox


The birthday paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.

(It's not actually a paradox, it's just a surprising result.)
""")

# Set up a tuple of month names in order:
MONTHS = (
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
)

while True: # Keep asking until the user enters a valid amount
    print('How many birthdays shall i generate? (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break # User has entered a valid amount
print()

# Generate and display the birthdays
print(f'Here are {numBDays} birthdays:')
birthdays = GetBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Display a comma for each birthday after the first birthday
        print(', ', end='')
        MonthName = MONTHS[birthday.month - 1]
        DateText = f'{MonthName} {birthday.day}'
        print(DateText, end='')
print()
print()

# Determine if there are two birthdays that match
match = GetMatch(birthdays)

# Display the results
print('In this simulation, ', end='')
if match != None:
    MonthName = MONTHS[match.month - 1]
    DateText = f'{MonthName} {match.day}'
    print(f'multiple people have birthday on {DateText}')
else:
    print('there are no matching birthdays')
print()

# Run through 100,000 simulations
print(f'Generating {numBDays} random birthdays 100,000 times...')
print('Press Enter to begin...')

print("Let's run another 100,000 simulations")
SimMatch = 0 # How many simulations had matching birthdays in them
for i in range(100000):
    # Report the progress every 10,000 simulations:
    if i % 10000 == 0:
        print(f'{i} simulations run...')
    birthdays = GetBirthdays(numBDays)
    if GetMatch(birthdays) != None:
        SimMatch = SimMatch + 1
print('100,000 simulations run')

# Display simulations results
probability = round(SimMatch / 100000 * 100, 2)
print(f'Out of 100,000 simulations of {numBDays} people there was a')
print(f'matching birthday in that group {SimMatch} times. This means')
print(f'that {numBDays} people have a {probability}% chance of')
print('having a matching birthday in their group.')
print("That's probably more than you would think!")