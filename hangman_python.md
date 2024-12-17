# HANGMAN GAME

The general operation of the game is as follows:

The user selects the topic for which a secret word will be chosen. The game then chooses the secret word from the list.

The player is asked to guess the secret word letter by letter.

If the player guesses all the letters he wins; if not, he loses.

The hang has a trunk made of | in a number of the letters in the word, guessed letter occupies its position in the trunk.
On the left side of the trunk when a user does not guess the letter the game draws a man.

Steps:

1-Themes lists

2-Inform the player of the rules

3-Select word category

4-Declare the number of lives and start the game

5-Ask the player to guess a letter

6-Verify that the player is still in the game

7-Print game results

8-Logic to determine if the player won



## Code without functions

The [file](https://github.com/KaterinGorbachev/Python---basics-/blob/main/hangman_python.md) with code 

The first step is to prepare some graphic 


```python 
letra1 = ["   ","   ",   " |"]
startbulk = ["  +------+"]
bulk = ["  |      |"]
head = " o "
neck = " | "
leg = "  \\"
legTwo = "/ \\"
legLong = "   |"
legsLong = "||"
suelo = ["============"]
```


The second is a simple menu


```python
print("Choose the category ***** animals - 1 ***** transport - 2 ***** singers - 3 ***** ")
userChoiceMenu = int(input("Your choice:  "))

if (userChoiceMenu - 1) == 0: 
    secretWord = secretWords[0] 
   
if (userChoiceMenu - 1) == 1: 
    secretWord = secretWords[1] 
if (userChoiceMenu - 1) == 2: 
    secretWord = secretWords[2] 
```


Then is making the hang with a specific length


```python 
for i in secretWord: 
    humanHorca.insert(3, letra1[:])
```   


Some checks could be useful 


```python 
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
```


The main checks are for the right and the wrong letter. 

The drawing of a man is in the wrong check loop.


```python 
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

```

Finally is the result
