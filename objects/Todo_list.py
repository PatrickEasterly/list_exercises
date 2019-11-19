from todo_objects import Todo
class Todolist:
# properties

# -todos
    def __init__(self):
        self.todos = []
    
    def display(self):
        for todo in self.todos:
            print(todo)
    
    def add(self, title):
        # Instantiate a new Todo object
        new_todo = Todo(title)
        self.todos.append(new_todo)

    def add_already_completed(self, title):
        new_todo = Todo(title, True)
        self.todos.append(new_todo)
    
    def complete(self, index):
        todo = self.todos[index]
        todo.update_completed(True)