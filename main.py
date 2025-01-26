# Creating Manu
f = open('base.txt', 'a+')
read_base = open('base.txt', 'r')
backno ='No'
backyes ='yes'
interface = True


def user_input(name):
   if  menu == 1:
        f.write(name + '\n')

while interface:
    print('1. Add a name to the base \n2.Delete a name from the base\n3.Get name from the base \n4.Edit a name \n5.Exit')
    menu = int(input('input an option : '))
    if menu ==1:
        user_input(name=input('type a name :'))
        name_added()
    elif menu == 2:
        print('\nOption 2 executed')
    elif menu == 3:
        print('\nOption 3 executed')
    elif menu == 4:
        print('\nOption 4 executed')
    elif menu > 4:
        print('program closed')
        interface = False







import random
marks=random.randrange(start=0, stop=1)
print(marks)

if marks>=90:
    print("A")
elif marks >=80:
    print('B')
elif marks >=70:
    print('C')
elif marks >=60:
     print('D')
elif marks >=50:
     print('E')

else:
  print("Fail")






