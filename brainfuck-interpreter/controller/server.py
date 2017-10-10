import os
import cherrypy

'''
@author: tdhiraj
'''


#This class renders the html page of the interpreter.
class UI(object):
    @cherrypy.expose
    def index(self):
        return open('../ui/index.html')
        
    @cherrypy.expose
    def add(self, num1=2, num2=3):
        return int(num1+num2)
        

#This class will expose functionalities via REST API

@cherrypy.expose
class InterpreterWebService(object):
    
    @cherrypy.tools.accept(media ='text/plain')
    
    def POST(self):
        #TODO: call interpreter
        pass

    def GET(self):
        #TODO: call the neatify functionality
        return "Interpreted"
    
if __name__ == '__main__':
    
    '''conf = {
             '/': {
                'tools.sessions.on': True,
                'tools.staticdir.root': os.path.abspath(os.getcwd())
            },
            '/interpretor': {
                'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
                'tools.response_headers.on': True,
                'tools.response_headers.headers': [('Content-Type', 'text/plain')],
            },
            '/static': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': '../ui'
            }
        }'''
          
          
    webapp = UI()
    webapp.interpreter = InterpreterWebService()
    
    #TODO: keep an option to specify the port number to the user so that port 
    #chosen as per the user's will
    cherrypy.config.update('server.conf')
    
    #Open app.conf for app related configuration
    cherrypy.quickstart(webapp, '/', 'app.conf')
          
        
    
    