'''
Created on 19-10-2011
@author: SP
'''

from SeleniumLibrary import SeleniumLibrary
from TestStatusInfo import info, warn, fail #@UnusedImport
import time
from BasicObjects import PBI, Team, Sprint, Project, FilterItem, Attribute, Release


class Forms():
   '''
   Class with operations performing filling web forms.
   '''
   
   def __init__(self) :      
      self.seleniumLibrary = SeleniumLibrary() 
      
   
   def fillPbiForm(self, title, description, priority, storyPoints, team, sprint, status, user, atr=None):
      sel = self.seleniumLibrary._selenium
      if (user == 'po'):
         sel.type("pbiFormTitle", title)
         sel.type("pbiFormDescription", description)
         sel.type("pbiFormPriority", priority)
      if (user == 'sm') or (user == 'po'):
         sel.type("pbiFormStoryPoints", storyPoints)
         
      sel.select("pbiFormTeam", team)
      sel.select("pbiFormSprint", sprint)
      sel.select("pbiFormWorkStatus", status)
      
      if(atr != None):
         for a, v in atr.iteritems():
            idd = "pbiFormCustomAttr-%s" %a
            sel.type(idd, v)
      return PBI(title, description, priority, storyPoints, team, sprint, status, atr)
   
   def changeSpring(self, spring):
      sel = self.seleniumLibrary._selenium
      sel.type("pbiFormSprint", spring)
   
   
   def fillTeamForm(self, name, key, description, project, projectName, scrumMaster):
      sel = self.seleniumLibrary._selenium
      
      if sel.is_alert_present():
         time.sleep(30)
         warn("ALERT?")
      
      sel.type("teamFormName", name)
      sel.type("alias", key)
      sel.type("teamFormDescription", description)
      sel.type("teamFormProject", project)
      sel.type("teamFormScrumMaster", scrumMaster)
      return  Team(name, key, description, project, projectName, scrumMaster)
       
       
   def fillSprintForm(self, name, dateFrom, dateTo, status):
      sel = self.seleniumLibrary._selenium
      sel.type("sprintFormName", name)
      sel.type("sprintFormDateFrom", dateFrom)
      sel.type("sprintFormDateTo", dateTo)
      sel.select("sprintStatus", status)
      return Sprint(name, dateFrom, dateTo, status)

   def fillReleaseForm(self, name, dateFrom, dateTo):
      sel = self.seleniumLibrary._selenium
      sel.type("releaseFormName", name)
      sel.type("releaseFormDateFrom", dateFrom)
      sel.type("releaseFormDateTo", dateTo)
      return Release(name, dateFrom, dateTo)

   def fillProjectForm(self, name, alias, description, url, owner, version, attribute):
      sel = self.seleniumLibrary._selenium
      sel.type("projectFormName", name)
      sel.type("alias", alias)
      sel.type("projectFormDescription", description)
      sel.type("url", url)
      sel.type("owner", owner)
      sel.type("version", version)
      return Project(name, alias, description, url, owner, version)
   
   def fillFilterItemForm(self, position, andOr, field, operator, value):
      sel = self.seleniumLibrary._selenium
      css = "css=table[id='filterTable'] tbody tr:nth-child(%s) td:nth-child" % position
      if position>'1':
         sel.type(css+"(1) select", andOr)
      sel.type(css+"(2) select", field)
      sel.type(css+"(3) select", operator)
      sel.type(css+"(4) input", value)
      return FilterItem(andOr, field, operator, value)
   
   def fillAttributeForm(self, name, atype):
      sel = self.seleniumLibrary._selenium
      sel.type("attributeFormName", name)
      sel.type("attributeFormType", atype)
      return Attribute(name, atype)
   
      
