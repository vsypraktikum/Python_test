import os
import os.path
import codecs

import json
#-----------------------------------------------------
class Database_cl(object):
    #--------------------------------------------------

    def __init__(self):
        self.data_ku= None
        self.data_ma= None
        self.data_o= None
        self.data_rel= None
        self.readData_p()
        self.readData_mitarbeiter_p()
        self.readData_kunde_p()
        self.readData_rel_p()




#--------------------------------------------------------
    def read_px(self, id_spl = None):
#--------------------------------------------------------

        data_o = None
        if id_spl == None:
            data_o = self.data_o
        else:
            if id_spl in self.data_o:
                data_o = self.data_o[id_spl]

        return data_o


#--------------------------------------------------------
    def read_kunde_px(self, id_spl = None):
#--------------------------------------------------------

        data_ku = None
        if id_spl == None:
            data_ku = self.data_ku
        else:
            if id_spl in self.data_ku:
                data_ku = self.data_ku[id_spl]

        return data_ku
#--------------------------------------------------------
    def read_relation_px(self, id_spl = None):
#--------------------------------------------------------
        print("id bei mitarbeiter anzeigen AAAAAAAAAAAAAMKasdasdasdasd")
        print(id_spl)
        data_rel = None
        if id_spl == None:
            data_rel = self.data_rel
            print("id lieder leer")
        else:
            if id_spl in self.data_rel:
                print("hier ist data rel nach reaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaad")
                print(self.data_rel[id_spl])
                data_rel = self.data_rel[id_spl]
                print("hier ist data rel nach reaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaad")

        return data_rel


#--------------------------------------------------------
    def read_mitarbeiter_px(self, id_spl = None):
#--------------------------------------------------------

        data_ma = None
        if id_spl == None:
            data_ma = self.data_ma

        else:
            if id_spl in self.data_ma:
                data_ma = self.data_ma[id_spl]

        return data_ma

#--------------------------------------------------------
    def readData_p(self):
#--------------------------------------------------------

        try:
            fp_o = codecs.open(os.path.join('data', 'projekte.json'), 'r', 'utf-8')
        except:

            self.data_o = {}

            self.saveData_p()

        else:
            with fp_o:
                self.data_o = json.load(fp_o)

        return

#--------------------------------------------------------
    def readData_rel_p(self):
#--------------------------------------------------------

        try:
            rel_o = codecs.open(os.path.join('data', 'relation.json'), 'r', 'utf-8')
        except:

            self.data_rel = {}

            self.saveData_rel()

        else:
            with rel_o:
                self.data_rel = json.load(rel_o)
                print("data in data_rel nach read")
                print(self.data_rel)
        return

#--------------------------------------------------------
    def readData_mitarbeiter_p(self):
#--------------------------------------------------------

        try:
            ma_o = codecs.open(os.path.join('data', 'mitarbeiter.json'), 'r', 'utf-8')
        except:
            self.data_ma = {}

            self.saveData_ma()


        else:
            with ma_o:
                self.data_ma = json.load(ma_o)


        return


#--------------------------------------------------------
    def readData_kunde_p(self):
#--------------------------------------------------------

        try:
            ku_o = codecs.open(os.path.join('data', 'kunde.json'), 'r', 'utf-8')
        except:
            self.data_ku = {}

            self.saveData_ku()


        else:
            with ku_o:
                self.data_ku = json.load(ku_o)


        return
#--------------------------------------------------------
    def saveData_p(self):
#--------------------------------------------------------
        with codecs.open(os.path.join('data', 'projekte.json'), 'w', 'utf-8') as fp_o:
            json.dump(self.data_o, fp_o)

#--------------------------------------------------------
    def saveData_ku(self):
#--------------------------------------------------------
        with codecs.open(os.path.join('data', 'kunde.json'), 'w', 'utf-8') as ku_o:
            json.dump(self.data_ku, ku_o)

#--------------------------------------------------------
    def saveData_ma(self):
#--------------------------------------------------------
        with codecs.open(os.path.join('data', 'mitarbeiter.json'), 'w', 'utf-8') as ma_o:
            json.dump(self.data_ma, ma_o)

#--------------------------------------------------------
    def saveData_rel(self):
