while True:
    sentences = ""
    current_string = input()
    if current_string == "End":
        break
    if current_string == "SoftUni":
        continue
    for character in current_string:
        sentences += character * 2
    print(sentences)
