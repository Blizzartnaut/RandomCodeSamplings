keepgoing = input("Do you wish to create a list? ")
list1=list()
keepgoing = keepgoing.lower()
def Whileloop(keepgoing, list1):
    while keepgoing == "yes":
        adlist=input("What would you like to add to the list? ")
        list1.append(adlist)
        print("Current list is", list1)
        keepgoing = input("Do you wish to continue to add to the list? ")
        keepgoing = keepgoing.lower()

def ifloop(quest, list1, keepgoing):
    if quest == "yes":
        what=input("What are you looking for? ")
        isitthere=str(what in list1)
        if isitthere == "True":
            isitthere = "Yes it is there"
        else:
            isitthere = "It was not found"

        try:
            posisitthere=str(list1.index(what)+1)
        except:
            posisitthere="n/a"

        print(str(isitthere),"in position", str(posisitthere))
        keepgoing = input("Do you want to continue with the list? ")
        Whileloop(keepgoing, list1)
    elif quest == 'no':
        print("Thank you, the list is complete.")
    else:
        print("I'm sorry, that answer didnt make sense. Please try again later.")
        
Whileloop(keepgoing, list1)

quest=input("Is there something your looking for? ")
quest=quest.lower()
ifloop(quest, list1, keepgoing)