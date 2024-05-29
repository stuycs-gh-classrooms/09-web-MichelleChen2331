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
      <img src="py/lottery.png" alt="Lottery Logo">
      <li>
    <ul>
      Reload to generate the lottery number
      </ul>
      </li>
    </p>
  </body>

</html>"""
print(stuff, 'Some random lotto number:', r)
