
def obtener_parametros(url):
    base, parametros = url.split('?', 1)
    parametros = parametros.split('&')
    valores = [parametro.split('=')[1] for parametro in parametros]
    
    return valores

url = "https://retosdeprogramacion.com?year=2023&challenge=0"
print(obtener_parametros(url))













