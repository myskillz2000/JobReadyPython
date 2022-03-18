""" A function that can return your name. """

def hello(x):
    try:
        return "Hello" + " " + x
    except:
        return "You need to enter a name not a number."

print(hello('Matt'))