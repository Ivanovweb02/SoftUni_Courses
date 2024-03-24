data = input()
submissions = {}
result = {}
while data != 'exam finished':
    if 'banned' in data:
        data = data.split("-")
        username = data[0]
        if username in result.keys():
            result.pop(username)

    else:
        username, language, points = data.split("-")
        if language not in submissions.keys():
            submissions[language] = 0
        submissions[language] += 1
        if username not in result.keys():
            result[username] = []
        result[username].append(int(points))
    data = input()

print("Results:")
for (username, points) in result.items():
    max_point = max(points)
    print(f"{username} | {max_point}")
print("Submissions:")
for (language, count) in submissions.items():
    print(f"{language} - {count}")
