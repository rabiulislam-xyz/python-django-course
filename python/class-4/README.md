### string split and join

## conditional statement
- logical expression
```python
>>> (4 < 5) and (5 < 6)
>>> (4 < 5) and (9 < 6)
True
False
>>> (1 == 2) or (2 == 2)
True
>>> 
>>> 2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2
True
```
- condition with if
```python
name = 'Alice'
if name == 'Alice':
    print('Hi, Alice.')
```
- indentation
```python
name = 'Alice'
if name == 'Alice':
    print('Hi, Alice.')
print('Hi, Bob')
```
- else
```python
name = 'Bob'
if name == 'Alice':
    print('Hi, Alice.')
else:
    print('Hello, stranger.')
```
- elif
```python
name = 'Bob'
age = 5
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
    
name = 'Bob'
age = 30
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
else:
    print('You are neither Alice nor a little kid.')
```
- ordering
```python
name = 'Dracula'
age = 4000
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')
    
name = 'Dracula'
age = 4000
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 100:
    print('You are not Alice, grannie.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
```
- nested condition
```python
today = "holiday"
bank_balance = 25000
if today == "holiday":
   if bank_balance > 20000:
      print("Go for shopping")
   else:
      print("Watch TV")
else:
   print("normal working day")
```

## loops
- while loop
```python
spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1
```
- while input
```python
name = ''                 
while name != 'your name':
    print('Please type your name.')
    name = input()        
print('Thank you!')       
```
- break, continue
```python
while True:                  
    print('Please type your name.')
    name = input()           
    if name == 'your name':  
        break                
print('Thank you!')       


while True:
  print('Who are you?')
  name = input()
  if name != 'Joe':     
    continue            
  print('Hello, Joe. What is the password? (It is a fish.)') 
  password = input()    
  if password == 'swordfish':
    break               
print('Access granted.')


```

- range()
```python
list(range(10))
list(range(0,10))
list(range(0,10,1))
```
- for loop
```python
print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')
```
- sequence/itarable
```python
l = ['hello','world','how','are','you']
for item in l:
    print(l)
```

## bonus
```python
import random
random.random()
random.randint(1,10)
```
## task
-  Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
- What is the difference between break and continue?
