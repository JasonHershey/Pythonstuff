# Pythonstuff
Python scirpts and samples

## Scripts

### Passwordgenerator.py
This script generates a password from a pre-defined set of chaacters.

The character options are:
- Lower and upper case charactes from English alphabet
- Integers from 0-9
- Special characters that include !@#$%^&*()_[]|?>/<-=+~`,.

This script was inspired by a script from the book **THE BIG BOOK OF SMALL PYTHON PROJECTS** by Al Sweigart.  His script was called **Bagels** and was basically a game that involved generating a 3 digit number that uses would guess. This made me think of generating passwords... and several hours later, we have this script.

The basic logic is that, after choosing from the option to include numbers and/or special characters and the length of the password, the script generates the password using the following logic:
It shuffles the character set and chooses the first character from that set and adds it to the password -- repeating a number of times equal to the length of the password.
By doing it this way, it allows for characters to be used more than once (vs just randomizing the overall set of potential characters)

Code comments are in the file

