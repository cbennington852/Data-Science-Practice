print("Cr battery")

base_salary = 10000
bonus_salary = .10
total_salary = base_salary * (1 + bonus_salary)

print(total_salary)

print(print)

print(type(bonus_salary))

#shows a basic function
def greet():
    return "COCK"


#demonstrates a class in python
class jobPost:
    def __init__(self, title, location, salary):
        self.title = title
        self.location = location
        self.salary = salary
        
    def print_salary(self):
        print(f"total salary: {self.title}")
        return

#creating and calling a class
job_1 = jobPost("Car", "Seattle", 1000)
print(job_1.title)
print(job_1.salary)
job_1.print_salary()

#we have built in functions for the strings
myStr = 'car'
myStr = myStr.capitalize()
print(myStr)

#we can declare the varible type if nessicary 
floot = float(999)
print(floot)

#help is great
#print(help(str))
title = 'Data Anal'
title = title.replace('a','o', 2) #thing to be repalced, replacment, how many replace
print('Title: '+ title)

title = title.split(' ', 1)
print(title)

#use of fStrings
role = 'Cyber Defender'
skill = 'Python'
print(f'Role: {role}; Skill: {skill}')

#formatting
myStr = '0123456789'
myStr = ', '.join(myStr)
print(myStr)

##############################################################
#wow a if statement
##############################################################
if True:
    print('IS TRUE!')
elif False:
    print('IS false!')
    
apple = 'apple'
hungryFor = 'apple'
if (apple == hungryFor):
    print('OMG APPLES!!')
    
##############################################################
#lists OMG LISTS
##############################################################

myList = ['sql','exel','tableu','COMPTIA Secuirty+']
#help(list)
myList.append('python')
print(myList)

myList.remove('tableu')
print(myList)
print(myList[2])

#sort
myList.sort()
print(f'Sorted List: {myList}')


##############################################################
#dictonary
##############################################################
myDict = {
    'Dootabase':['124','12123','123123'],
    'language':'Google',
    'shard':'my pants'
}
print(myDict)
#help(dict)

#shows keys
print(myDict.keys())

#shows vlaues
print(myDict.values())

myDict['Giggkle'] = 'Shard???'

#get value from dicotrnay
print(myDict.get('shard'))


##############################################################
#Sets
##############################################################

mySet = {
    'Cokc',
    'coke',
    'obama',
    'python'
}

print(f'My set: {mySet}' )

#can do union on these

#converting a list to a set will remove all of the duplicates

##############################################################
#Tuple
##############################################################

#immutable
wiggleTuple = ('car', 'battery', 'apple','Cheese')

print(wiggleTuple[2])


##############################################################
#Loops 
##############################################################

numbers = [0,1,2,3,4,5,6]
chars = 'Student'

#for loop
for num in numbers:
    print(num)
    
for c in chars:
    print(c)
    
for _ in range(5):
    print(_)
    
    
x = 7
while x >= 0:
    print(x)
    x = x  - 1
    
##############################################################
#List comprehension 
##############################################################

#we can make the list using these for in range
numbersList = [x%3+x for x  in range(10)]
print(f'List comprehension {numbersList}') 

#we can also use strings 
stringList = [x for x in 'STUDENT']
print(f'More List Comprehension {stringList}')

#additinally we can add an if to the end good for making sublists of things
numbersListIf = [x for x  in range(10) if x == 3 in range(10)]
print(f'List comprehension {numbersListIf}') 

#smaller funcitons
print(min(numbersList))

print(max(numbersList)