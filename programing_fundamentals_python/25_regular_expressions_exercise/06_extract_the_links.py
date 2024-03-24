import re

sentence = input()
pattern = r'(w{3}\.[A-Za-z0-9\-\.]+\.[a-z]+)'
while sentence:
    match = re.search(pattern, sentence)
    if match:
        valid_url = match.group(1)
        print(valid_url)
    sentence = input()
