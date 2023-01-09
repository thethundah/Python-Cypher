# Transposition Cipher Encrypt/Decrypt File
# http://inventwithpython.com/hacking (BSD Licensed)

import time, os, sys, transpositioncypher, transpositiondecrypt

def main():
        inputFilename = 'frankenstein.txt'
        # BE CAREFUL! If a file with the outputFilename name already exists,
        # this program will overwrite that file.
        outputFilename = 'frankenstein.encrypted.txt'
        myKey = 10
        myMode = 'encrypt' # set to 'encrypt' or 'decrypt'

        # If the input file does not exist, then the program terminates early.
        if not os.path.exists(inputFilename):
            print('The file %s does not exist. Quitting...' % (inputFilename))
            sys.exit()

        # If the output file already exists, give the user a chance to quit.
        if os.path.exists (outputFilename):
            print ('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFilename))
            response = input ('> ')


            # The startswith() method will return True if its string argument can be found at the beginning of the string
            #If the user did not type in 'c', 'continue', 'C', or another string that begins with C,
            # then sys.exit() will be called to end the program.

            # Technically, the user doesn’t have to enter “Q” to quit; any string that does not begin with “C”
            # will cause the sys.exit() function to be called to quit the program.

            # The response.lower() only set the user input into lowercase letters
            if not response.lower ().startswith ('c'):
                sys.exit ()



        # Read in the message from the input file
        fileObj = open(inputFilename)
        # fileObj.read will read the whole content of the file
        content = fileObj.read()
        fileObj.close()

        print('%sing...' % (myMode.title()))

        # Measure how long the encryption/decryption takes.
        startTime = time.time()


        if myMode == 'encrypt':
            translated = transpositioncypher.encryptMessage(myKey, content)
        elif myMode == 'decrypt':
            translated = transpositiondecrypt.decryptMessage(myKey, content)
        totalTime = round(time.time() - startTime, 2)
        print('%sion time: %s seconds' % (myMode.title(), totalTime))

        # Write out the translated message to the output file.
        outputFileObj = open(outputFilename, 'w')
        outputFileObj.write(translated)
        outputFileObj.close()

        print('Done %sing %s (%s characters).' % (myMode, inputFilename, len(content)))
        print('%sed file is %s.' % (myMode.title(), outputFilename))

        # If transpositionCipherFile.py is run (instead of imported as a module)
        # call the main() function.
if __name__ == '__main__':
    main()