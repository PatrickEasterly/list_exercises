#keep track of todos
#add todos
#delete todos
#print todos
#show main menu

    ###

#keep track of todos
todo_list = []

#print todos

def print_todos():
    # print('\n')
    if todo_list == []:
        print('You have nothing to do. ')
    for todo in todo_list:
        print(todo)
#add todos

def add_todo(todo): 
    todo_list.append(todo)


#delete todos

def delete_todo(index):
    # del todo_list[index]
    try:
        todo_list.pop(index)
    except IndexError:
        print('Sorry, no todo at that index.')
        


def main():
    menu = '''
    Your favorite todo app
    ======================
    0. Quit
    1. Print Todos
    2. Add a Todo
    3. Complete a todo
    '''
    is_running = True
    while is_running == True:
        print(menu)
        choice = input('Choose one: ')
        if choice == '0':
            is_running = False
        elif choice == '1':
            print_todos()
        elif choice == '2':
            todo = input('Your todo: ')
            add_todo(todo)
        elif choice == '3':
            pass
        else:
            print('\nPlease enter a valid choice')

main()