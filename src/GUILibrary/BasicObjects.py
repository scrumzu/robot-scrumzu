'''
Created on 23-10-2011
@author: TM,SP
'''
import datetime

class PBI():
   def __init__(self, title, description, priority, storyPoints, team, sprint, status, attributes=None):
      now = datetime.datetime.now()
      self.title = title
      self.description = description
      self.priority = priority
      self.storyPoints = storyPoints
      self.dateCreation = now.strftime("%Y-%m-%d")
      self.team = team
      self.sprint = sprint
      self.status = status
      self.attributes = attributes
 
   
class Sprint():
   def __init__(self, name, dateFrom, dateTo, status):
      self.name = name
      self.dateFrom = dateFrom
      self.dateTo = dateTo
      self.status = status
      
class Release():
   def __init__(self, name, dateFrom, dateTo):
      self.name = name
      self.dateFrom = dateFrom
      self.dateTo = dateTo
      
   
class Team():
   def __init__(self, name, key, description, project, projectName, scrumMaster):
      self.name = name
      self.key = key
      self.description = description
      self.project = project
      self.projectName = projectName
      self.scrumMaster = scrumMaster
      

class Project():
   def __init__(self, name, key, description, website, owner, version):
      self.key = key
      self.name = name
      self.description = description
      self.website = website
      self.owner = owner
      self.version = version
      

class FilterItem():
   def __init__(self, andOr, field, operator, value):
      self.andOr = andOr
      self.field = field
      self.operator = operator
      self.value = value
      
class Attribute():
   def __init__(self, name, atype):
      self.name = name
      self.atype = atype