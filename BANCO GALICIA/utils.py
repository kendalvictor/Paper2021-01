def get_schedule(val):
    if val < 6:
        return 'madrugada'
    elif val < 9:
        return 'antes_del_trabajo'
    elif val < 13:
        return 'trabajo_manana'
    elif val < 16:
        return 'almuerzo'
    elif val < 19:
        return 'trabajo_tarde'
    else:
        return 'luego_del_trabajo'
    
def get_day_cut(val):
    if val < 7:
        return 'inicio_mes'
    elif val < 13:
        return '7_12'
    elif val < 18:
        return 'quincena'
    elif val < 25:
        return '18_24'
    else:
        return 'fin_de_mes'
    
def get_trimestre(val):
    if val <= 3:
        return 1
    elif val <= 6:
        return 2
    elif val <= 9:
        return 3
    elif val <= 12:
        return 4
    return 0