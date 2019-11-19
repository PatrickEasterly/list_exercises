#keep track of todos
#add todos
#delete todos
#print todos
#show main menu

    ###

#keep track of todos
todo_list = ['sample', 'list']

#print todos

def print_todos():
    # print('\n')
    if todo_list == []:
        print('\nYou have nothing to do. ')
    for count, todo in enumerate(todo_list):
        print(f'\n{count}: {todo}')
#add todos

def add_todo(todo): 
    todo_list.append(todo)


#delete todos

def delete_todo(index):
    # del todo_list[index]
    try:
        todo_list.pop(index)
    except IndexError:
        print('\nSorry, no todo at that index.')
        


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
        choice = input('\nChoose one: ')
        if choice == '0':
            is_running = False
        elif choice == '1':
            print_todos()
        elif choice == '2':
            new_todo = input('What do you need todo? : ')
            add_todo(new_todo)
        elif choice == '3':
            delete = int(input('Complete which todo? '))
            delete_todo(delete)
        else:
            print('\nPlease enter a valid choice')

main()