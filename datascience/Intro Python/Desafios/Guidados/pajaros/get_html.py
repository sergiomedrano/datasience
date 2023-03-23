from string import Template

def obtener_html():
    html_template = Template('''<!DOCTYPE html>
    <html>
    <head>
    <title>Pájaros</title>
    </head>
    <body>
    $body
    </body>
    </html>
    ''')
    
    return html_template