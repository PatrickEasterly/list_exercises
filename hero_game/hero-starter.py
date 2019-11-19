from Goblin import Goblin
from Hero import Hero
"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

def main():
    pat = Hero()
    gobbles = Goblin()
    while gobbles.is_alive() and pat.is_alive():
        # print("You have %d health and %d power." % (pat.health, pat.power))
        print(pat.health_status())
        # print("The gobbles has %d health and %d power." % (gobbles.health, gobbles.power))
        print(gobbles.health_status())
        print()
        print("What do you want to do?")
        print("1. fight gobbles")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            pat.attack(gobbles)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if gobbles.health > 0:
            gobbles.attack(pat)

main()
