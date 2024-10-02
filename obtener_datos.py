import requests
from bs4 import BeautifulSoup

def obtener_datos(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        convocatorias = soup.find_all('article', class_='convocatoria')
        return convocatorias
    else:
        print('Error al realizar la solicitud:', response.status_code)
        return None
