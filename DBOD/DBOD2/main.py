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
            <form autocomplete="off" method="get" action="func">
              <input type="text" name="num" placeholder="token"/>
              <br>
              <select name="dbodt">
               <option value="dbod_minecraft">Minecraft</option>
               <option value="dbod_image">basic</option>
              </select>
              <br>
              <input type="text" name="pref" placeholder="prefix"/>
              <button type="submit">create</button>
            </form>
            </p>
          </body>
        </html>"""

    @cherrypy.expose
    def func(self, num, pref, dbodt):
        createbot(num, pref, dbodt)
        return "Your bot has been created."

if __name__ == '__main__':
   cherrypy.config.update({'server.socket_host': '0.0.0.0'})
   cherrypy.quickstart(application())
