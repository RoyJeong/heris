#!python
print("content-type: text/html")
print()
import cgi, os
files = os.listdir('data')
listStr = ''
for item in files:
    listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data'+pageID,'r').read()
    update_link='<a href="update.py?id={}">Update</a>'.format(pageId)
else:
    pageId = 'welcome'
    description = 'Hello, web'
print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    {listStr}
  </ol>
  <a href = "create.py">Create</a>
  <h2>{title}</h2>
  <p>{desc}</p>
</body>
</html>
'''.format(title=pageId, desc=description, listStr=listStr))
