def menu ():
    print('***** MENU *****')
    print('1. Add a new contact')
    print('2. Data entry by keyboard')
    print('3. Find in directory')
    print('4. Edit list')
    print('5. Show list')
    print('6. Exit')
    
def menu2():
    print('a.- Find by name')
    print('b.- Find by phone')
    print('c.- Find by direction')
 
def menu3():
    print("Edit list")
    print('1.- Delete a user')
    print('2.- Edit a user')
 
directory = []
Phones = {}
Names = {}
Addresses = {}
Nicknames = {}
menuoption = 0
menu()
x=0

while menuoption != 6:
    menuoption = int(input("Insert option number: "))
    if menuoption == 1:
        print('Create name of list:')
        list_name=input()
        menu()
 
    elif menuoption == 2:
        print("Add Name, Phone, Address y Nickname")
        Name = input("Name: ")
        Phone = input("Phone: ")
        Address = input("Address: ")
        Nickname = input("Nickname: ")
        Phones[Name] = Phone
        Names[Phone] = Name
        Addresses[Address] = Name
        directory.append([Name, Phone, Address, Nickname])
        menu()
 
    elif menuoption == 3:
        print("Find")
        menu2()
        menuoption2 = input("Insert a letter to choose an option: ")
        if menuoption2=="a":
            Name = input("Name: ")
            if Name in Phones:
                print("El Phone es", Phones[Name])
            else:
                print(Name, "can't be found")
 
        if menuoption2=="b":
            Phone = input("Phone: ")
            if Phone in Names:
                print("The Name is", Names[Phone])
            else:
                print(Phone, "can't be found")
 
        if menuoption2=="c":
            Address = input("Address: ")
            Name = Addresses.get(Address, '')
            if Name:
                print('The Name is: ', Name)
            else:
                print('No record for this address ', Address)
        
    elif menuoption == 4:
        menu3()
        menuoption3 = input("Insert a number to choose an option: ")
        if menuoption3=="1":
            Name = input("Name: ")
            if Name in directory[0:10]:
                print('Delete')
            else:
                print(Name, "can't be found")
        else:
            menu()
        menu()
 
    elif menuoption == 5:
 
        print("\nName list: ",list_name)
        for e in directory:
            print("\nThe list is: ",directory)
        menu()
 
 
    elif menuoption != 6:
        menu()