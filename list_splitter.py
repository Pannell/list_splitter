import pyperclip, decimal

# Take list of items from the clipboard
rawinput = pyperclip.paste()

# Convert to an actual list, assuming each item is on it's own line
inputlist = rawinput.split('\n')

# Calculate the list size
listsize = len(inputlist)

# Initial starting point for list slice
start = 0

# Loop to check batch sizes are correct
switch = False
while switch == False:
    # Allow user to define how many batches the list should be split into
    print('How many batches would you like to split this list into?')
    batches = int(input())

    # Calculate size of batches
    floatbatch = listsize / batches
    roundbatch = decimal.Decimal(floatbatch).quantize(decimal.Decimal('0'), rounding=decimal.ROUND_UP)

    # Print list size
    print('Your list has ' + str(listsize) + ' items.')
    # Print batch sizes, if statement to account for 'remainder' batch
    if listsize % batches == 0:
        print('Split this into ' + str(batches) + ' batches of ' + str(int(listsize / batches)) + '. Proceed? (Y/N)')
        checkpoint = input()
        checkpoint.upper()
        if checkpoint == 'Y':
            break
        else:
            continue
    else:
        print('Split this into ' + str(batches) + ' batches. ' + str(batches - 1) + ' batches of ' + str(roundbatch) + ' and 1 batch of ' + str(listsize % batches) + '. Proceed?  (Y/N)'
        checkpoint = input()
        checkpoint.upper()
        if checkpoint == 'Y':
            break
        else:
            continue
    
# Loop to create batches
for i in range(1, (batches + 1)):
    # Dictate end point of slice
    stop = (roundbatch * i)
    # Use slice to create temporary batch
    batch = inputlist[int(start):int(stop)]
    # Convert list items back to string, separated by new lines
    converted = '\n'.join(batch)
    # Add batch to the clipboard
    pyperclip.copy(converted)
    # Notify user
    print('Batch ' + str(i) + ' is on the clipboard.')
    # Wait until user confirms they have pasted the batch from the clipboard
    print('Proceed? (Y/N)')
    command = input()
    command.upper()
    if command == 'Y':
        print('Completed Batch ' + str(i) + '.')
    # Begin the next slice where the last one ended
    start = stop

print('Process Complete.')
