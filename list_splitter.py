import pyperclip, decimal

# Take list of items from the clipboard
rawinput = pyperclip.paste()

# Convert to an actual list, assuming each item is on it's own line
inputlist = rawinput.split('\n')

# Calculate the list size
listsize = len(inputlist)

# Initial starting point for list slice
start = 0

# Allow user to define how many batches the list should be split into
print('How many batches would you like to split this list into?')
batches = int(input())

# Calculate size of batches
floatbatch = listsize / batches
roundbatch = decimal.Decimal(floatbatch).quantize(decimal.Decimal('0'), rounding=decimal.ROUND_UP)

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
    print('Proceed?')
    command = input()
    if command == 'y':
        print('Completed Batch ' + str(i) + '.')
    # Begin the next slice where the last one ended
    start = stop

print('Process Complete.')
