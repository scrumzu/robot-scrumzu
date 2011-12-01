'''
Created on 25-09-2011
@author: TM, SP

''' 

from SeleniumLibrary import SeleniumLibrary
from TestStatusInfo import info, warn, fail #@UnusedImport
from Constants import * #@UnusedWildImport
import time
import datetime

class BasicOperations:
   
   def __init__(self):      
      self.seleniumLibrary = SeleniumLibrary()
      
   def openScrumzuAtSpectre(self, browser="ff", port=DEFAULT_PORT):
      '''
      Opens default spectre page
      '''
      self.seleniumLibrary.set_selenium_timeout(30)
      self.seleniumLibrary.open_browser("http://spectre.dyndns-server.com:%s/" % port, browser)
         
   def openScrumzuAtLocalhost(self, browser="opera", port=DEFAULT_PORT):
      '''
      Opens scrumzu at localhost
      '''
      self.seleniumLibrary.set_selenium_timeout(30)
      self.seleniumLibrary.open_browser("http://localhost:%s/scrumzu" % port, browser)

   def clickOn(self, btnId):
      sel = self.seleniumLibrary._selenium
      sel.click("css=[id='%s']" % btnId)
      time.sleep(8)
      if('submit' in btnId):
         sel.wait_for_page_to_load(DEFAULT_TIMEOUT_MS)

 
   def selectCheckbox(self, objId, onoff='on'):
      sel = self.seleniumLibrary._selenium
      chk = 'chk%s' % objId
      if sel.get_value(chk) != onoff:
         sel.click(chk)
      info('Checkbox id=' + chk + ' set to ' + sel.get_value(chk))

   def waitFor(self, el):
      sel = self.seleniumLibrary._selenium
      for i in range(20) :
         if sel.is_element_present(el) :
            info("element appeared after %s" % i)
            break 
         else :
            time.sleep(1)
      else :
         fail("element DID NOT appear")

   def closeBrowser(self):
      self.seleniumLibrary.close_all_browsers()      
      
   def goToPage(self, page):
      sel = self.seleniumLibrary._selenium
      if(page == 'pbis'):
         url = "/scrumzu/TEST/pbis/"
      elif(page == 'teams'):
         url = "/scrumzu/TEST/teams/"
      elif(page == 'sprints'):
         url = "/scrumzu/TEST/sprints/"
      elif(page == 'projects'):
         url = "/scrumzu/projects/"
      elif(page == 'releases'):
         url = "/scrumzu/TEST/releases/"
      elif(page == 'TEST'):
         url = "/scrumzu/TEST"
      else:
         fail("Unknown page given")
         
      sel.open(url)
      sel.wait_for_page_to_load(DEFAULT_TIMEOUT_MS)
     
   def clickPbiActionButton(self, button):
      if(button == "new pbi"):
         btn = pbiAddBtn
      elif(button == "submit form"):
         btn = submitForm
      elif(button == "edit pbi"):
         btn = pbiEditBtn
      elif(button == "delete pbi"):
         btn = pbiDel
      elif(button == "mark as done"):
         btn = pbiMarkAsDone
      else:
         fail("Unknown button")
         
      self.clickOn(btn)
      info(btn + "clicked")
     
      
   def clickTeamActionButton(self, button):
      if(button == "new team"):
         btn = teamAddBtn
      elif(button == "edit team"):
         btn = teamEditBtn
      elif(button == "delete"):
         btn = teamDel
      elif(button == "submit form"):
         btn = submitForm
      else:
         fail("Unknown button")
         
      self.clickOn(btn)
      info(btn + "clicked")
      

   def clickSprintActionButton(self, button):
      if(button == "new sprint"):
         btn = sprintAddBtn
      elif(button == "edit sprint"):
         btn = sprintEditBtn
      elif(button == "delete sprint"):
         btn = sprintDel
      elif(button == "submit form"):
         btn = submitForm
      elif(button == "start sprint"):
         btn = sprintStart
      elif(button == "end sprint"):
         btn = sprintStop
      else:
         fail("Unknown button")
         
      self.clickOn(btn)
      info(btn + "clicked")
  
   def clickProjectActionButton(self, button):
      if(button == "new project"):
         btn = projectAddBtn
      elif(button == "edit project"):
         btn = projectEditBtn
      elif(button == "delete project"):
         btn = projectDel
      elif(button == "submit form"):
         btn = submitForm
      elif(button == "add atr"):
         btn = projectAddAtr
      elif(button == "delete atr"):
         btn = projectDeleteAtr
      else:
         fail("Unknown button")
         
      self.clickOn(btn)
      info(btn + "clicked")
   
   def clickReleaseActionButton(self, button):
      if(button == "new release"):
         btn = releaseAddBtn
      elif(button == "edit release"):
         btn = releaseEditBtn
      elif(button == "delete release"):
         btn = releaseDel
      elif(button == "submit form"):
         btn = submitForm
      else:
         fail("Unknown button")
         
      self.clickOn(btn)
      info(btn + "clicked")
   
            
   def pause(self):
      time.sleep(10)  
      
   def getCurrentDate(self):
      now = datetime.datetime.now()
      return now.strftime("%Y-%m-%d")
   
   
   def login(self, role):
      sel = self.seleniumLibrary._selenium
      if( "%s" % role == "owner" ):
         sel.type( loginTB, owner )
         sel.type( passwordTB, pswd )
         self.clickOn( logIn )
      elif( "%s" % role == "master" ):
         sel.type( loginTB, master )
         sel.type( passwordTB, pswd )
         self.clickOn( logIn )
      elif( "%s" % role == "master2" ):
         sel.type( loginTB, 'sm2' )
         sel.type( passwordTB, pswd )
         self.clickOn( logIn )
      elif( "%s" % role == "user" ):
         sel.type( loginTB, user )
         sel.type( passwordTB, pswd )
         self.clickOn( logIn )
      elif( "%s" % role == "root" ):
         sel.type( loginTB, root )
         sel.type( passwordTB, pswd )
         self.clickOn( logIn )
      elif( "%s" % role == "sp" ):
         sel.type( loginTB, 'sp' )
         sel.type( passwordTB, pswd )
         self.clickOn( logIn )
      else:
         fail("Unknown user")
         
   def logout(self):
      sel = self.seleniumLibrary._selenium
      sel.click( logOut )
      sel.wait_for_page_to_load(DEFAULT_TIMEOUT_MS)
      
      
   def clickFilterActionButton(self, button):
      if(button == "select"):
         btn = filterSelectBtn
      elif(button == "clear"):
         btn = filterClearBtn
      elif(button == "run"):
         btn = filterRunBtn
      else:
         fail("Unknown button")
         
      self.clickOn(btn)
      info(btn + "clicked")
      
   def clickDialogWindowElement(self,element):
      sel = self.seleniumLibrary._selenium
      if(element == 'close filter'):
         el = filterClose
      elif(element == 'add filter'):
         el = filterAdd
      else:
         fail("Unknown element to click")
         
      sel.click(el)
      
   def makeDictionary(self, atr1, val1, atr2, val2):
      dic= {}
      dic[atr1] = val1
      dic[atr2] = val2
      return dic

   def selectCheckboxes(self, ids, idPrefix="chk"):
      for i in ids:
         self.selectCheckbox(i)
         
   def makeList(self, it1, it2):
      return [it1, it2]