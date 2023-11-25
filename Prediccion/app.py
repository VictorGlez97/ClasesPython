from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
from scipy.stats import poisson

app = FastAPI()
app.title = 'Prediccion'
app.version = '0.0.1'

@app.get('/', tags=['Prediccion'])
def get_prediccion():

    # BEAUTIFULSOUP
    # URL PAGINA
    url = 'https://www.sofascore.com/tournament/football/argentina/liga-profesional-de-futbol/155#47647'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    try:

        # HACER PETICION A PAGINA
        response = requests.get(url, headers=headers)
        print(response)

        # VERIFICAR SI SE PUDO ENTRAR A LA PAGINA
        if response.status_code == 200:

            # HACIENDO INSTANCIA A PLUGIN BEAUTIFULSOUP
            soup = BeautifulSoup(response.text, 'html.parser')
            # print( soup.prettify() )

            # IMPRIMIENDO TITULO DE LA PAGINA
            print('Titulo de la pagina', soup.title.text)
            
            # BUSCANDO ELEMENTOS DE PAGINA POR MEDIO DE CLASES
            items = soup.find_all('div', class_='sc-fqkvVR')
            # items = soup.find_all('a')
            # print( items )
            print( len(items) )

            # ITERANDO RESULTADO DE BUSQUEDA POR CLASES
            for item in items:
                print('Item: ', item) 

            # SCIPY
            # Definir la media (número promedio de eventos en el intervalo)
            media = 3

            # Número de eventos para el cual deseas calcular la probabilidad
            x = 2

            # Calcular la probabilidad de tener exactamente 'x' eventos
            probabilidad_exacta = poisson.pmf(x, media)

            # Calcular la probabilidad acumulativa de tener 'x' eventos o menos
            probabilidad_acumulativa = poisson.cdf(x, media)
    
    except Exception as e:

        print(e)

    return 'Hola'
