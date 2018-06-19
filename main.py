from spy_details import spy_name ,spy_salutation , spy_age, spy_rating

print "Let's get started"

response= raw_input('Do you want to continue as '+ spy_salutation + " " + spy_name+ "?(Y/N)")


def start_chat (spy_name, spy_age, spy_rating):
    menu_choices = "What do you want to do? \n 1. Add a status update \n"
    menu_choices = int (raw_input(menu_choices))

    if menu_choices =="1":
        print "Status update function called"
    else:
        exit()



if response=="Y":
    #start the
    print "Welcome "+ spy_salutation+  " " +spy_name
    start_chat( spy_name , spy_age , spy_rating)
else:
    spy_name =raw_input('Welcometo spy chat, you must tell meyour name first: ')

    if len(spy_name)>0:
        print 'Welcome ' + spy_name + ' Glad to have you back'
        spy_salutation =raw_input('What should we call you(Mr. or Ms.)')
        spy_name= spy_salutation +" "+spy_name
        print 'Alright ' + spy_name +'. I\'d like to know a little bit more about ou before we proceed'
        spy_age= input('what is your spy age?')
        if spy_age>12 and spy_age<50:
            spy_rating = input('What is your spy_rating?')
            if spy_rating>4.5:
                print"you are gret"
            elif spy_rating>3.5 and spy_rating < 4.5:
                print 'Work harder'
        else:
            print "Sorry you are not of correct age to be a spy"

        spy_is_online = True
        print "Authentication complete. Welcome " + spy_name + " age: " + str(spy_age) + " and rating of: " + str(spy_rating) + " proud to have you on board"

    else:
        print "A spy needs to have a val id name. Please try again later"

    start_chat( spy_name , spy_age , spy_rating)