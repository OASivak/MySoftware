class Button:
    def __init__(self):
        pass

    def click(self):
        print("Click")
        
       
class Screen:
    def __init__(self):
        pass

    def welcome(self):
        print("New Screen")


button = Button()
button.click()  # This will print "Click"

screen = Screen()
screen.welcome()  # This will print "New Screen"

