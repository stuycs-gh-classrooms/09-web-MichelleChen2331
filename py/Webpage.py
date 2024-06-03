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
    'Words'.open()

html = HTML_HEADER
##html += file.readlines
html += '<br><a href="Webpage.html">Back</a>'
html += HTML_FOOTER
print(html)
print('Words')