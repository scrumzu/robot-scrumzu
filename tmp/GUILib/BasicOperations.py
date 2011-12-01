'''
Created on 25-09-2011
@author: TM

''' 

from SeleniumLibrary import SeleniumLibrary
from TestStatusInfo import info, warn, fail #@UnusedImport

class BasicOperations:
   
   def __init__(self):      
      self.seleniumLibrary = SeleniumLibrary()
      
   def openBrowserWithSpectrePage(self, browser="ff", port="8080"):
      '''
      Opens default spectre page
      '''
      self.seleniumLibrary.open_browser("http://spectre.dyndns-server.com:%s/" % port, browser)
           
   def openUrl(self, url):
      '''
      Opens given url in active browser window.
      '''
      sel = self.seleniumLibrary._selenium
      sel.open('http://spectre.dyndns-server.com:8080/scrumzu/pbis')
         
   def openScrumzuAtLocalhost(self, browser="ff", port="8080"):
      '''
      Opens scrumzu at localhost
      '''
      self.seleniumLibrary.open_browser("http://localhost:%s/scrumzu" % port, browser)
      
   def closeBrowser(self):
      self.seleniumLibrary.close_all_browsers()
