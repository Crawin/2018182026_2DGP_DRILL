table = {
    'SLEEP' :{'HIT':'WAKE'},
    'WAKE' : {'TIMER10':'SLEEP'}
}

cur_state = 'SLEEP'
print(table[cur_state]['HIT'])
print(table['WAKE']['TIMER10'])