from string import Template
from get_html import obtener_html

def imprimir_pajaro(pajaro):
    body = ''
    
    for p in pajaro:
        img_template = Template('<img src="$url">')
        nombre_es_template = Template('<p>Español: $nombre_esp</p>')
        nombre_en_template = Template('<p>Inglés: $nombre_eng</p>')
        
        texto_img = img_template.substitute(url = p['images']['main'])
        nombre_es = nombre_es_template.substitute(nombre_esp = p['name']['spanish'])
        nombre_en = nombre_en_template.substitute(nombre_eng = p['name']['english'])
    
        body += texto_img+nombre_es+nombre_en+'<br>'
    
    #html = obtener_html().substitute(body = body)
    
    with open('output.html', 'w') as f:
        f.write(obtener_html().substitute(body = body))
