def get_description(): #смотрите строку документации
    ''' Return random weather, just like the pros '''
    from random import choise
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return choise(possibilities)
