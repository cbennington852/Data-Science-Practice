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