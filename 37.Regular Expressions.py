import re

patterns = ['term1', 'term2']
text = 'This is a string with term1, but not the other term'
for pattern in patterns:
    print('Searching for "%s" in: \n "%s"' % (pattern, text))
    # Check for match
    if re.search(pattern, text):
        print('\n')
        print('Match was found. \n')
    else:
        print('\n')
        print('No Match was found. \n')

match = re.search(patterns[0], text)
# print(type(match))
print(match.start())
print(match.end())

split_term = '@'
phrase = 'What is your email, is it hello@gmail.com'
k = re.split(split_term, phrase)
print(k)

j = 'hello world'.split()
print(j)

h = re.findall('match', 'Here is one match, here is another match')
print(h)

