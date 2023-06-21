import csv

def read_csv(path):   
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',') 
        header = next(reader) 
        data = []    # puedo agregar una lista vacia data, donde se guarde el diccionario en cada iteración
        for row in reader:
            iterable = zip(header, row)  

            country_dict = {key: value for key, value in iterable}  
            data.append(country_dict)  # creamos una lista de los diccionarios creados en la iteración de country_dict que podemos consultar con elel nombre de la columna
        return data # un return porque el finultimo es que los datos se guarden en data y debemos mostrarlo


'''También deseo correr el archivo como un script, es decir, poder hacerlo desde la terminal, por lo cual hacemos: '''

if __name__ == '__main__':
    data = read_csv('./app/data.csv')
    print(data[0])