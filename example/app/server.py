#!/usr/bin/env python

from livereload import Server, shell
server = Server()
dirs = ("templates", "../build")
server.watch("templates/*.html",
             shell(["bagel", "--file-type", "html", dirs[0], dirs[1]]))
server.watch("app/static/*.css", shell("rsync -a static/ ../build"))
server.serve(root=dirs[1], port=8080, host="localhost", open_url=True)
