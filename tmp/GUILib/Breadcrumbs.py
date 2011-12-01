'''
Created on 18-10-2011

@author: dzk
'''

from TestStatusInfo import info, warn, fail #@UnusedImport
from SeleniumLibrary import SeleniumLibrary

class Breadcrumbs:
   '''
   Class with operations performing checking bread crums
   '''

   def __init__(self):
      self.seleniumLibrary = SeleniumLibrary()
      
   def openUrl(self, browser="ff", port="8090"):
      sel = self.seleniumLibrary._selenium
      sel.open_browser("http://localhost:%s/scrumzu" % port, browser)
      
   def openSpecyfic(self, browser="ff", port="8090", page="pbis"):
      sel = self.seleniumLibrary._selenium
      sel.open_browser("http://localhost:%s/scrumzu/%s" % (port, page), browser)

   def checkTitle(self, text):
      sel = self.seleniumLibrary._selenium
      sel.get_title = sel.is_text_present( "%s" % text )
         
         