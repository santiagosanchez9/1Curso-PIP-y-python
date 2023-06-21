'''El resto está en obtener de data el crecimiento poblacional a través de los años, esto partiendo de la información que ya
 tenemos como diccionario. De dicha información tendremos que transformar el diccionario.'''

# Vamos a usar esa función
def get_population(country_dict):    # la data será el país que seleccionamos en forma de diciconario
    
    # cómo seleccionamos las columnas que son los años?
    population_dict = {       # vamos a crear manualmente los años:
    '2022': int(country_dict['2022 Population']),    # ahora podemos seleccionar el nombre de las columnas
    '2020': int(country_dict['2020 Population']),
    '2015': int(country_dict['2015 Population']),     
    '2010': int(country_dict['2010 Population']),      # tenemos que decirle que son enteros (int) ya que cuando lee el csv entiende string
    '2000': int(country_dict['2000 Population']),
    '1990': int(country_dict['1990 Population']),
    '1980': int(country_dict['1980 Population']),
    '1970': int(country_dict['1970 Population'])
    }
    
    labels = population_dict.keys() 
    values = population_dict.values()         # el return debe ser un array de los valores y un array de los labels
    return labels, values

def population_by_country(data, country): #Los parámetros de entrada son la información con los países y luego el país que quiero saber
    result = list(filter(lambda item: item['Country/Territory'] == country, data))
    return result