import os 
import os.path 
import codecs
import json

from .status import *

class Database(object):

	def __init__(self, workingDir):

	   self.workingDir_s = workingDir
	   self.dataDir_s = os.path.join(workingDir, 'data')

	def read_Page(self):

	   status = NOTFOUND_K
	   data = None
	   try:
	      with codecs.open(os.path.join(self.dataDir_s,'data'), 'r', 'utf-8') as file_o:
	         data = json.load(file_o)
	         status = OK_K
	   except:
	      pass

	   return status,data


	def create_Page(self,bezeichnung_s = "", ap_s = "", id_s = "", nummer_s = "", ort_s = ""):

	   data = {
	      'bezeichnung': bezeichnung_s,
	      'ap': ap_s,
	      'id_s': id_s,
	      'nummer': nummer_s,
	      'ort': ort_s
	   }
	   file_o = codecs.open(os.path.join(self.dataDir_s,'data'), 'w', 'utf-8')
	   json.dump(data, file_o, indent=5)
	   file_o.close()

	   return data

	def update_Page(self, bezeichnung_s, ap_s, id_s, nummer_s, ort_s):

	   return self.create_Page(bezeichnung_s, ap_s, id_s, nummer_s, ort_s)




