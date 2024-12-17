secretWords = ['wolf', 'moto', 'madona']
alfabet = list('abcdefghijklmnñopqrstuvwxyz')

wrongLetras = []
correctLetras = []

letra1 = ["   ","   ",   " |"]

startbulk = ["  +------+"]
bulk = ["  |      |"]
head = " o "
neck = " | "
leg = "  \\"
legTwo = "/ \\"
legLong = "  |"
legsLong = "| |"
suelo = ["============"]

humanHorca = [wrongLetras, startbulk, bulk, suelo]
counter = 0
counterWrong = 0

#info about the rules 
print("!!!Welcome to the HANGMAN game!!!\nTry to guess the word. \nYou have as many tries as there are letters in the word. The number of letters is the number of | on the right of the hang.\nWith each error appears a part of the man.\nGo and save a sole!")


#menu 
print("Choose the category ***** animals - 1 ***** transport - 2 ***** singers - 3 ***** ")
userChoiceMenu = int(input("Your choice:  "))

if (userChoiceMenu - 1) == 0: 
    secretWord = secretWords[0] 
   
if (userChoiceMenu - 1) == 1: 
    secretWord = secretWords[1] 
if (userChoiceMenu - 1) == 2: 
    secretWord = secretWords[2] 

secretWord = list(secretWord)


#word length
for i in secretWord: 
    humanHorca.insert(3, letra1[:])

#number of tries 
print(f"You have {len(secretWord)} tries. If the letter appears in the word twice or more times - you spent the same number of tries. You will win if guess all the letters!")
    

while (counter < len(secretWord)) and (counterWrong < len(secretWord)):
    
    stopGame = input("""Would you like to continue? Press space for "yes" or any other key for "no": """)
    if stopGame.lower() != ' ': 
        break

    
    userLetra = input("Enter the letter: ") 

    for i in range(len(secretWord)): 

#checks 
        if userLetra in wrongLetras: 
            print("You cant use the letter twice")
            break
        elif userLetra in correctLetras: 
            print("You cant use the letter twice") 
            break
        elif userLetra not in alfabet: 
            print("You should use letters only")
            break
        elif len(userLetra) > 1: 
            print("You should enter only 1 letter")
            break

#check if it is right 
        elif userLetra in secretWord: 
        
            correctLetras.append(userLetra)

            for j in range(len(secretWord)):
                if secretWord[j] == userLetra:
                    userLetraPosition = j+3 
                    humanHorca[userLetraPosition][2] = userLetra
                    counter += 1


            for item in humanHorca: 
                print(*item)
            break


#check if it is wrong
        elif userLetra not in secretWord: 
            wrongLetras.append(userLetra)
             
            
            if counterWrong == 0: 
                humanHorca[counterWrong+3][0] = head

            elif counterWrong == 1: 
                humanHorca[counterWrong+3][0] = neck

            elif counterWrong == 2: 
                humanHorca[counterWrong+3][0] = leg
                
            elif counterWrong == 3: 
                humanHorca[counterWrong+2][0] = legTwo
                
            elif counterWrong == 4: 
                humanHorca[counterWrong+2][0] = legLong
                
            elif counterWrong == 5: 
                
                humanHorca[counterWrong+1][0] = legsLong

            elif counterWrong >5: 
                humanHorca[counterWrong+3][0] = legsLong

            counterWrong += 1
            for item in humanHorca: 
                print(*item)
            break
    
    
if counter == len(secretWord):
    print("!!!!You win!!!!!")
else: 
    print("You lost :(\nNice try!")




    



        






