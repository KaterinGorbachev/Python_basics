import random

#make a dictionary of categories and words
def computer_words():
    
    words_library = { 
        'films':['Robocop', 'Ghostbusters', 'Smurfs', 'Juno', 'Chocolat', 'Shrek', 'Cell', 'Ronin', 'Superman', 'Metropolis', 'Evolution'], 
        'countries':['Honduras', 'Belarus', 'Tonga', 'Mexico', 'Madagascar', 'Greece', 'Denmark', 'Mongolia', 'Japan', 'Thailand', 'Slovenia'], 
        'animals':['Alligator', 'Alpaca', 'Bat', 'Beaver', 'Camel', 'Gorilla','Elephant','Deer','Chicken','Chameleon']
    }
    return words_library


#shows the user categories and returns them for a program like a list
def list_categories(words_lib):
    categories = []
    for i in words_lib.keys(): 
        categories.append(i)
    print("Choose the category from: ")
    count = 0
    for i in categories: 
        count +=1
        print(count, "for", i)
    return categories


#remember users choice of a category
def get_category(categories):
        
    try:
        category = int(input(f"Enter number from 1 to {len(categories)} to choose a category: "))
        if category <= 0:
            print("************************************************\n* Just enter a number bigger than 0. Try again *\n************************************************")
            return get_category(categories)
        elif category> len(categories): 
            print("************************************************\n* There is no a category with entered number.Try again *\n************************************************")
            return get_category(categories)
        else: 
            print(f"You have chosen {categories[category-1]}")
            return categories[category-1]
    
    
    except: 
        print(f"***************************************\n* Waiting for a number from 1 to {len(categories)}..... *\n***************************************")
        return get_category(categories)


#give a random word from chosen category
def get_computer_word(words_lib, category): 
    
    try: 
        return random.choice(words_lib[category])
    except KeyError: 
        print("Something whent wrong! Try to get a category first")
        exit
        
        


#get a category from a player 
def game_master_category(): 
    print("***************************************\n* The Game Master enters the category *\n***************************************")
    category = input("Write the category: ").strip()
    if category.isalpha():
        print(f"***************************************\n* The category is {category} *\n***************************************") 
    else: 
        print("*************************************************************************************\n* The category should be written with letters only and without spaces in the middle *\n*************************************************************************************")
        return game_master_category()


#get a word from a player
def game_master_word(): 
    print("********************************************\n* The Game Master enters the word secretly *\n********************************************")
    word = input("Write the word: ").strip()
    if word.isalpha():
        return word
    else: 
        print("*******************************************************************************\n* The word is not a word without letters. Numbers and spaces are not allowed. *\n*******************************************************************************")
        return game_master_word()
    


#get a letter from player 
def get_letter(): 
    letter = input("Enter one letter: ")
    letter = letter.strip()                ##delete spaces first and the last 
       
    if len(letter) > 1: 
        print("You have entered more than 1 symbol.")
        return get_letter()
    else: 
        ###check if it is a letter 
        if letter.isalpha(): 
            return letter
        else: 
            print("You have not entered one letter. Try again!")
            return get_letter()


#check if the letter has been used 
def check_letter_usage(wrongLetters, correctLetters, letter): 
    if letter not in wrongLetters and letter not in correctLetters: 
        return letter
    else: 
        print("You cant use the letter twice")
        return get_letter()
    




def menu(): 
    try: 
        i = int(input("Enter a number: "))
        if i in range(3):
            return i 
        else: 
            print("You must enter 0, or 1, or 2. Can't enter other numbers")
            return menu()
    except Exception as e: 
        print(f"You must enter 0, or 1, or 2. ERROR: {e}")


class HumanHorca(): 

    startbulk = [" +------+"]
    bulk = [" ^      |"]
    head = "  o  "
    neck = "  |  "
    leg = "   \\"
    legTwo = " / \\ "
    legLong = "   |"
    legsLong = " | |"
    suelo = ["============"]
    letra1 = ["     ","  |"]

    def __init__(self, word): 
        self.length = [HumanHorca.letra1[:] for i in range(len(word))]
        self.wrongLetters = []
        self.correctLetters = []
        
       
    

    
    def add_wrong_letter(self, letter, word):
        if letter not in word and letter not in self.wrongLetters and letter not in self.correctLetters:
            self.wrongLetters.append(letter)
            

        

    

    def add_correct_letter(self, letter, word): 
        if letter in word  and letter not in self.wrongLetters and letter not in self.correctLetters: 
            self.correctLetters.append(letter)
           

  
    

    def update_length(self, letter, word): 
        if len(self.wrongLetters) == 1: 
            self.length[0][0] = HumanHorca.head
        elif len(self.wrongLetters) == 2: 
            self.length[1][0] = HumanHorca.neck
        elif len(self.wrongLetters) == 3: 
            self.length[2][0] = HumanHorca.leg
        elif len(self.wrongLetters) == 4: 
            self.length[2][0] = HumanHorca.legTwo
        elif len(self.wrongLetters) == 5: 
            self.length[3][0] = HumanHorca.legsLong
        elif len(self.wrongLetters) > 5: 
            self.length[len(self.wrongLetters)][0] = HumanHorca.legsLong

        for m in range(len(word)): 
            if word[m] == letter: 
                self.correctLetters.append(letter)
                self.length[m][1] = '   '+letter

    
    ## printing method
    def print_horca(self): 
        print(*HumanHorca.startbulk, *HumanHorca.bulk, sep = '\n')
        for j in self.length: 
            print(*j)
        print(*HumanHorca.suelo)

        
    

    
    
