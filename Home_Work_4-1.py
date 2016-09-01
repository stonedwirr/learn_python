animal = 'fruitbat'
def print_global():
    #print('inside print_global:', animal)
    animal = 'wombat'
    print('inside print_global:', animal)
print('at the top level:', animal)
print_global()
