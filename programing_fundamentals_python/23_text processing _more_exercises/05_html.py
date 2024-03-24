title = input()
article = input()
comment = input()
list_of_comments = []

while comment != 'end of comments':
    list_of_comments .append(comment)
    comment = input()

print(f"""<h1>
    {title}
</h1>""")
print(f"""<article>
    {article}
</article>""")
for comment in list_of_comments:
    print(f"""<div>
    {comment}
</div>""")
