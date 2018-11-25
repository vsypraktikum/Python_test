import codecs
import os.path
import string
import mako

from mako.template import Template
from mako.lookup import TemplateLookup

#------------------------------------------
class View_cl(object):
#------------------------------------------

    #----------------------------------------------
    def __init__(self):
    #----------------------------------------------
        self.path_s = "/home/till/Dokumente/prak1/template/"
        self.lookup_o = TemplateLookup(directories=self.path_s)

    #----------------------------------------------
    def createList_px(self, data_opl):
    #----------------------------------------------

        markup_s=''
        markup_s += self.readFile_p('list0.tpl')
        markup_s += self.create_p('list1.tpl', data_opl)
        markup_s += self.readFile_p('list2.tpl')

        return markup_s

    #----------------------------------------------
    def createList_mitarbeiter(self, data_opl):
    #----------------------------------------------
        markup_s=''
        markup_s += self.readFile_p('ma_list0.tpl')
        markup_s += self.create_m('ma_list1.tpl', data_opl)
        markup_s += self.readFile_p('ma_list2.tpl')

        return markup_s


    #----------------------------------------------
    def createList_mitarbeiterRel(self, data_opl):
    #----------------------------------------------
        markup_s=''
        markup_s += self.readFile_p('ma_list0.tpl')
        markup_s += self.create_m('ma_list1.tpl', data_opl)
        markup_s += self.readFile_p('ma_list2.tpl')

        return markup_s

    #----------------------------------------------
    def createList_kunde(self, data_opl):
    #----------------------------------------------

        markup_s=''
        markup_s += self.readFile_p('ku_list0.tpl')
        markup_s += self.create_p('ku_list1.tpl', data_opl)
        markup_s += self.readFile_p('ku_list2.tpl')

        return markup_s


    #---------------------------------------------
    def readFile_p(self, fileName_spl):
    #---------------------------------------------
        content_s=''
        with codecs.open(os.path.join('template', fileName_spl), 'r' , 'utf-8') as fp_o:
            content_s = fp_o.read()

        return content_s
    #---------------------------------
    def createForm_px(self, id, data_opl):
    #------------------------------------

        markup_s = ''
        markup_s += self.readFile_p('form0.tpl')
        markupV_s = self.readFile_p('form1.tpl')
        lineT_o = string.Template(markupV_s)

        markup_s += lineT_o.safe_substitute(Nummer=data_opl[0]
        , Bezeichnung=data_opl[1]
        , Bearbeitungszeitraum=data_opl[2]
        , Budget=data_opl[3]
        , Kunde=data_opl[4]
        #, Mitarbeiter=data_opl[5]
        , id_s=count
        )

        markup_s += self.readFile_p('form2anlegen.tpl')
        return markup_s


	#-------------------------------------------------------
    def createForm_pro(self, id_spl, data_opl, data_ma = None):
	#-------------------------------------------------------


        markup_s = ''
        markup_s += self.readFile_p('form0.tpl')
        markupV_s = self.readFile_p('form1.tpl')
        print("-------------------------------------------------------------")
        print(data_ma)

        markup_s += self.create_m('ma_list_pro.tpl', data_ma)
        lineT_o = string.Template(markupV_s)
        markup_s += lineT_o.safe_substitute(Nummer=data_opl['Nummer']
        , Bezeichnung=data_opl['Bezeichnung']
        , Bearbeitungszeitraum=data_opl['Bearbeitungszeitraum']
        , Budget=data_opl['Budget']
        , Kunde=data_opl['Kunde']
        #, Mitarbeiter=data_opl['Mitarbeiter']
        , id_s=id_spl
        )

        markup_s += self.readFile_p('form2.tpl')
        return markup_s


	#-------------------------------------------------------
    def createForm_ku(self, id_spl, data_opl):
	#-------------------------------------------------------


        markup_s = ''
        markup_s += self.readFile_p('ku_form0.tpl')
        markupV_s = self.readFile_p('ku_form1.tpl')
        lineT_o = string.Template(markupV_s)
        markup_s += lineT_o.safe_substitute(Nummer=data_opl['Nummer']
        , Bezeichnung=data_opl['Bezeichnung']
        , Ansprechpartner=data_opl['Ansprechpartner']
        , Ort=data_opl['Ort']

        , id_s=id_spl
        )

        markup_s += self.readFile_p('ku_form2.tpl')
        return markup_s

	#-------------------------------------------------------
    def createForm_ma(self, id_spl, data_opl):
	#-------------------------------------------------------


        markup_s = ''
        markup_s += self.readFile_p('ma_form0.tpl')
        markupV_s = self.readFile_p('ma_form1.tpl')
        lineT_o = string.Template(markupV_s)
        markup_s += lineT_o.safe_substitute(Name=data_opl['Name']
        , Vorname=data_opl['Vorname']
        , Funktion=data_opl['Funktion']
        , id_s=id_spl
        )

        markup_s += self.readFile_p('ma_form2.tpl')
        return markup_s


    def create_p(self, template_spl, data_opl):
        print("BBBBBBBBBBBBB")
        print (data_opl)
        template_o = self.lookup_o.get_template(template_spl)
        markup_s = template_o.render(data_o = data_opl)
        return markup_s
   #-------------------------------------------------------

    def create_m(self, template_spl, data_ma):
        template_o = self.lookup_o.get_template(template_spl)
        markup_s = template_o.render(data_ma = data_ma)
        return markup_s
