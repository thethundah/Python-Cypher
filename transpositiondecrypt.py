# Transposition Cipher Decryption
# https://inventwithpython.com/hacking (BSD Licensed)

import math, pyperclip

def main():
    myMessage = 'Cenoonommstmme oo snnio. s s c'
    myKey = 8

    plaintext = decryptMessage(myKey, myMessage)

    # Print with a | ("pipe" character) after it in case
    # there are spaces at the end of the decrypted message.
    print(plaintext + '|')

    pyperclip.copy(plaintext)


def decryptMessage(key, message):
    # The transposition decrypt function will simulate the "columns" and
    # "rows" of the grid that the plaintext is written on by using a list
    # of strings. First, we need to calculate a few values.


    # this will take the full length of our message , in our case 20 , and divide it
    # with the key value. This will give us the total index for our list.
    # we then have to have , in this case , divide 20 by 6(key) and round us that number


    # The number of "columns" in our transposition grid:
    # math.ceil will round UP
    # math.floor will rounf DOWN
    numOfColumns = int(math.ceil(len(message) / key))

    # 1 row ["1" "2" "3" "4" "5" "6"]

    # we need the exact number of row to be the same as the key
    # The number of "rows" in our grid will need:
    numOfRows = key

    # 1 row ["1" "2" "3" "4" "5" "6"]
    # 2 row ["1" "2" "3" "4" "5" "6"]
    # 3 row ["1" "2" "3" "4" "5" "6"]
    # 4 row ["1" "2" "3" "4" "5" "6"]
    # 5 row ["1" "2" "3" "4" "5" "6"]
    # 6 row ["1" "2" "3" "4" "5" "6"]


    # The number of "shaded boxes" in the last "column" of the grid:
    # we have to multiply the number of rows with the number of columns and then
    # subtact that to the total length of the message to obtain de number of
    # grayed-out boxes that we do not need.
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    # 1 row ["1" "2" "3" "4" "5" "6"]
    # 2 row ["1" "2" "3" "4" "5" "6"]
    # 3 row ["1" "2" "3" "4" "5" "6"]
    # 4 row ["1" "2" "3" "4" "5" "6"]
    # 5 row ["1" "2" "3" "4" "5" "6"]
    # 6 row ["1" "2" "3" "4" "GRAYED-OUT" "GRAYED-OUT"]


    # Each string in plaintext represents a column in the grid.
    plaintext = [''] * numOfColumns

    # The column and row variables point to where in the grid the next
    # character in the encrypted message will go.
    column = 0
    row = 0

    # This for loop will go through each character in the message and assign it
    # the variable of symbol
    for symbol in message:

        # Here we will put the symbol into the  first column to start decrypting
        plaintext[column] += symbol
        column += 1 # Point to next column.


        # Once we have reached the end of the lenght of our decryption list , we will start a new
        # row , until we reach the end of the columns of that row

        # If there are no more columns OR we're at a shaded box, go back to
        # the first column and the next row:
        if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1

    return ''.join(plaintext)


# If transpositionDecrypt.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()