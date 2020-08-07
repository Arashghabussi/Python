# Hangman Game 

# Exporting file
def textBank():
    text_file = open("texts.txt", "r")
    return text_file
    
# Hidden Convertor
def hiddenText():
    text_file = textBank()
    text_string = text_file.read()
    hidden_phrase = list(text_string)
    for x in range(0, len(text_string)):
        if(text_string[x] == " "):
            hidden_phrase[x] = ' '
        else:
            hidden_phrase[x] = '*'
    return text_string, hidden_phrase

# Occurance Counter
def occuranceCounter(charcter, text_String):
    counter = []
    for x in range(0, len(text_String)):
        if(text_String[x] == charcter):
            counter.append(x)
    return counter

# User Input
def userInput():
    char_entery = input("Guess: ")
    return char_entery
    
# Brain
def brain():
    text_string, hidden_phraser = hiddenText()
    print("".join(hidden_phraser))
    char_entery = userInput()
    while('*' in hidden_phraser):
        foundedList = occuranceCounter(char_entery, text_string)
        if(char_entery in text_string):
            for index in foundedList:
                hidden_phraser[index] = (char_entery)
        else:
            print('not found')

        print("".join(hidden_phraser))
        winning(hidden_phraser)
        char_entery = userInput()

# Winning
def winning(hidden_phraser):
    if('*' in hidden_phraser):
        pass
    else:
        print('Won')
        exit()

brain()