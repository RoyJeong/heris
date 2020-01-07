#!python


import cgi
form = cgi.FieldStorage()
title = form["title"].value
description = form["description"].value

opend_file = open('data/'+title, 'w')
opend_file.write(description)

#Redirection
print("location: index.py?id="+title)
print()
