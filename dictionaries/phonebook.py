# Electronic Phone Book
# =====================
# 1. Look up an entry
# 2. Set an entry
# 3. Delete an entry
# 4. List all entries
# 5. Quit

# What do you want to do (1-5)?
#####
# phone numbers
contacts = {
    'Pat': '678-654-2784',
    'Ryan': '404-993-0499',
    'John': '404-409-1183'
}

# look up an entry
# lookup_input = input('Name: ')
def look_up():
    lookup_input = input('Name: ')
    print(contacts[lookup_input])

# set a new entry
def new_entry():
    entry_name = input('New Contact: ')
    entry_number = input('number: ')
    contacts[entry_name] = entry_number
    print(f'Entry stored for {entry_name}')
    print(contacts)
    
# new_entry(entry_name, entry_number)

# delete an entry

# def delete_entry(name):
#     del contacts[name]
#     print(f'{name} removed. ')
#     print(contacts)
# delete_entry('Pat')
# list all entries

# quit
# def choose(choice):
#     print(f'CHOOICE = {choice}')
#     options = {
#         1: (look_up()),
#         2: (new_entry()),
#     }
    
#     options[choice]

main
def main():
    phone = True
    while phone == True:
        print('''
# Electronic Phone Book
# =====================
# 1. Look up an entry
# 2. Set an entry
# 3. Delete an entry
# 4. List all entries
# 5. Quit
        ''')
        choice = int(input('# What do you want to do? '))
        print(f"choice = {choice}")
        choose(choice)
# choice
main()