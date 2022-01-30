
        #name = input("enter you name: ")
        #age = input("enter you age: ")
        #print("hello " + name + "! you are " + age)


        #num1 = input("Enter a number: ")
        #num2 = input("Enter anohter number: ")
        #result = float(num1) + float(num2)
        #result2 = float(num1) * float(num2)



        #print(result)
        #print(result2)


            #color = input("Enter a color: ")
            #plural_noun = input("Enter a plural noun: ")
            #celebrity = input("Enter a celebrity: ")

        #print(" Roses are " + color)
        #print(plural_noun + " are blue ")
        #print(" I love " + celebrity)

        #homework////mad lips
        #world = input("Enter a weather: ")
        #hate = input("Enter a thing u hate in it: ")
        #love = input("Enter a thing u love in it: ")



        #print("summer season is " + world)
        #print("i hate " + hate)
        #print("i love " + love)


#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-----Lists----xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                        #|
                            #it stores multiple strings


    #friends = ["Kevin", "Karen", "Jim", "Oscar", "Tobyw"]
    #friends[1] = "mike"
    #print(friends[1])

#xxxxxxxxxxxxxxxxxxxxxxxxxx-----Lists functions----xxxxxxxxxxxxxxxxxxxxxxxxx

        #lucky_numbers = [4, 8, 15, 16, 23, 42]
        #friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]


    #friends.extend((lucky_numbers))# added 2 lists with each other
    #friends.append("creed")# adds another string to the list at last
    #friends.insert(1, "Kelly")# adds a string in between of list
    #friends.remove("Kevin")# removes a particular string in a list
    #friends.clear()# clears a list
    #friends.pop()# it removes the last string from the list
    #friends.sort()# it sorts according to alphabetical order
    #friends.reverse()# reverses a list
    #friends2 = friends.copy()# it copies a list

    #print(friends.index("Jim"))# it tells what is the index of the string and if its there
    #print(friends.count("Jim"))# it shows how many strings are there with same name

        #print(friends)


#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-----Tuples----xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                        #|
                   # Container which stores different values (immutable)

            #cooridnates = [(4, 5), (6, 7), (80 ,34)]
            #print(cooridnates[1])

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-----Functions----xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                        #|
                    #collection of code which performs specific tasks

       # def say_hi(name,age): # def means we are using function
         #   print("Hello " + name + ", you are " + age)


      #  say_hi("Mike", "35")
       # say_hi("set", "20")

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-----Return statement----xxxxxxxxxxxxxxxxxxxxxxxxxx
                                           #|
                             # A keyword that returns information

            #def cube(num):
              # return num*num*num

            #result = cube(4)
            #print(result)

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-----If statements----xxxxxxxxxxxxxxxxxxxxxxxxxxx
                                            #|
                         #It makes decision on certain conditions

#is_male = False
#is_tall = False

#if is_male and is_tall:
  #print("You are a tall male")

#elif is_male and not (is_tall):
   #print("You are short male")

#elif not (is_male) and is_tall:
   #print("You are not a male but are tall")

#else:
   #print("you are not male not tall ")
#xxxxxxxxxxxxxxxxxxxxxxx-----If statements and comaprisions----xxxxxxxxxxxxxxxxxxxx

#def max_num(num1, num2, num3):
  #if num1 == num2 and num1 >= num3:
    #return num1
  #elif num2 >= num1 and num2 >= num3:
    #return num2
  #else:
    #return num3

#print(max_num(40, 40, 5))

#xxxxxxxxxxxxxxxxxxxxxxx-----Building a better calculator----xxxxxxxxxxxxxxxxxxxxx

#num1 = float(input("Enter first number: "))
#op = (input("Enter operator: "))
#num2 = float(input("Enter second number: "))

#if op =="+":
  #print(num1 + num2)
#elif op == "-":
  #print(num1 - num2)
#elif op == "*":
  #print(num1 * num2)
#elif op == "/":
  #print(num1 / num2)
#else:
  #print("Invalid operator")


#xxxxxxxxxxxxxxxxxxxxxxxxxxxxx-----Dictionaries----xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                        #|
     #it is a special structure which stores values and called "key value pairs"

#monthConservations = {
    #0: "January",
    #"Feb": "February",
    #"Mar":  "March",
    #"Apr":  "April",
    #"May":  "May",
    #"Jun":  "June",
    #"Jul":  "July",
    #"Aug":  "August",
    #"Sep":  "September",
    #"Oct":  "October",
    #"Nov":  "November",
    #"Dec":  "December",

#}

#print(monthConservations.get(0))

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxx-----While loop----xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                       #|
                 #  it execute a block of code multiple times

