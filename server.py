from livereload import Server, shell

def rebuild():
    print('SITE REBUILDED')
    return


rebuild()


server = Server()
server.watch('*.css', rebuild)
server.serve(root='.')