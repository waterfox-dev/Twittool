def create_page(name : str, *args):
    template = open(f"server/templates/{name}.html", 'x')
    script = open(f"server/static/script/{name}.js", 'x')
    style = open(f"server/static/style/{name}.css",  'x')

    template.close
    script.close
    style.close