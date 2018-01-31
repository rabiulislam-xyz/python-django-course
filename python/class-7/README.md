## task
-  Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
- What is the difference between break and continue?

## importing module
```python
import this
import random
from random import randint

import math
math.pi
from math import pi
pi
from math import *
pi
sqrt
from math import pi, sqrt
```
## exception handling
```python
try:
  1 / 0
except:
  print("You cannot divide by zero!")
  
try:
  1 / 0
except ZeroDivisionError:
  print("You cannot divide by zero!")

my_dict = {"a":1, "b":2, "c":3}
try:
  value = my_dict["d"]
except IndexError:
  print("This index does not exist!")
except KeyError:
  print("This key is not in the dictionary!")
except:
  print("Some other error occurred!")
```
## classes
```python
class Robot:
  name = 'wall-e'
```
## objects
```python
class Robot:
  name = 'wall-e'
 
robot1 = Robot()
robot2 = Robot()

robot1 is robot2
False

robot1.name
'wall-e'
robot2.name
'wall-e'
```
## method
```python
class Robot:
  name = 'wall-e'
  def say_hello(self):
    return 'HI, Hello!'
 
robot = Robot()
robot.name
'wall-e'
robot.say_hello()
'HI, Hello!'

class Robot:
  name = 'wall-e'
  def say(self, somthing):
    return str(somthing)
 
robot = Robot()
robot.name
'wall-e'
robot.say('bangladesh')
'bangladesh'
robot.say('dhaka')
'dhaka'
```
## __init__()
```python
class Robot:
  def __init__(self, name):
    self.name = name
 
robot1 = Robot('wall-e')
robot2 = Robot('eve')

robot1 is robot2
False

robot1.name
'wall-e'
robot2.name
'eve'
```
## class level variable and instance level variable
```python
class Robot:
  company = 'BNL'
  def __init__(self, name):
    self.name = name
 
robot1 = Robot('wall-e')
robot2 = Robot('eve')

robot1.company
'BNL'
robot1.name
'wall-e'

robot2.company
'BNL'
robot2.name
'eve'

robot1.company is robot2.company

Robot.company

Robot.name
```
