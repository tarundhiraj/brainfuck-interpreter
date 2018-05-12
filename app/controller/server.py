import cherrypy

from app.backend.brainfuck_interpreter import BrainfuckProgram
from app.backend.neatify import Neatify

'''
@author: tdhiraj, sohilladhani
'''


# This class renders the html page of the interpreter.
class UI(object):
    @cherrypy.expose
    def index(self):
        return open('../ui/index.html')


# This class will expose functionalities via REST API

@cherrypy.expose
class InterpreterWebService(object):
    @cherrypy.tools.accept(media='text/plain')
    def POST(self):
        bf_source_code = cherrypy.request.body.read(int(cherrypy.request.headers['Content-Length']))
        return BrainfuckProgram(bf_source_code).run()


@cherrypy.expose
class FormatterWebService(object):
    @cherrypy.tools.accept(media='text/plain')
    def POST(self):
        src_code = cherrypy.request.body.read(int(cherrypy.request.headers['Content-Length']))
        formatter = Neatify()
        formatted_code = formatter.format(src_code)
        return formatted_code


if __name__ == '__main__':
    webapp = UI()
    webapp.interpreter = InterpreterWebService()
    webapp.formatter = FormatterWebService()

    # chosen as per the user's will
    cherrypy.config.update('server.conf')

    # Open app.conf for app related configuration
    cherrypy.quickstart(webapp, '/', 'app.conf')
