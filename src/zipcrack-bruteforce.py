#! /usr/bin/python

import zipfile
import itertools
import time

# Function for extracting zip files to test if the password works!
def extractFile(zip_file, password):
    try:
        zip_file.extractall(pwd=password)
        return True
    except KeyboardInterrupt:
        exit(0)
    except Exception:
        pass

# Function to get the desired alphabet to use with bruteforce
def getAlphabet():
    lower_alphabet_include = input('Include lowercase letters(y/n)? ')
    if lower_alphabet_include.lower() == 'y':
        lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    else:
        lower_alphabet = ''
    upper_alphabet_include = input('Include uppercase letters(y/n)? ')
    if upper_alphabet_include.lower() == 'y':
        upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    else:
        upper_alphabet = ''
    digits_include = input('Include numbers(y/n)? ')
    if digits_include.lower() == 'y':
        digits = '0123456789'
    else:
        digits = ''
    symbols_include = input('Include symbols(y/n)? ')
    if symbols_include.lower() == 'y':
        symbols = '!@#$%^&*()-_=+`~\|]}[{;:/?.>,<'
    else:
        symbols = ''

    return(lower_alphabet + upper_alphabet + digits + symbols)


if __name__ == '__main__':
    # The file name of the zip file.
    zipfilename = input('Please enter the full name of the zip file: ')
    # The first part of the password.
    partial_password = input('Do you know the first part of the password(y/n)? ')
    if partial_password.lower() == 'y':
        first_half_password = input('Please enter first part of password: ')
    else:
        first_half_password = ''
    # Here we get the desired alphabet for the password
    alphabet = getAlphabet()
    zip_file = zipfile.ZipFile(zipfilename)

    # Setting the lower and upper bounds for the password lengths to check
    lower_bound = input("Please enter the password length minumum: ")
    upper_bound = input("Please enter the password length maximum: ")

    # Loops through the various different lengths for the passwords
    for i in range(int(lower_bound),int(upper_bound) + 1):
        # For every possible combination of i letters from alphabet...
        for c in itertools.product(alphabet, repeat=i):
            # Slowing it down on purpose to improve performance in web terminal.
            # Remove this line at your peril
            time.sleep(0.001)
            # Add the three letters to the first half of the password.
            password = first_half_password+''.join(c)
            # Try to extract the file.
            print("Trying: %s" % password)
            # If the file was extracted, you found the right password.
            if extractFile(zip_file, password):
                print('*') * 20
                print('Password found: %s' % password)
                print('Files extracted...')
                exit(0)

        # If no password was found by the end, let us know!
        print('Password not found.')
