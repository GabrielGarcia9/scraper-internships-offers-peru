import pandas as pd

def procesar_convocatorias(convocatorias):
    empresas = []
    practicantes_de = []
    ubicacion = []
    subvencion = []
    postula_hasta = []
    detalle = []
    link = []

    base_url = 'https://www.practicas.pe/'

    for convocatoria in convocatorias:
        # Empresa
        empresa = convocatoria.find('h3').text.strip()
        # print("\nEmpresas:\n", empresa)
        empresas.append(empresa)
        

        # Practicantes de
        practicantes = convocatoria.find('p', class_='resaltar').find_next('p').text.strip()
        # print("\nPracticantes:\n", practicantes)
        practicantes_de.append(practicantes)
        

        # Ubicación
        lugar = convocatoria.find('div', class_='lugar').text.strip()
        # print("\nLugar:\n", lugar)
        ubicacion.append(lugar)
        

        # Detalle
        departamento_texto = '-'.join(convocatoria.find('a', class_='enlace1')['href'].split('-')[3:7])
        # print("\nDepartamento:\n", departamento_texto)
        detalle.append(departamento_texto)
        

        # Subvención
        subvencion_texto = convocatoria.find('div', class_='info').find_next('div', class_='info').find_next('div', class_='info').text.strip()
        # print("\nSubvencion:\n", subvencion_texto)
        subvencion.append(subvencion_texto)
        

        # Postula hasta
        info_divs = convocatoria.find_all('div', class_='info')
        

        if len(info_divs) > 0 and 'Finaliza el ' in info_divs[-1].text:
            postula_hasta_texto = info_divs[-1].text.split('Finaliza el ')[1].strip()

        # print("\nFecha:\n", postula_hasta_texto)
        postula_hasta.append(postula_hasta_texto)

        

        # Link
        link_texto = '-'.join(convocatoria.find('a', class_='enlace1')['href'].split('-')[::])
        # print("\nlink_texto:\n", link_texto)
        full_url = base_url + link_texto    
        link.append(full_url)


    return pd.DataFrame({
        'Empresa': empresas,
        'Practicantes de': practicantes_de,
        'Ubicación': ubicacion,
        'Detalle': detalle,
        'Subvención': subvencion,
        'Postula hasta': postula_hasta,
        'Link': link
    })
