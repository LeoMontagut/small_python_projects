import random, sys, time

PAUSE = 0.15

# Individual rows of the DNA animation
ROWS = [
    #123456789 <- Use this to measure the number of spaces:
    '         ##',  # Index 0 has no {}.
    '        #{}-{}#',
    '       #{}---{}#',
    '      #{}-----{}#',
    '     #{}------{}#',
    '    #{}------{}#',
    '    #{}-----{}#',
    '     #{}---{}#',
    '     #{}-{}#',
    '      ##',  # Index 9 has no {}.
    '     #{}-{}#',
    '     #{}---{}#',
    '    #{}-----{}#',
    '    #{}------{}#',
    '     #{}------{}#',
    '      #{}-----{}#',
    '       #{}---{}#',
    '        #{}-{}#']
    #123456789 <- Use this to measure the number of spaces:

try:
    print('DNA animation')
    print('Press Ctrl-C to quit...')
    time.sleep(2)
    row_index = 0

    while True:
        # Increment row_index to draw next row
        row_index = row_index + 1
        if row_index == len(ROWS):
            row_index = 0

        if row_index == 0 or row_index == 9:
            print(ROWS[row_index])
            continue

        # Select random nucleotide pairs G-C and A-T
        random_selection = random.randint(1, 4)
        if random_selection == 1:
            left_nucleotide, right_nucleotide = 'A', 'T'
        elif random_selection == 2:
            left_nucleotide, right_nucleotide = 'T', 'A'
        elif random_selection == 3:
            left_nucleotide, right_nucleotide = 'C', 'G'
        elif random_selection == 4:
            left_nucleotide, right_nucleotide = 'G', 'C'

        # Print the row
        print(ROWS[row_index].format(left_nucleotide, right_nucleotide))
        time.sleep(PAUSE)

except KeyboardInterrupt:
    sys.exit()