#secret = HumanHorca('pan')

#print(*secret.horca)
#secret.print_horca()

def main(): 

    print("!!!Welcome to the HANGMAN game!!!\nTry to guess the word. \nYou have as many tries as there are letters in the word. The number of letters is the number of | on the right of the hang.\nWith each error appears a part of the man.\nGo and save a sole!\n\n\n Choose the mode of play: \n 1 for PC\n 2 for Player 2\n 0 for Exit")
    
    option = menu()
    
    if option == 1: 
        words_library = computer_words()
        categories = list_categories(words_library)
        category = get_category(categories)
        word = get_computer_word(words_library, category).lower()

    elif option == 2: 
        category = game_master_category() 
        word = game_master_word().lower()

    elif option == 0: 
        print("The game is over")
        exit

    secret = HumanHorca(word)

    secret.print_horca()

    count = 0 
    while count <= len(word)-1: 
        letter = get_letter().lower()
        if letter in secret.correctLetters or letter in secret.wrongLetters:
            print("You can't use the letter twice.")
            continue
        if letter in word:
            secret.add_correct_letter(letter, word)
            count +=1
        else:
            secret.add_wrong_letter(letter, word)
            count +=1

        secret.update_length(letter, word)
        secret.print_horca()


    if len(secret.correctLetters) == len(word): 
        print("Congratulations!!!!!!!!!!!! YOU WIN !!!!!!!!!!")

    else: 
        print("Nice try! Lets play again!")
        main()
    








'''
def main(): 

    print("!!!Welcome to the HANGMAN game!!!\nTry to guess the word. \nYou have as many tries as there are letters in the word. The number of letters is the number of | on the right of the hang.\nWith each error appears a part of the man.\nGo and save a sole!\n\n\n Choose the mode of play: \n 1 for PC\n 2 for Player 2\n 0 for Exit")
    
    option = menu()
    
    if option == 1: 
        words_library = computer_words()
        categories = list_categories(words_library)
        category = get_category(categories)
        word = get_computer_word(words_library, category).lower()

    elif option == 2: 
        category = game_master_category() 
        word = game_master_word().lower()

    elif option == 0: 
        print("The game is over")
        exit

    count = 0
    
    wrongLetters = []       #variable de instancia 
    correctLetters = []     #variable de instancia 
    
    letra1 = ["     ","   |"]
    startbulk = [" +------+"]
    bulk = [" |      |"]
    head = "  o  "
    neck = "  |  "
    leg = "   \\"
    legTwo = " / \\ "
    legLong = "   |"
    legsLong = " | |"
    suelo = ["============"]
    humanHorca = [letra1[:] for i in range(len(word))]

    
    while count < len(word): 
        letter = get_letter().lower()
        check_letter_usage(wrongLetters, correctLetters, letter)
        
        
        

       
        
        if letter not in word: 
            count +=1
            wrongLetters.append(letter)
            if len(wrongLetters) == 1: 
                humanHorca[0][0] = head
            elif len(wrongLetters) == 2: 
                humanHorca[1][0] = neck
            elif len(wrongLetters) == 3: 
                humanHorca[2][0] = leg
            elif len(wrongLetters) == 4: 
                humanHorca[2][0] = legTwo
            elif len(wrongLetters) == 5: 
                humanHorca[3][0] = legsLong
            elif len(wrongLetters) > 5: 
                humanHorca[len(wrongLetters)-4][0] = legsLong




        else: 
            count += 1

            for m in range(len(word)): 
                if word[m] == letter: 
                    correctLetters.append(letter)
                    humanHorca[m][1] = '   '+letter

            
            
        print(f"WrongLetters: {wrongLetters}", startbulk, bulk, sep = '\n')
        for j in humanHorca: 
            print(*j)
        print(suelo)


    if len(correctLetters) == len(word): 
        print("Congratulations!!!!!!!!!!!! YOU WIN !!!!!!!!!!")

    else: 
        print("Nice try! Lets play again!")
        main()

        

                


'''


if __name__ == '__main__': 
    main()












