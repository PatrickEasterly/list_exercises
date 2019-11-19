# blueprint
# a.k.a. factory
# a.k.a. class

class Todo:
    # instructions for how to construct a new Todo oject
    # Assume a new todo is not completed
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed
        
    #behaviors

    # example of encapsulation
    # the details of how your code works are hidden. 
    # you give an interface, and that's good enough.
    #  Don't build me a watch, tell me the time

    def update_title(self, new_title):
        self.title = new_title

    completed_tasks = 0

    def update_completed(self, current_completed_status):
        self.completed = current_completed_status
        completed_tasks += 1

    def display(self):
        # talk = input('What do you want to say')
        # MUST use keyword self as first arg 
        # it links the function to the object
        # "Constructor"
        # "dunder init", or double undersocre init
        print(self.title)

    def __str__(self):
        return f"{self.title} ({self.completed})"
