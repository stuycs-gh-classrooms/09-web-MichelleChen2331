#!/usr/bin/python
print('Content-type: text/html\n')

import cgitb
cgitb.enable()

import cgi

HTML_HEADER = """
<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="utf-8">
<title>Practice</title>
</head>
"""

HTML_FOOTER = """
</body>
</html>
"""

data = cgi.FieldStorage()
file = "TestDoc.txt"
if ('Words' in data):
    file = data['Words'].value
    file.open()

html = HTML_HEADER
html += "<p>"
html += file.readlines()
html += "</p>"
html += '<br><a href="Webpage.html">Back</a>'
html += HTML_FOOTER
print(html)
