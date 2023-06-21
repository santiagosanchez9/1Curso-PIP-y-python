import read_final
import charts_final
import utils_final


def run():
    data = read_final.read_csv('data.csv')
    data = list(filter(lambda z: z['Continent'] == 'South America', data))  # filtaremos por continente para que la visualización sea más fácil

    countries = list(map(lambda x: x['Country/Territory'], data))   # tomamos los datos de la columna de country y generamos una lista
    percentages = list(map(lambda y: y['World Population Percentage'], data))  # lo mismo con los porcetajes de la población
    charts_final.generate_pie_chart(countries, percentages)

    country = input('Type Country: ')     # selecionar el país que queremos graficar

    result = utils_final.population_by_country(data, country)   # el resultado donde vamos a pedir el país a partir de 'data'

    if len(result) > 0:   # esta condición debido a que si el resultado de encontrar un país es cero, quiere decir que no encontró el país
        country = result[0]
        labels, values = utils_final.get_population(country)  # acá se arma el diccionario de año y población
        charts_final.generate_bar_chart(country['Country/Territory'], labels, values)  # Acá agregamos el country al inicio porque así queremos que se llame la imagen



if __name__ == '__main__':
    run()
