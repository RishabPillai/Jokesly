import random

jokes = ["What’s the best thing about Switzerland I don’t know, but the flag is a big plus.","I invented a new word! Plagiarism!",
         "Did you hear about the mathematician who’s afraid of negative number He’ll stop at nothing to avoid them."
         ,"Why do we tell actors to “break a leg? Because every play has a cast. "]

def get_joke():
    joke = random.choice(jokes)
    print(joke)

def alljoke():
    print(jokes)
    
def add_joke(new_joke):
    jokes.append(new_joke)

def remove_joke(remove_joke):
    jokes.remove(remove_joke)

