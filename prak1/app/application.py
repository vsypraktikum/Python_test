import cherrypy
import json
from .view import View_cl
from .database import Database_cl


class Application_cl(object):


#-----------------------------------------
    def __init__(self):
#-----------------------------------------
        self.view_o = View_cl()
        self.db_o = Database_cl()
#-----------------------------------------

    @cherrypy.expose
    #--------------------------------------------
    def index(self):
    #--------------------------------------------

        return self.createList_p()

    @cherrypy.expose
    #-------------------------------------------
    def createList_p(self):
    #-------------------------------------------
        data_o = self.db_o.read_px()
        return self.view_o.createList_px(data_o)


    #-------------------------------------------
    def createList_ma(self, id = None):
    #-------------------------------------------

        if id == None:
            data_ma = self.db_o.read_mitarbeiter_px()

            return self.view_o.createList_mitarbeiter(data_ma)
        else:
            data_rel = self.db_o.read_relation_px(id)
            data_ma = {}

            for ma in data_rel:
                data_ma[ma] = self.db_o.read_mitarbeiter_px(ma)

            return self.view_o.createList_mitarbeiterRel(data_ma)


    #-------------------------------------------
    def createList_maRel(self):
    #-------------------------------------------
        data_ma = self.db_o.read_px()

        return self.view_o.createList_mitarbeiter(data_ma)


    #-------------------------------------------
    def createList_ku(self):
    #-------------------------------------------
        data_ku = self.db_o.read_kunde_px()

        return self.view_o.createList_kunde(data_ku)


    @cherrypy.expose
    #-------------------------------------------
    def mitarbeiterAnzeigen(self, id= None):
    #-------------------------------------------
        if id != None:
            return self.createList_ma(id)
        else:
            return self.createList_ma()


    @cherrypy.expose
    #-------------------------------------------
    def kundenAnzeigen(self, id= None):
    #-------------------------------------------
        if id != None:
            pass
        else:
            return self.createList_ku()




    #-------------------------------------------
    @cherrypy.expose
    #-------------------------------------------
    def delete(self, id):
    #-------------------------------------------

        self.db_o.delete_px(id)
        return self.createList_p()


    #-------------------------------------------
    @cherrypy.expose
    #-------------------------------------------
    def deleteKu(self, id):
    #-------------------------------------------
        print("------------------------------------------------------")
        print(id)
        print("------------------------------------------------------")
        self.db_o.delete_Ku(id)
        return self.createList_ku()

    @cherrypy.expose
    #-------------------------------------------
    def deleteMa(self, id):
    #-------------------------------------------
        print("------------------------------------------------------")
        print(id)
        print("------------------------------------------------------")
        self.db_o.delete_Ma(id)
        return self.mitarbeiterAnzeigen()

    @cherrypy.expose


    def editMa(self,id):

        return self.createForm_ma(id)

    @cherrypy.expose
    #++++++++++++++++++++++++++++++++++++++++++++
    def editProjekt(self,id):
    #-----------------------------------------
        print(id)
        return self.createForm_pro(id)

    @cherrypy.expose
    def editKunde(self,id):

        return self.createForm_ku(id)



    def createForm_ma(self, id_spl = None):
        if id_spl != None:
            data_o = self.db_o.read_mitarbeiter_px(id_spl)
        else:
            data_o = self.db_o.read_px(id_spl)

        return self.view_o.createForm_ma(id_spl, data_o)



    def createForm_ku(self, id_spl = None):
        if id_spl != None:
            data_o = self.db_o.read_kunde_px(id_spl)
        else:
            data_o = self.db_o.read_kunde_px(id_spl)

        return self.view_o.createForm_ku(id_spl, data_o)




    def createForm_pro(self, id_spl = None):
        if id_spl != None:
            data_o =self.db_o.read_px(id_spl)
            data_ma = self.db_o.read_mitarbeiter_px()
            print("datensatz nach lesen von einzelsatz für neues proj")
            print(data_ma)
            print("asdasdasd")
        else:
            data_o = self.db_o.createNewPro(data = None)
            data_ma = self.db_o.self.db_o.read_mitarbeiter_px()


        return self.view_o.createForm_pro(id_spl, data_o, data_ma)


    @cherrypy.expose
	#-------------------------------------------------------
    def save(self, **data_opl):
	#-------------------------------------------------------

        id_s = data_opl["id_s"]
        data_a = [ data_opl["Nummer"]
        , data_opl["Bezeichnung"]
        , data_opl["Bearbeitungszeitraum"]
        , data_opl["Budget"]
        , data_opl["Kunde"]
        #, data_opl["Mitarbeiter"]
        ]
        data_rel = (data_opl["selected"])#ids der mitarbeiter]
        print("data relAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        print (data_rel)
        #noch checkbox auswerten in eigenes data und in relation.json speichern nur wie
        if id_s != "None":
            self.db_o.update_relation(id_s, data_rel)
            self.db_o.update_projekte(id_s, data_a)
        else:
			# Create-Operation
            id_s = self.db_o.create_px(data_a)

        return self.index()#.createForm_p(id_s)


    @cherrypy.expose
	#-------------------------------------------------------
    def saveMa(self, **data_opl):
	#-------------------------------------------------------

        id_s = data_opl["id_s"]
        data_a = [ data_opl["Name"]
        , data_opl["Vorname"]
        , data_opl["Funktion"]

        ]
        if id_s != "None":

            self.db_o.update_ma(id_s, data_a)
        else:
			# Create-Operation
            id_s = self.db_o.create_px(data_a)

        return self.mitarbeiterAnzeigen()#.createForm_p(id_s)


    @cherrypy.expose
	#-------------------------------------------------------
    def saveKu(self, **data_opl):
	#-------------------------------------------------------

        id_s = data_opl["id_s"]
        data_a = [ data_opl["Nummer"]
        , data_opl["Bezeichnung"]
        , data_opl["Ansprechpartner"]
        , data_opl["Ort"]

        ]
        if id_s != "None":

            self.db_o.update_Ku(id_s, data_a)
        else:
			# Create-Operation
            id_s = self.db_o.create_px(data_a)

        return self.kundenAnzeigen()#.createForm_p(id_s)




    @cherrypy.expose
    def proAnlegen(self):
        #print('geht los')
        if self.db_o.read_mitarbeiter_px() == {}:
            print("keine mitarbeiter")
            return self.index()
        else:
            id = self.db_o.createNewPro()
            data= self.db_o.read_px(str(id))
            data_ma = self.db_o.read_mitarbeiter_px()

        #print('vor return index')
        #print('id kommt jetzt die zurückgegeben wird')

        return self.view_o.createForm_pro(id , data , data_ma)


    @cherrypy.expose
    def MaAnlegen(self):
        #print('geht los')
        id = self.db_o.createNewMa()
        data= self.db_o.read_mitarbeiter_px(str(id))
        print(data)

        #print('vor return index')
        #print('id kommt jetzt die zurückgegeben wird')

        return self.view_o.createForm_ma(id , data)

    @cherrypy.expose
    def KuAnlegen(self):
        #print('geht los')
        id = self.db_o.createNewKu()
        data= self.db_o.read_kunde_px(str(id))
        print(data)

        #print('vor return index')
        #print('id kommt jetzt die zurückgegeben wird')

        return self.view_o.createForm_ku(id , data)
# EOF
