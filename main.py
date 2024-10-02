import pandas as pd
from obtener_datos import obtener_datos
from procesar_datos import procesar_convocatorias

def main():
    # Lista de URLs a procesar
    carrera = input('Ingrese carrera(solo una palabra): ')
    base = 'https://www.practicas.pe/resultados-busqueda.php?'

    url_1 = base + 'q=' + carrera + '&dep=0'
    url_2 = base + 'page=2&sort=1-fecha_publicacion&q=' + carrera + '&dep=0'

    urls = [url_1, url_2]

    # Inicializar DataFrame vacío
    df = pd.DataFrame()

    # Procesar cada URL y concatenar los resultados
    for url in urls:
        convocatorias = obtener_datos(url)
        if convocatorias:
            df_convocatorias = procesar_convocatorias(convocatorias)
            df = pd.concat([df, df_convocatorias], ignore_index=True)

    # Convertir la columna 'Postula hasta' a formato datetime
    df['Postula hasta'] = pd.to_datetime(df['Postula hasta'], dayfirst=True)
    df['Postula hasta'] = df['Postula hasta'].dt.strftime('%d/%m/%Y')
    
    # Imprimir información
    print(df['Empresa'].value_counts())
    print('\n', df['Ubicación'].value_counts())
    print('\n', df['Subvención'].value_counts())
    print('\n', df['Detalle'].value_counts().to_string())
    print('\n Archivo completo: \n','\n', df[['Empresa','Ubicación','Detalle','Subvención','Postula hasta']].sort_values('Postula hasta').to_string())

    print('\n Links: \n','\n', df[['Link']].to_string())

if __name__ == "__main__":
    main()
