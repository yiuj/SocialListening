#pass string of arguments that will apply to string of text
#looking for 2-3 digit numbers
'''
Identifiers #looking for any number, etc.

#this is a character
\d = any number
\D = anything but a number
\s = space
\S = anything but a space
\w = any letter
\W = anything but a letter
. = any character, except for a new line
\b = space around whole words
\. = period. must use backslash, because . normally means any character.


Modifiers #this amount, this type, etc. A description
{1,3} = for digits, u expect 1-3 counts of digits, or "places"
        #looking for digits 1-3 in length
        example: \d{1,3}
+ = match 1 or more
? = match 0 or 1 repetitions.
    #might only want to find 1 instance
* = match 0 or MORE repetitions
$ = matches at the end of string
^ = matches start of a string
| = matches either/or. Example x|y = will match either x or y
    #looking for a digit 1-3 in length. or looking for a character 1-6 in length
    \d{1,3} | \w{1,6}

[] = range, or "variance"
    #looking for range capital A-Z with a-z as 2nd letter
    [A-Za-z]
    #looking for a number 1-5 with lowercase a-q with uppercase A-Z
    [1-5a-qA-Z]

{x} = expecting 'x' amount of the preceding code.
{x,y} = expect to see this x-y amounts of the precedng code


White Space Characters:
\n = new line
\s = space
\t = tab
\e = escape
\f = form feed
\r = carriage return

Characters used
. + * ? [ ] $ ^ ( ) { } | \

'''
import re
examplestring = '''Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97 years old, and his grandfather, Oscar, is 102'''

#specify regular expressions corresponding to names
    #looking for any capital letter first. [A-Z] anything capital A-Z
    #looking for anything lowercase a-z
    # * looking for only 1 [A-Z] and as many of [a-z]
names = re.findall(r'[A-Z][a-z]*', examplestring)
#specify regular expressions corresponding to age
    #nofify this is a regular expression: r'
    #looking for any digit with 1-3 digits
    # ,search for in examplestring
ages = re.findall(r'\d{1,3}', examplestring)
print(names)
print(ages)
#stick names and ages in a dictionary
ageDict={}
x=0
for eachName in names:
    ageDict[eachName] = ages[x]
    x+=1
print(ageDict)
