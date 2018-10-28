import codecs 
import os.path 
import string

class View(object):

	def __init__(self, workingDir):

	   self.workingDir_s = workingDir
	   self.templates = {
	      'erfassen': None,
	      'liste': None,
	   }
	   markup = self.readFile('erfassen.html')
	   self.templates['erfassen'] = string.Template(markup)
	   markup = self.readFile('liste.html')
	   self.templates['liste'] = string.Template(markup)

	def erfassen_Page(self, data):

	   markup = self.templates['erfassen'].safe_substitute(
	      bezeichnung = data['bezeichnung']
	      ,ap = data['ap']
	      ,id_s = data['id_s']
	      ,nummer = data['nummer']
	      ,ort = data['ort']
	   )
	   return markup

	def readFile(self, fileName_spl):

	   content_s = ''
	   with codecs.open(os.path.join(self.workingDir_s, 'template', fileName_spl), 'r', 'utf-8') as fp_o:
	      content_s = fp_o.read()

	   return content_s

