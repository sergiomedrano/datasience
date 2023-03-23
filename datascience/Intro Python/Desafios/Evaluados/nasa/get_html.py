from string import Template

def build_web_page(fotos):
    html_template = Template('''<!DOCTYPE html>
    <html>
        <head>
            <title>NASA</title>
        </head>
        <body>
            <ul>
                $imagenes
            </ul>
        </body>
    </html>
    ''')
    
    imagenes = ''
    [imagenes := imagenes + Template('<li><img src="$url" width="20%"></li>').substitute(url = f) for f in fotos]
        
    return html_template.substitute(imagenes = imagenes)