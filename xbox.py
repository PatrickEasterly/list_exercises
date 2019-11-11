from random import seed
from random import randint
def xbox(name):
    name = name.upper()
    name = name.replace("L", "1")
    name = name.replace("E", "3")
    name = name.replace("T", "7")
    name = name.replace("S", "5")
    name = name.replace("O", "0")
    name = "xX" + name + "Xx"
    return name
name = input("Write your xbox gamertag. ")
name = xbox(name)
clan_tags = ['KSI', 'BEAR', 'ALI', 'JFK']
rando = randint(0, 3)
my_clan_tag = clan_tags[rando]
print(f'[{my_clan_tag}] {name}')