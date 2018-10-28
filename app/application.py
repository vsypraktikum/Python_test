# coding: utf-8
import cherrypy

from .database import Database
from .view import View
from .page import Page
from .status import *
#--------------------------------------
class Application(object):

	def __init__(self,workingDir):

	  self.db = Database(workingDir)
	  self.view = View(workingDir)
	  self.page = Page(self.db, self.view)
	  pass

	@cherrypy.expose
	def index(self):
	  return self.page.view(ROOTPAGE_K)

	@cherrypy.expose
	def default(self, *arglist, **kwargs):

		msg_s = "unbekannte Anforderung:"
			#str(arglist) + \
			#''+\
			#str(kwargs)
		raise cherrypy.HTTPError(404, msg_s)
# EOF
