'''
Created on 15-10-2011
@author: TM,SP
'''
from BasicOperations import BasicOperations
from Constants import * #@UnusedWildImport
from SeleniumLibrary import SeleniumLibrary
from TestStatusInfo import info, warn, fail #@UnusedImport


'''
from Constants import *
'''

class CheckContent(BasicOperations):
   '''
   Class with operations performing checking pages content.
   '''
   def __init__(self) :      
      self.seleniumLibrary = SeleniumLibrary()      

   
   def checkContent(self, viewName) :
      contents = {"pbis" : [pbiAddBtn ,
                            pbiEditBtn ,
                            pbiDelBtn ,
                            pbiSelectAllChbx] ,
                  
                  "teams" : [teamAddBtn,
                             teamEditBtn,
                             teamDelBtn,
                             teamSelectAllChbx] ,
                  
                  "sprints" : [sprintAddBtn ,
                               sprintEditBtn ,
                               sprintDelBtn ,
                               sprintSelectAllChbx]  ,
                  
                  "projects" : [projectAddBtn ,
                                projectEditBtn ,
                                projectDelBtn ,
                                projectSelectAllChbx] ,
                  
                  "filters" : [filterSelectBtn, 
                               filterClearBtn] ,
                  
                  "filterDialogWindow" : [filterList ,
                                          filterTable ,
                                          filerTableLogic ,
                                          filterTableColumn ,
                                          filterTableOperator ,
                                          filterTableValue ,
                                          filterTableControls ,
                                          filterNewName ,
                                          filterSave] ,
                  
                  "testAtr" : [projectAddAtr ,
                               projectDeleteAtr] ,
                  
                  "releases" : [releaseAddBtn ,
                                releaseEditBtn ,
                                releaseDelBtn ,
                                releaseSelectAllChbx]  ,
                  }
      
      for key in contents[viewName] :
         sel = self.seleniumLibrary._selenium
         if sel.is_element_present(key) :
            info("Element %s is present." % key)
         else :
            fail("Element %s not found!" % key)
            
 
      
   def checkHeader(self, expectedHeader) :
      sel = self.seleniumLibrary._selenium
      header = sel.get_text("css=h1")
      if header != expectedHeader:
         fail("Wrong header displayer, should be %s, but was %s" %(expectedHeader, header))
      
      
   def checkTitle(self, text) :
      sel = self.seleniumLibrary._selenium
      title = sel.get_title()     
      if ("%s" % text in str(title)) :
         info("Title OK!")
      else:
         fail("Wrong title! Was %s, should be %s" % (sel.get_title(), text))
      
  
   def checkSpecyficTitle(self, viewName) :
      contents = {"" : "Home" ,
                  "index" : "Index" ,
                  "pbis" : "Backlog" ,
                  "new pbi" : "Add PBI" ,
                  "edit pbi" : "Edit PBI" ,
                  "teams" : "Teams" ,
                  "new team" : "Add Team" ,
                  "edit team" : "Edit Team" ,
                  "sprints" : "Sprints" ,
                  "new sprint" : "Add sprint" ,
                  "edit sprint" : "Edit Sprint" ,
                  "projects" : "Projects" ,
                  "new project" : "Add project" ,
                  "TEST" : "Project details" ,
                  "new atr" : "Add attribute" ,
                  "releases" : "Releases" ,
                  "new release" : "Add release" , 
                  "edit release" : "Edit release" ,
                  }
      
      sel = self.seleniumLibrary._selenium
      expectedTitle = contents[viewName]
      title = sel.get_title()
      if (expectedTitle in str(title)) :
         info("Title OK for %s " % viewName)
      else:
         fail("Wrong title for %s, was %s !" % (viewName, sel.get_title()))
            
   def checkRowInPbiTable(self, pbi, idPbi, deleted=None, attributes=None):
      sel = self.seleniumLibrary._selenium
      css = "css=table[id='%s'] tr[id='pbi%s']" % (pbiListTable, idPbi)
      info(css)
      
      if(attributes != None):
         shift = len(attributes)
      else:
         shift = 0
      print "SHIFT %s" % shift

      if sel.is_element_present(css):
         info("New pbi visible in table")

         css = css + " td:nth-child(%s)"
         
         if sel.get_text(css % 1 + " h4 a") != pbi.title:
            fail("Invalid name displayed")
            
         if sel.get_text(css % 2) != pbi.priority:
            fail("Invalid priority, was %s, should be %s" % (sel.get_text(css % 2), pbi.priority))

         if sel.get_text(css % (5+shift)) != pbi.sprint:
            fail("Invalid sprint, was %s, should be %s" % (sel.get_text(css % (5+shift)), pbi.sprint))
         
         if sel.get_text(css % (6+shift)) != pbi.status:
            fail("Invalid status, was %s, should be %s" % (sel.get_text(css % 6), pbi.status))
            
      else:
         if(deleted):
            info("Pbi deleted successfully")
         else:
            fail("New pbi didn't appear")
      
   def checkPbiDetails(self, pbi, idPbi):
      sel = self.seleniumLibrary._selenium
      css = "css=table[id='%s'] tr[id='pbi%s'] a" % (pbiListTable, idPbi)
      info(css)
      
      if sel.is_element_present(css):
         sel.click(css)
      else:
         fail("Link to pbi not found")
         
      sel.wait_for_page_to_load(DEFAULT_TIMEOUT_MS)
      
      details = {'Title' : pbi.title,
                'Description' : pbi.description,
                'Priority' : 'Priority: ' + pbi.priority,
                'DateCreation' : 'Created: ' + pbi.dateCreation
                }
      
      for elementId, value in details.iteritems():
         css = "css=[id='pbiDetails%s']" % elementId
         text = sel.get_text(css)
         if text != value:
            fail("Wrong project.%s displayed: %s" % (elementId, text))
         else:
            info("Content of %s OK" % elementId)

   
   def checkRowInTeamTable(self, team, idTeam, deleted=None):
      sel = self.seleniumLibrary._selenium
      css = "css=table[id='%s'] tr[id='team%s']" % (teamListTable, idTeam)
      info(css)


      if sel.is_element_present(css):
         info("New team visible in table")

         css = css + " td:nth-child(%s)"
         
         if sel.get_text(css % 1 + " h3 a") != team.key+' - '+team.name:
            fail("Invalid key and name")
            
         if sel.get_text(css % 1 + " p") != team.description:
            fail("Invalid description")
         
         if sel.get_text(css % 1 + " ul li a") != team.projectName:
            fail("Invalid project")
             
      else:
         if(deleted):
            info("Team deleted successfully")
         else:
            fail("New team didn't appear")

            
            
   def checkTeamDetails(self, team, idTeam):
      sel = self.seleniumLibrary._selenium
      css = "css=table[id='%s'] tr[id='team%s'] a" % (teamListTable, idTeam)
      info(css)
      
      if sel.is_element_present(css):
         sel.click(css)
      else:
         fail("Link to team not found")
         
      sel.wait_for_page_to_load(DEFAULT_TIMEOUT_MS)
      
      details = {'Header' : team.key + ' - ' + team.name,
                'Description' : team.description,
                'Project' : 'Project: ' + team.projectName}
      
      for elementId, value in details.iteritems():
         css = "css=[id='teamDetails%s']" % elementId
         text = sel.get_text(css)
         if text != value:
            fail("Wrong project.%s displayed: %s" % (elementId, text))
         else:
            info("Content of %s OK" % elementId)

   def checkRowInSprintTable(self, sprint, idSprint, deleted=None):
      sel = self.seleniumLibrary._selenium
      css = "css=table[id='%s'] tr[id='sprint%s']" % (sprintListTable, idSprint)
      info(css)

      if sel.is_element_present(css):
         info("New sprint visible in table")

         css = css + " td:nth-child(%s)"
         
         if sel.get_text(css % 1 + " h4 a") != sprint.name:
            fail("Invalid name")
            
         if sel.get_text(css % 2 ) != sprint.dateFrom:
            fail("Invalid date FROM")
         
         if sel.get_text(css % 3 ) != sprint.dateTo:
            fail("Invalid date TO")
            
         if sel.get_text(css % 6 ) != sprint.status:
            fail("Invalid status")
             
      else:
         if(deleted):
            info("Sprint deleted successfully")
         else:
            fail("New sprint didn't appear")
            
            
            
   def checkSprintDetails(self, sprint, idSprint):
      sel = self.seleniumLibrary._selenium
      css = "css=table[id='%s'] tr[id='sprint%s'] a" % (sprintListTable, idSprint)
      info(css)
      
      if sel.is_element_present(css):
         sel.click(css)
      else:
         fail("Link to sprint not found")
         
      sel.wait_for_page_to_load(DEFAULT_TIMEOUT_MS)
            
      details = {'Name' : sprint.name,
                'DateFrom' : 'Date from: '+ sprint.dateFrom,
                'DateTo' : 'Date to: ' + sprint.dateTo,
                'Status' : 'Status: ' + sprint.status
                }
      
      for elementId, value in details.iteritems():
         css = "css=[id='sprintDetails%s']" % elementId
         text = sel.get_text(css)
         if text != value:
            fail("Wrong project.%s displayed: %s" % (elementId, text))
         else:
            info("Content of %s OK" % elementId)
            
   def checkRowInReleaseTable(self, release, idRelease, deleted=None):
      sel = self.seleniumLibrary._selenium
      css = "css=table[id='%s'] tr[id='release%s']" % (releaseListTable, idRelease)
      info(css)

      if sel.is_element_present(css):
         info("New release visible in table")

         css = css + " td:nth-child(%s)"
         
         if sel.get_text(css % 1 + " h4 a") != release.name:
            fail("Invalid name, was %s, should be %s" % (sel.get_text(css + "h4 a"), release.name))
            
         if sel.get_text(css % 2 ) != release.dateFrom:
            fail("Invalid date FROM")
         
         if sel.get_text(css % 3 ) != release.dateTo:
            fail("Invalid date TO")
            
      else:
         if(deleted):
            info("Release deleted successfully")
         else:
            fail("New release didn't appear")
            
  
            
   def checkReleaseDetails(self, release, idRelease):
      sel = self.seleniumLibrary._selenium
      css = "css=table[id='%s'] tr[id='release%s'] a" % (releaseListTable, idRelease)
      info(css)
      
      if sel.is_element_present(css):
         sel.click(css)
      else:
         fail("Link to sprint not found")
         
      sel.wait_for_page_to_load(DEFAULT_TIMEOUT_MS)
            
      details = {'Name' : release.name,
                'DateFrom' : 'Date from: '+ release.dateFrom,
                'DateTo' : 'Date to: ' + release.dateTo,
                }
      
      for elementId, value in details.iteritems():
         css = "css=[id='releaseDetails%s']" % elementId
         text = sel.get_text(css)
         if text != value:
            fail("Wrong project.%s displayed: %s" % (elementId, text))
         else:
            info("Content of %s OK" % elementId)            
            
         
         
   def checkRowInProjectTable(self, project, idProject, deleted=None):
      sel = self.seleniumLibrary._selenium
      css = "css=table[id='%s'] tr[id='project%s']" % (projectListTable, idProject)
      info(css)

      if sel.is_element_present(css):
         info("New project visible in table")

         css = css + " td:nth-child(%s)"
         
         if sel.get_text(css % 1 + " h3 a") != project.key+' - '+project.name:
            fail("Invalid key and name")
            
         if sel.get_text(css % 1 + " p" ) != project.description:
            fail("Invalid description")
         
         if sel.get_text(css % 1 + " ul li a" ) != project.website:
            fail("Invalid website")
            
         if sel.get_text(css % 1 + " ul li:nth-child(2)") != 'Version: '+project.version:
            fail("Invalid version")
            
         if sel.get_text(css % 1 + " ul li:nth-child(3)") != 'Product owner: '+project.owner:
            fail("Invalid product owner")
             
      else:
         if(deleted):
            info("Project deleted successfully")
         else:
            fail("New project didn't appear")
            
            
            
   def checkProjectDetails(self, project, idProject):
      sel = self.seleniumLibrary._selenium
      css = "css=table[id='%s'] tr[id='project%s'] a" % (projectListTable, idProject)
      info(css)
      
      if sel.is_element_present(css):
         sel.click(css)
      else:
         fail("Link to project not found")
         
      sel.wait_for_page_to_load(DEFAULT_TIMEOUT_MS)
      
      details = {
                'Header' : project.key + " - " + project.name,
                'Description' : project.description,
                'Website' : 'Website: ' + project.website,
                'Owner': 'Product owner: ' + project.owner,
                'Version' : 'Version: ' + project.version
                }
      
      for elementId, value in details.iteritems():
         css = "css=[id='projectDetails%s']" % elementId
         text = sel.get_text(css)
         if text != value:
            fail("Wrong project.%s displayed: %s" % (elementId, text))
         else:
            info("Content of %s OK" % elementId)
      
   def checkStatusInList(self, obj, idObj, expectedStatus):
      '''
      Checks status of object with #id in proper table with objects list
      @param obj: object type, eg. sprint
      @param idObj: object id number in DB
      @param expectedStatus: expected obj status shown in table 
      '''
      sel = self.seleniumLibrary._selenium
      
      if(obj == 'pbi'):
         css = "css=table[id='%s'] tr[id='pbi%s'] td:nth-child(6)" % (pbiListTable, idObj)
      elif(obj == 'sprint'):
         css = "css=table[id='%s'] tr[id='sprint%s'] td:nth-child(6)" % (sprintListTable, idObj)
      else:
         fail("Unknown obj for status checking in list table")
         
      statusInTable = sel.get_text(css)
      
      if statusInTable != expectedStatus:
         fail("Invalid status, should be %s, but was %s" % (expectedStatus, statusInTable))
      else:
         info("Status OK %s" % statusInTable)
         
         
   def checkUserRole(self, role):
      sel = self.seleniumLibrary._selenium
      css = "css=div[id=loginPanel] p b"
      if( role == 'owner' ):
         if sel.get_text( css ) != "po" :
            fail('User wrongly logged (product owner)')
         else:
            info('User logged as product owner')
      elif( role == 'master' ):
         if sel.get_text( css ) != "sm" :
            fail('User wrongly logged (scrum master)')
         else:
            info('User logged as scrum master')
      elif( role == 'user' ):
         if sel.get_text( css ) != "user" :
            fail('User wrongly logged (team member)')
         else:
            info('User logged as team member')
      else:
         fail('Unknown user')
         


#   def checkSprintStatusInList(self, idSprint, expectedStatus):
#      sel = self.seleniumLibrary._selenium
#      css = "css=table[id='%s'] tr[id='sprint%s'] td:nth-child(6)" % (sprintListTable, idSprint)
#      
#      statusInTable = sel.get_text(css)
#      
#      if statusInTable != expectedStatus:
#         fail("Invalid status, should be %s, but was %s" % (expectedStatus, statusInTable))
#      else:
#         info("Status OK %s" % statusInTable)
      

         