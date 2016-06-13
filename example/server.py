#!/usr/bin/env python

from livereload import Server, shell
server = Server()
dirs = ("app/templates", "build")
server.watch("app/templates/*.html",
             shell(["bagel", "--file-type", "html", dirs[0], dirs[1]]))
server.watch("app/static/*.css", shell("rsync -a app/static/ build"))
server.serve(root=dirs[1], port=8080, host="localhost", open_url=True)
