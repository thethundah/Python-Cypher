# Caesar Cipher Hacker
# http://inventwithpython.com/hacking (BSD Licensed)

message = 'GUVF VF ZL FRPERG ZRFFNTR.'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# loop through every possible key
for key in range(len(LETTERS)):

    # It is important to set translated to the blank string so that the
    # previous iteration's value for translated is cleared.
    translated = ''

    # The rest of the program is the same as the original Caesar program:

    # run the encryption/decryption code on each symbol in the message
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol) # get the number of the symbol
            num = num - key

            # handle the wrap-around if num is 26 or larger or less than 0
            if num < 0:
                num = num + len(LETTERS)

            # add number's symbol at the end of translated
            translated = translated + LETTERS[num]


            # Commented out. Print the symbol and the translated symbol matchign the
            # Rotation number
            #
            #
            #print (symbol)
            #print(translated)
            #
            #


        else:
            # just add the symbol without encrypting/decrypting
            translated = translated + symbol

    # display the current key being tested, along with its decryption
    #The argument for the print() function call is something we haven’t used before.
    # It is a string value that makes use of string formatting (also called string interpolation).
    # String formatting with the % s text is a way of placing one string inside another one.
    # The first % s text in the string gets replaced by the first value in the parentheses after the % at the end of the string.
    #Example -->

    #>> > 'The %s ate the %s that ate the %s.' % ('dog', 'cat', 'rat')
    #'The dog ate the cat that ate the rat.'
    #>> >
    print('Key #%s: %s' % (key, translated))