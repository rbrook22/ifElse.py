#Creating my first if else statements
name= "Rick"

if name == 'Ricky':
    print("Hello Ricky!")
else: 
    print("Hello Stranger!")

value= input('What is your name?')
if value == 'Rick':
    print("Hello Rick!")
elif value == 'Debbie':
    print("Hello Debbie!")
elif value == 'Kendall':
    print('Hello Kendall!')
else:
    print("I'm sorry we don't recognize you %s" %value)

