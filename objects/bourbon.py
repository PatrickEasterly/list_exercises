a_bottler = Bottler('bob the bottler')

the_barrel_maker = BarrelMaker('Jenn the Cooper')

the_farmer = Farmer('Andi')

def ferment(grains):
    pass

def distill(spirits):
    pass

def main():
    #get grains from the farmer
    my_grains = the_farmer.make_grain_order('corn', 'rye', 'malt')

    #ferment etc
    spirits = ferment(my_grains)
    baby_bourbon = distill(spirits)
    #put in barrels
    my_barrels = the_barrel_maker.make_barrel_order(50)
    aged_bourbon = my.barrels.age(baby_bourbon)
    #put in bottles
    my_bottles a_bottler.get_bottles(250)
    my_bottles.store(aged_bourbon)
    