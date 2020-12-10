"""Tests for my functions in the Pseudobar module"""

from JC_module import pseudobar_functions as pf 
from datetime import date, datetime

def test_SingleMingle(self):
    """Tests that every necessary attribute of my class is present.
    Also tests that every attribute matches the desired object type."""
    assert self.name
    assert self.age
    assert self.friend
    assert self.school
    assert self.drink
    assert self.name != self.friend
    assert isinstance(self.name, str)
    assert isinstance(self.age, int)
    assert isinstance(self.friend, str)
    assert isinstance(self.school, str)
    assert isinstance(self.drink, str)
    
def test_compliment():
    """Tests the class attribute compliment(self)"""
    
    Drake = pf.SingleMingle(name = "Drake",
                    age = 32,
                    friend = "Josh",
                    school = "SDSU",
                    drink = "Natty Light")
    
    drake_compliment = Drake.compliment()
    print(drake_compliment)
    
    assert "Hey, I'm "
    assert "Drake"
    assert ". I just want to say "
    assert drake_compliment
    assert isinstance(drake_compliment, str)
    
def test_pick_up_line():
    """Tests the class attribute pick_up_line(self)"""
    
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
    
    Drake = pf.SingleMingle(name = "Drake",
                    age = 32,
                    friend = "Josh",
                    school = "SDSU",
                    drink = "Natty Light")
    
    drake_line = Drake.pick_up_line()
    print(drake_line)
    
    assert drake_line in pickup
    assert isinstance(drake_line, str)

def test_wingman():
    """Tests my method Wingman(self)"""
    
    Drake = pf.SingleMingle(name = "Drake",
                    age = 32,
                    friend = "Josh",
                    school = "SDSU",
                    drink = "Natty Light")
    
    drake_wingman = Drake.wingman()
    print(drake_wingman)
    
    assert "Have you met my friend, "
    assert "Josh"
    assert "? I'll go grab him!"
    assert isinstance(drake_wingman, str)

def test_over18():
    """Tests my method over18(self)"""
    
    Drake = pf.SingleMingle(name = "Drake",
                    age = 32,
                    friend = "Josh",
                    school = "SDSU",
                    drink = "Natty Light")
    
    drake_over18 = Drake.over18()
    
    string_age = str(32)
    
    assert string_age
    assert isinstance(string_age, str)

def test_check_your_watch():
    """Tests that method check_your_watch(self) presents the current time"""
    
    Drake = pf.SingleMingle(name = "Drake",
                    age = 32,
                    friend = "Josh",
                    school = "SDSU",
                    drink = "Natty Light")
    
    drake_watch = Drake.check_your_watch()
    return drake_watch

    assert drake_watch
    assert drake_watch != datetime(2020, 1, 1)
 