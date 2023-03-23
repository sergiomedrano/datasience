from get_html import build_web_page

def imprimir_fotos(foto):
    with open('fotos_rovers.html', 'w') as f:
        f.write(build_web_page([f['img_src'] for f in foto]))
