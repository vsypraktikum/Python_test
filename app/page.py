# coding: utf-8

import cherrypy
from .status import *

#----------------------------------------------------------
class Page(object):
#----------------------------------------------------------

   #-------------------------------------------------------
   def __init__(self, db_opl, view_opl):
   #-------------------------------------------------------
      self.db_o = db_opl
      self.view_o = view_opl

   #-------------------------------------------------------
   @cherrypy.expose
   def view(self, title_spl):
   #-------------------------------------------------------
      # angeforderte Seite im View-Modus liefern
      # falls Seite nicht existiert, neu anlegen

      status_i, data_o = self.db_o.read_Page()
      if status_i == NOTFOUND_K:
         data_o = self.db_o.create_Page(title_spl)

      markup_s = self.view_o.erfassen_Page(data_o)

      return markup_s

   #-------------------------------------------------------
   @cherrypy.expose
   def edit(self, title_spl):
   #-------------------------------------------------------
      # angeforderte Seite im Edit-Modus liefern
      # falls Seite nicht existiert, neu anlegen

      status_i, data_o = self.db_o.read_Page()
      if status_i == NOTFOUND_K:
         data_o = self.db_o.create_Page(title_spl)

      markup_s = self.view_o.erfassen_Page(data_o)

      return markup_s

   #-------------------------------------------------------
   @cherrypy.expose
   def save(self,bezeichnung, ap, id_s, nummer, ort):
   #-------------------------------------------------------
      # Änderungen speichern
      # Seite mit neuem Titel anlegen oder aktualisieren
      status_i, data_o = self.db_o.read_Page()
      if status_i == NOTFOUND_K:
         # dürfte hier nicht auftreten, da save nur vom edit-Modus aus ausgeführt werden kann
         data_o = self.db_o.create_Page(bezeichnung, ap, id_s, nummer, ort)
      else:
         data_o = self.db_o.update_Page(bezeichnung, ap, id_s, nummer, ort)

      #if oldTitle != title:
         # alte Seite entfernen
         # TODO: Fehlerbehandlung
         #self.db_o.pageDelete_px(oldTitle)

      markup_s = self.view_o.erfassen_Page(data_o)

      return markup_s

   #-------------------------------------------------------
   @cherrypy.expose
   def delete(self, title_spl):
   #-------------------------------------------------------
      # Seite entfernen, root-Seite zurückliefern

      if title_spl != 'root':
         status_i = self.db_o.pageDelete_px(title_spl)
         if status_i == OK_K:
            data_o = self.db_o.pageRead_px(ROOTPAGE_K)
         else:
            data_o = self.db_o.pageRead_px(title_spl)
      else:
         data_o = self.db_o.pageRead_px(ROOTPAGE_K)

      markup_s = self.view_o.viewPage_px(data_o)

      return markup_s

# EOF
