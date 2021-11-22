import random
name = input("What is your name? ")
print ("Hello, " + name, "Time to play GOOD LUCK!")
print ("Start guessing...\n")
words = ['python','programming','treasure','creative','medium','horror']
word = random.choice(words)
guesses = ''
turns = 3
while turns > 0:         
    failed = 0             
    for char in word:      
        if char in guesses:    
            print (char,end="")    
        else:
            print ("_",end=""),     
            failed += 1    
    if failed == 0:        
        print ("\nYou won") 
        break              
    guess = input("\nguess a character:") 
    guesses += guess                    
    if guess not in word:  
        turns -= 1        
        print("\nWrong")    
        print("\nYou have", + turns, 'more guesses') 
        if turns == 0:           
            print ("\nYou Lose") 
