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
    url = 'https://www.sofascore.com/es/'

    # HACER PETICION A PAGINA
    response = requests.get(url)
    print(response)

    # VERIFICAR SI SE PUDO ENTRAR A LA PAGINA
    if response.status_code == 200:

        # HACIENDO INSTANCIA A PLUGIN BEAUTIFULSOUP
        soup = BeautifulSoup(response.text, 'html.parser')

        # IMPRIMIENDO TITULO DE LA PAGINA
        print('Titulo de la pagina', soup.title.text)
        
        # BUSCANDO ELEMENTOS DE PAGINA POR MEDIO DE CLASES
        items = soup.find_all(class_='sc-fqkvVR sc-dcJsrY')

        # ITERANDO RESULTADO DE BUSQUEDA POR CLASES
        for item in items:
            print('Elemento: ', item) 

        # SCIPY
        # Definir la media (número promedio de eventos en el intervalo)
        media = 3

        # Número de eventos para el cual deseas calcular la probabilidad
        x = 2

        # Calcular la probabilidad de tener exactamente 'x' eventos
        probabilidad_exacta = poisson.pmf(x, media)

        # Calcular la probabilidad acumulativa de tener 'x' eventos o menos
        probabilidad_acumulativa = poisson.cdf(x, media)
 

    return 'Hola'
