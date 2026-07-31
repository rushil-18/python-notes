import re 

text = "blah the blah instagram facebook reduce brain reels"

match = re.match('blah' , text , re.I)
match = re.match('I like to teach', text, re.I)
matches = re.findall('language', text, re.I)
matches = re.sub('%', '', text)
print(matches)



'''re.match(): searches only in the beginning of the
 first line of the string and returns matched objects if found, else returns None.
re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
re.findall: Returns a list containing all matches
re.split: Takes a string, splits it at the match points, returns a list
re.sub: Replaces one or many matches within a string'''