#i = 1
#while i <= 5:
    #print(i)
    #i = i + 1

#print("done with loop")

#xxxxxxxxxxxxxxxxxxxxxxx-----Building a Guessing game----xxxxxxxxxxxxxxxxxxxxxxxxx

#secret_word = "giraffe"
#guess = ""
#guess_count = 0
#guess_limit = 3
#out_of_guesses = False

#while guess !=secret_word and not(out_of_guesses):
    #if guess_count < guess_limit:
        #guess = input("Enter guess: ")
        #guess_count += 1
    #else:
        #out_of_guesses = True

#if out_of_guesses:
    #print("Out of Guesses, YOU LOSE!" )
#else:
    #print("YOU WIN!")

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-----For loop----xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                         #|
                         # it helps loop over collection of itenms

#friends = ["Jim", "Karen", "MIke"]
#len(friends)
#for name in range(2):
    #if name == 0:
        #print("first Iteration")
    #else:
        #print("Not first")

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxx-----Expoenent Function----xxxxxxxxxxxxxxxxxxxxxx

#def raise_to_power(base_num, pow_num):
    #result = 1
    #for index in range(pow_num):
        #result = result * base_num
    #return result

#print(raise_to_power(2, 10))

#xxxxxxxxxxxxxxxxxxxxxxx-----2D Lists and nested Loops---xxxxxxxxxxxxxxxxxxxxxxxx

#number_grid = [
   #[1, 2, 3],
   #[4, 5, 6],
   #[7, 8, 9],
   #[0]
#]

#print(number_grid[2][1]) # optional
#for row in number_grid:
    #or col in row:
        #print(col)

#xxxxxxxxxxxxxxxxxxxxxxx-----Build a translator---xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#def translate(phrase):
    #translation = ""
    #for letter in phrase:
        #if letter.lower() in "aeiou":
            #if letter.isupper():
                #translation = translation + "G"
            #else:
                #translation = translation + "g"
        #else:
            #translation = translation + letter
    #return translation

#print(translate(input("Enter a phrase: ")))


#xxxxxxxxxxxxxxxxxxxxxxxxxxxxx------Finding errors----xxxxxxxxxxxxxxxxxxxxxxxxxx

#try:
    #umber = int(input("Enter a number: "))
    #print(number)
#except:
    #print("Invalid input")

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxx------Reading Files----xxxxxxxxxxxxxxxxxxxxxxxxxx

#emply = open("emp.txt", "r")
#for emplyo in emply.readlines():
    #print(emplyo)

#emply.close()

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxx------Writing Files----xxxxxxxxxxxxxxxxxxxxxxxxxx


#emply = open("emp.txt", "a")
#emply.write("\nkelly")

#emply.close()


#xxxxxxxxxxxxxxxxxxxxxxxxxxxxx------Modules and pip----xxxxxxxxxxxxxxxxxxxxxxxxxx
                                            #|
                  #  python file which import in current python file


#import useful_tools

#print(useful_tools.roll_dice(10))

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxx------Classes and objects----xxxxxxxxxxxxxxxxxxxxxxxxxx
                           # help create objects and structures

#from Student import Student

#student1 = Student("Jim", "Buisness", 3.1, False)

#print(student1.gpa)

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxx--Multiple choice quiz----xxxxxxxxxxxxxxxxxxxxxxxxxx
#from Question import Question

#question_prompts = [
    #"What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    #"#What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    #"What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
#]

#questions = [
    #Question(question_prompts[0], "a"),
    #Question(question_prompts[1], "c"),
    #Question(question_prompts[2], "b"),
#]

#def run_test(questions):
    #score = 0
    #for question in questions:
        #answer = input(question.prompt)
        #if answer == question.answer:
            #score += 1
    #print("You got" + str(score) + "/" + str(len(questions))+ "Correct")

#run_test(questions)

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxx--Object functions----xxxxxxxxxxxxxxxxxxxxxxxxxx

#from Student import Student

#student1 = Student("Oscar", "Accounting", 3.1)
#student2 = Student("Phyllis", "BUisness", 3.8)

#print(student2 .on_honor_roll())

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxx--Inheritance----xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                    #|
         #    it defines attributes and functions inside of class

#from Chef import Chef
#from ChineseChef import ChineseChef

#myChef = Chef()
#myChef.make_special_dish()

#myChineseChef = ChineseChef()
#myChineseChef.make_special_dish()


#xxxxxxxxxxxxxxxxxxxxxxxxxxxxx------Python intrepreter----xxxxxxxxxxxxxxxxxxxxxxxx
                                      #Last topic 😂😂😂
                                    #For beginners 😶😫

#BYeeeeeeee