#--------------------------------------------------------
        with codecs.open(os.path.join('data', 'relation.json'), 'w', 'utf-8') as rel_o:
            json.dump(self.data_rel, rel_o)


#---------------------------------------------------------
    def delete_px(self, id_spl):
#---------------------------------------------------------

        if id_spl in self.data_o:
            del self.data_o[id_spl]
            del self.data_rel[id_spl]
            #self.data_o[id_spl] = self.getDefault_px()
            self.saveData_p()
            self.saveData_rel()
        return 

#---------------------------------------------------------
    def delete_Ma(self, id_spl):
#---------------------------------------------------------
        status_b = False
        if id_spl in self.data_ma:
            del self.data_ma[id_spl]

            self.saveData_ma()
        return status_b


#---------------------------------------------------------
    def delete_Ku(self, id_spl):
#---------------------------------------------------------
        status_b = False
        print(self.data_ku)
        del self.data_ku[id_spl]
        #print(self.data_ku[id_spl])
            #self.data_o[id_spl] = self.getDefault_px()
        self.saveData_ku()
        return status_b



	#-------------------------------------------------------
    def update_projekte(self, id_spl, data_opl):
	#-------------------------------------------------------
		# Überprüfung der Daten müsste ergänzt werden!
        status_b = False
        if id_spl in self.data_o:

            self.data_o[id_spl] = {
                'Nummer': data_opl[0],
                'Bezeichnung': data_opl[1],
                'Bearbeitungszeitraum': data_opl[2],
                'Budget': data_opl[3],
                'Kunde': data_opl[4],
                #'Mitarbeiter': data_opl[5]
                }
            self.saveData_p()
            status_b = True


        return status_b
	#-------------------------------------------------------
    def update_ma(self, id_spl, data_opl):
	#-------------------------------------------------------
		# Überprüfung der Daten müsste ergänzt werden!
        status_b = False
        if id_spl in self.data_ma:

            self.data_ma[id_spl] = {
                'Name': data_opl[0],
                'Vorname': data_opl[1],
                'Funktion': data_opl[2],
                }
            self.saveData_ma()
            status_b = True


        return status_b

	#-------------------------------------------------------
    def update_Ku(self, id_spl, data_opl):
	#-------------------------------------------------------
		# Überprüfung der Daten müsste ergänzt werden!
        status_b = False
        if id_spl in self.data_ku:

            self.data_ku[id_spl] = {
                'Nummer': data_opl[0],
                'Bezeichnung': data_opl[1],
                'Ansprechpartner': data_opl[2],
                'Ort': data_opl[2],
                }
            self.saveData_ku()
            status_b = True


        return status_b


	#-------------------------------------------------------
    def update_relation(self, id_spl, data_opl):
	#-------------------------------------------------------
		# Überprüfung der Daten müsste ergänzt werden!
        status_b = False

        self.data_rel[id_spl] = data_opl

        self.saveData_rel()
        status_b = True


        return status_b



    def createNewPro(self):
        data = self.read_px()
        count = 0
        while str(count) in data:
            count+=1
            if str(count) not in data:

                break

        status_b = False
        self.data_o[str(count)] = {
            'Nummer': '',
            'Bezeichnung': '',
            'Bearbeitungszeitraum': '',
            'Budget': '',
            'Kunde': '',
            #'Mitarbeiter': ''
            }
        status_b = True
        return count



    def createNewMa(self):
        data = self.read_mitarbeiter_px()
        count = 0
        while str(count) in data:
            count+=1

            if str(count) not in data:
                break

        status_b = False
        self.data_ma[str(count)] = {
            'Name': '',
            'Vorname': '',
            'Funktion': '',
            }

        status_b = True
        return count




    def createNewKu(self):
        data = self.read_kunde_px()
        count = 0
        while str(count) in data:
            count+=1

            if str(count) not in data:
                break

        status_b = False
        self.data_ku[str(count)] = {
            'Nummer': '',
            'Bezeichnung': '',
            'Ansprechpartner': '',
            'Ort': '',
            }

        status_b = True
        print('data in createkunde')
        print(self.data_ku[str(count)])
        return count





# EOF
