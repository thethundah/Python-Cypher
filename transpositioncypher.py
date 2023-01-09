# Transposition Cipher Encryption
# http://inventwithpython.com/hacking (BSD Licensed)

import pyperclip

def main():
    myMessage = 'Common sense is not so common.'

    myKey = 8

    ciphertext = encryptMessage(myKey, myMessage)

    # Print the encrypted string in ciphertext to the screen, with
    # a | (called "pipe" character) after it in case there are spaces at
    # the end of the encrypted message.
    print(ciphertext + '|')

    # Copy the encrypted string in ciphertext to the clipboard.
    pyperclip.copy(ciphertext)


def encryptMessage(key, message):
    # Each string in ciphertext represents a column in the grid.
    # Creates a list of the lenght of the key
    ciphertext = [''] * key

    # Loop through each column in ciphertext.
    for col in range(key):
        #create a pointer to locate the column we are at for the message
        pointer = col

        # Keep looping until pointer goes past the length of the message.
        # while we haven't gone through the whole message , keep looping
        while pointer < len(message):

            # Place the character at the pointer's position in the message at the end of the
            # current column in the ciphertext list.
            # Spaces also count when counting with pointer

            #Example :
            # message	["Common sense is not so common."]
            # ciphertext	[""]
            # col	[0]
            # pointer	[0]
            #
            #>>> add "C" to cyphertext and add 8 to the pointer since key is "8"
            #
            # message	["Common sense is not so common."]
            # ciphertext	["C"]
            # col	[0]
            # pointer	[8]
            #>>> add "e" to cyphertext and add 8 to the pointer since key is "8"
            # message	["Common sense is not so common."]
            # ciphertext	["Ce"]
            # col	[0]
            # pointer	[16]
            #...



            #
            # This add's letter that the pointer is pointing to in the message to our first column in the list created called
            # ciphertext which is of the lenght of our key. In our case , this would be lenght of 8 , from 0 to 7
            ciphertext[col] += message[pointer]

            # move to the next pointer , in regard's to the key used
            # in our case , we add 8 to our pointer for it to point us to the next letter , when we add 8 , which is
            # our key value , from the beginning of the pointer position
            # message	["Common sense is not so common."]

            #Example:
            # 0 1 2 3 4 5 6 7
            # C o m m o n   s
            # e n s e   i s
            # n o t   s o   c
            # o m m o n .    |

            # Start at column 0 , position 0 , and count to 8. you will get to e if you start with "C".
            # You go through each letter , counting from the last position you ended on.
            # Next you start with the column 1 , position 0. You start with the letter "o" and then you count
            # to 8 . You should end up at the letter "n". And you keep doing that until youve gone trough all the columns.

            # Dont forget that spaces also count

            pointer += key

    # Convert the ciphertext list into a single string value and return it.

    return ''.join(ciphertext)


# If transpositionEncrypt.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()