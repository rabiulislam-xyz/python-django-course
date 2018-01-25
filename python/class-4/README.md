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

```
- break, continue
```python

```
- for loop
```python

```
- sequence/itarable
```python

```
- range()
```python

```

## task
-  Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

