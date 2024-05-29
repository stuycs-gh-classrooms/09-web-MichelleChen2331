#!/usr/bin/python
print('Content-type: text/html\n')

from random import random
r = random()
stuff = """<!DOCTYPE html>

<html lang="en">

  <head>
    <meta charset="utf-8">
    <title>Lottery Number</title>
  </head>

  <body>
    <p>
      Reload to generate a random number
    </p>
  </body>

</html>"""
print('Some random number:', stuff, r)
