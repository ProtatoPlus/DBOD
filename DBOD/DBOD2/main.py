import docker
import cherrypy.process.plugins
import cherrypy
import os
from createmain import createbot
client = docker.from_env()


class application:
    @cherrypy.expose
    def index(self):
        return """<html>
          <head></head>
          <body>
            <p>Make bot<br>
            <select name="type">
             <option value="red">Minecraft</option>
             <option value="purple">Basic</option>
            </select>
            <form autocomplete="off" method="get" action="func">
              <input type="text" name="num" placeholder="token"/>
              <br>
              <input type="text" name="pref" placeholder="prefix"/>
              <button type="submit">create</button>
            </form>
            </p>
          </body>
        </html>"""

    @cherrypy.expose
    def func(self, num, pref):
        createbot(num, pref, type)
        return "Your bot has been created."

if __name__ == '__main__':
   cherrypy.config.update({'server.socket_host': '0.0.0.0'})
   cherrypy.quickstart(application())
