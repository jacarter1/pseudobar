"""The functions and class utilized throughout my project"""

import random
from datetime import date, datetime

comp = ["I can tell you're not like other girls.",
       "you have the most beautiful eyes.",
       "you have an amazing smile.",
       "you look like a work of art.",
       "you're looking good tonight.",
       "I can't keep my eyes off of you.",
       "I'd love to get to know you better.",
       "you're hot.",
       "I'd love to get your Snapchat."]

pickup = ["Are you from Tennessee? Because you're the only 10 I see.",
          "Did it hurt when you fell from heaven?",
          "I’m not a photographer, but I can picture us together.",
          "Have we met before? You look a lot like my next girlfriend.",
          "I lost my phone number. Can I have yours instead?",
          "Do you believe in love at first sight, or should I walk by again?",
          "Is it hot in here, or is it just you?",
          "My shoes must be untied, because I just fell for you.",
          "I’m new around here. Can I have directions to your heart?",
          "If you were a fruit, you'd be a fine-apple."]
    
class SingleMingle(): #Used to break the chat into multiple small conversations
    
    def __init__(self, name, age, friend, school, drink):
        self.name = name
        self.age = age
        self.friend = friend
        self.school = school
        self.drink = drink
    
    def compliment(self):
        """Randomly gives a compliment from the list of compliments, comp
        
        Parameters
        ----------
        from self, self.name (string)
        
        Returns
        ----------
        comp2 : string
            String introducing self.name and comp2 in the form of a sentence 
        """
        
        comp2 = random.choice(comp)
        
        return "Hey, I'm " + self.name + ". I just want to say " + comp2
    
    def pick_up_line(self):
        #This function operates similarly to my compliment function
        #However, this returns just a compliment (no instance attributes)
        """Randomly tells a pick-up line.
        
        Returns
        ----------
        line : string
            random choice of 1 pick-up line from the list, pickup
            
        """
        line = random.choice(pickup)
        
        return line
    
    def wingman(self):
        """Introduces self.friend to user for bar mingling / mating.
        
        Parameters
        ----------
        self.friend : string
            This is the buddy of the class member,
                utilizes first in WingmanMode to 'set up' with our user.
                
        Returns
        -------
        self.friend : string
            Function asks user if they have met self.friend
            Chat then ends as the bot leaves to "get" the friend
            
        """
        return "Have you met my friend, " + self.friend + "? I'll go grab him!"
    
    def over18(self):
        """Chatbot assesses if user is above the legal age of flirtation.
        
        Parameters
        ----------
        self.age : int
            age of the created member of class SingleMingle
            
        string_age : string
            turns self.age into a string
            
        Returns
        -------
        o1 : int
            user's inputted age
            
        o2 : string
            Delivers 1 of 4 possible statements depending on the user's age 
            
        """
        string_age = str(self.age)
        
        o1 = input("Hey, gorgeous! How old are you? (Please respond with a number.)\n")
        
        age = int(o1)
        
        if age in range(0, 18): #Cannot flirt with a minor
            o2 = print("Oh, I'm getting a phone call.\nHave a great night!\n")
        elif age in range(18, 50): #Optimal age range for flirting
            o2 = print("Awesome! I am " + string_age + ".")
        elif age in range (50, 150): #A bit older, but the chatbot is respectful
            o2 = print("Aged like a fine wine!")
        else: #Included in case the user's input is not in range 0-150
            o2 = print("Haha what?/n")
                    
    def want_a_drink(self):
        """Chatbot asks user if they would like a drink from the bar.
        
        Parameters
        ----------
        self.drink : string
            This is the created class member's favorite drink.
            
        Returns
        -------
        w1 : string
            If 'Yes', chatbot then asks what kind of drink.
            If 'No', the chatbot says 'Sure!' 
            
        w2 : string
            If user's desired drink == chatbot's favorite drink (self.drink),
                then the chatbot expresses delight.
                
        """
        w1 = input("Would you like a drink? (Please respond with 'Yes' or 'No')\n")
        if w1 == 'Yes':
            w2 = input("Great! What kind of drink would you like?\n")
            if w2 == self.drink:
                print("That's my favorite, too! You got it.\n")
            else:
                print("Sure!")     
        else:
            w2 = print("Okay! No problem. Have a great night!\n")
    
    def khosla(self):
        """Chatbot asks user if they are a student. Classic bar flirtation move.
        
        Parameters
        ----------
        self.school : string
            This is the school that the created class member attends/attended.
            
        self.friend : string
            This is the buddy of the class member to 'set up' with our user.
            
        Returns
        -------
        k1 : string
            If 'Yes', chatbot asks what school
            If 'No', chatbot ends conversation
            
        k2 : string
            If user attends/attended self.school, the chatbot flirts.
            If user enters a different school:
                Chatbot asks if user has met self.friend, who attends that school.
                
        """
        k1 = input("Are you a student? (Please respond with 'Yes' or 'No')\n")
        if k1 == 'Yes':
            k2 = input("Dope! What school do you go to?\n")
            if k2 == self.school:
                print("How have I never ran into a cutie like you on campus?\n")
            else:
                return("My buddy goes there! Have you met " + self.friend + "?")
        else:
            print("That's awesome!\n")
        
    def check_your_watch(self):
        """Prints the current time. Very useful at a bar setting."""
        watchface = datetime.today()
        print(watchface)