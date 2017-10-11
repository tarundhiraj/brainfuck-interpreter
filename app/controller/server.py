import os
import sys
import cherrypy
from app.backend.neatify import Neatify
'''
@author: tdhiraj
'''
path = os.getcwd()

#This class renders the html page of the interpreter.
class UI(object):
    @cherrypy.expose
    def index(self):
        return open(path + '/app/ui/index.html')
        

#This class will expose functionalities via REST API

@cherrypy.expose
class InterpreterWebService(object):
    
    @cherrypy.tools.accept(media ='text/plain')
    
    def POST(self, **kwargs):
        #TODO: call interpreter
        pass

@cherrypy.expose
class FormatterWebService(object):
    @cherrypy.tools.accept(media = 'text/plain')

    def POST(self, **kwargs):
        src_code = kwargs['code'] 
        formatter = Neatify()
        formatted_code = formatter.format(src_code)
        return formatted_code

def start_server():
    webapp = UI()
    webapp.interpreter = InterpreterWebService()
    webapp.formatter = FormatterWebService()

    #TODO: keep an option to specify the port number to the user so that port 
    #chosen as per the user's will
    cherrypy.config.update(path + '/app/controller/' + 'server.conf')
    
    #Open app.conf for app related configuration
    cherrypy.quickstart(webapp, '/', path + '/app/controller/' + 'app.conf')
          
        
    
    
