'''
Created on 27-09-2011

@author: TM
'''
import MySQLdb
from TestStatusInfo import info, warn, fail #@UnusedImport


HOST = "spectre.dyndns-server.com"
USER = "julius"
PASSWORD = "dr.no"
BASENAME = "scrumzu"

#HOST = "localhost"
#USER = "root"
#PASSWORD = ""
#BASENAME = "scrumzu"

class Database:
   def __init__(self):
      pass
       
   def runQuery(self, query):
      print "Connecting to database"
      self.db = MySQLdb.connect(HOST, USER, PASSWORD, BASENAME)
      cursor = self.db.cursor()
      
      print("Exeuting query %s" % query)
      
      cursor.execute(query)
      
      #number of rows in result
      numrows = int(cursor.rowcount)

      # get and display one row at a time
      rows = []
      for x in range(0, numrows):
         print "Fetching row %s" % x
         rows.append(cursor.fetchone())

      cursor.close()
      self.db.commit()
      self.db.close()

      print rows
      return rows
   
   def selectFromTable(self, table, where, *arg):
      columns = ', '.join(arg)
      query = "SELECT %s FROM %s WHERE %s" % (columns, table, where)
      self.runQuery(query)
      
   def countRows(self, table, idColumn, idValue, expectedCount):
      query = "SELECT COUNT(%s) FROM scrumzu.%s WHERE %s = %s" % (idColumn, table, idColumn, idValue)
      rows = int(self.runQuery(query)[0][0])
      
      expectedCount = int(expectedCount)
      
      if rows != expectedCount:
         fail('Got %s rows, should be %s' %(rows, expectedCount))
   
   
   def getLastPbi(self):
      query = "SELECT idPBI from scrumzu.PBIs order by idPBI desc LIMIT 1;"
      return self.runQuery(query)[0][0]

   def deleteAttribute(self, idAttr):
      tables = ['PBIs_DoubleAttributes', 'PBIs_StringAttributes', 'Attributes']
      query = ""
      for table in tables:
         query += "DELETE FROM scrumzu.%s WHERE %s.idAttribute=%s;\n" % (table, table, idAttr)
      self.runQuery(query)
      

   def deletePbi(self, idPbi):
      query = "DELETE FROM scrumzu.WorkItems WHERE idPBI=%s;" %idPbi
      self.runQuery(query)
      query = "DELETE FROM scrumzu.PBIs_DoubleAttributes WHERE idPBI=%s;" %idPbi
      self.runQuery(query)
      
      query = "DELETE FROM scrumzu.PBIs_StringAttributes WHERE idPBI=%s;" %idPbi
      self.runQuery(query)

      query = "DELETE FROM scrumzu.PBIs WHERE idPBI=%s;" %idPbi
      self.runQuery(query)
      
      
      info("PBI #%s deleted" % idPbi);
      
      
   def getLastTeam(self):
      query = "SELECT idTeam from scrumzu.Teams order by idTeam desc LIMIT 1;"
      return self.runQuery(query)[0][0]

   def deleteTeam(self, idTeam):
      query = "DELETE FROM scrumzu.Teams WHERE idTeam=%s;" %idTeam
      self.runQuery(query)
      info("Team #%s deleted" % idTeam);
      
      
   def getLastSprint(self):
      query = "SELECT idSprint from scrumzu.Sprints order by idSprint desc LIMIT 1;"
      return self.runQuery(query)[0][0]

   def deleteSprint(self, idSprint):
      query = "DELETE FROM scrumzu.Sprints WHERE idSprint=%s;" %idSprint
      self.runQuery(query)
      info("Sprint #%s deleted" % idSprint);
      
      
   def getLastRelease(self):
      query = "SELECT idRelease from scrumzu.Releases order by idRelease desc LIMIT 1;"
      return self.runQuery(query)[0][0]

   def deleteRelease(self, idRelease):
      query = "DELETE FROM scrumzu.Releases WHERE idRelease=%s;" %idRelease
      self.runQuery(query)
      info("Release #%s deleted" % idRelease);
            
      
   def getLastAttribute(self):
      query = "SELECT idAttribute from scrumzu.Attributes order by idAttribute desc LIMIT 1;"
      return self.runQuery(query)[0][0]      
      
   def getLastProject(self):
      query = "SELECT idProject from scrumzu.Projects order by idProject desc LIMIT 1;"
      return self.runQuery(query)[0][0]

   def deleteProject(self, idProject):
      query = "DELETE FROM scrumzu.Projects WHERE idProject=%s;" %idProject
      self.runQuery(query)
      info("Project #%s deleted" % idProject);
      
   def testPackage(self):
      query = "INSERT INTO scrumzu.Projects(name, owner, url, description, version, alias) VALUES ('Testing Project', 'Tester', 'www.google.com', 'Project for tests', '1.0', 'TEST');"
      self.runQuery(query)
     
      query = "INSERT INTO scrumzu.Teams(idProject, description, name, alias, idUser) VALUES ((SELECT idProject from scrumzu.Projects order by idProject desc LIMIT 1), 'Team for tests', 'First Test Team', 'TTF', '3');"
      self.runQuery(query)
      query = "INSERT INTO scrumzu.Teams(idProject, description, name, alias, idUser) VALUES ((SELECT idProject from scrumzu.Projects order by idProject desc LIMIT 1), 'Team for tests', 'Second Test Team', 'TTS', '3');"
      self.runQuery(query)
     
      query = "INSERT INTO scrumzu.PBIs(title, description, idProject, priority, dateCreation, type) VALUES ('TEST project management', 'As a product owner i want to manage projects', (SELECT idProject from scrumzu.Projects order by idProject desc LIMIT 1), '0', '2011-12-12', '0');"
      self.runQuery(query)
      query = "INSERT INTO scrumzu.PBIs(title, description, idProject, priority, dateCreation, type) VALUES ('TEST team management', 'As a product owner i want to manage teams', (SELECT idProject from scrumzu.Projects order by idProject desc LIMIT 1), '0', '2011-12-12', '0');"
      self.runQuery(query)
      query = "INSERT INTO scrumzu.PBIs(title, description, idProject, priority, dateCreation, type) VALUES ('TEST pbi management', 'As a product owner i want to manage pbi', (SELECT idProject from scrumzu.Projects order by idProject desc LIMIT 1), '0', '2011-12-12', '0');"
      self.runQuery(query)
      query = "INSERT INTO scrumzu.PBIs(title, description, idProject, priority, dateCreation, type) VALUES ('projektowy', 'piszemy testy', (SELECT idProject from scrumzu.Projects order by idProject desc LIMIT 1), '0', '2011-12-12', '0');"
      self.runQuery(query)
      query = "INSERT INTO scrumzu.PBIs(title, description, idProject, priority, dateCreation, type) VALUES ('kwiatki', 'tylko nie rozowe', (SELECT idProject from scrumzu.Projects order by idProject desc LIMIT 1), '0', '2011-12-12', '0');"
      self.runQuery(query)
      query = "INSERT INTO scrumzu.PBIs(title, description, idProject, priority, dateCreation, type) VALUES ('slon', 'duzy i zielony', (SELECT idProject from scrumzu.Projects order by idProject desc LIMIT 1), '0', '2011-12-12', '0');"
      self.runQuery(query)
     
      query = "INSERT INTO scrumzu.Sprints(dateFrom, dateTo, sprintStatus, idProject, name) VALUES ('2014-12-12', '2015-12-12', '1', (SELECT idProject from scrumzu.Projects order by idProject desc LIMIT 1), 'first TEST');"
      self.runQuery(query)
      query = "INSERT INTO scrumzu.Sprints(dateFrom, dateTo, sprintStatus, idProject, name) VALUES ('2014-09-09', '2015-09-09', '1', (SELECT idProject from scrumzu.Projects order by idProject desc LIMIT 1), 'second TEST');"
      self.runQuery(query)
     
      query = "INSERT INTO scrumzu.WorkItems(idTeam, idPBI, idSprint, status, date, idUser, storyPoints) VALUES (null, (SELECT idPBI from scrumzu.PBIs WHERE PBIs.title='TEST project management'), null, '0', '2011-11-02 10:00:00', '2', '0');"
      self.runQuery(query)
      query = "INSERT INTO scrumzu.WorkItems(idTeam, idPBI, idSprint, status, date, idUser, storyPoints) VALUES (null, (SELECT idPBI from scrumzu.PBIs WHERE PBIs.title='TEST team management'), null, '0', '2011-11-02 10:00:00', '2', '0');"
      self.runQuery(query)
      query = "INSERT INTO scrumzu.WorkItems(idTeam, idPBI, idSprint, status, date, idUser, storyPoints) VALUES (null, (SELECT idPBI from scrumzu.PBIs WHERE PBIs.title='TEST pbi management'), null, '0', '2011-11-02 10:00:00', '2', '0');"
      self.runQuery(query)
      query = "INSERT INTO scrumzu.WorkItems(idTeam, idPBI, idSprint, status, date, idUser, storyPoints) VALUES (null, (SELECT idPBI from scrumzu.PBIs WHERE PBIs.title='projektowy'), null, '0', '2011-11-02 10:00:00', '2', '0');"
      self.runQuery(query)
      query = "INSERT INTO scrumzu.WorkItems(idTeam, idPBI, idSprint, status, date, idUser, storyPoints) VALUES (null, (SELECT idPBI from scrumzu.PBIs WHERE PBIs.title='kwiatki'), null, '0', '2011-11-02 10:00:00', '2', '0');"
      self.runQuery(query)
      query = "INSERT INTO scrumzu.WorkItems(idTeam, idPBI, idSprint, status, date, idUser, storyPoints) VALUES (null, (SELECT idPBI from scrumzu.PBIs WHERE PBIs.title='slon'), null, '0', '2011-11-02 10:00:00', '2', '0');"
      self.runQuery(query)
   
   def _deletePbisAndRelatedItems(self, pbiIds):
      tables=['WorkItems', 'PBIs_DoubleAttributes', 'PBIs_StringAttributes', 'PBIs']
      
      query=""
      for table in tables:
         for pbiId in pbiIds:
            query += "DELETE FROM scrumzu.%s WHERE %s.idPBI=%s;\n" % (table, table, pbiId)
         if(query!=""):
            self.runQuery(query)    
      
   def _getPbisIds(self, names=None, projectId=None):
      rows = []
      
      if names:
         titles = "'" + "', '".join(names)+"'"
         query = "SELECT idPBI from scrumzu.PBIs WHERE PBIs.title IN (%s)" % titles
         rows = self.runQuery(query)
      elif projectId:
         query = "SELECT idPBI from scrumzu.PBIs WHERE PBIs.idProject = %s" % projectId
         rows = self.runQuery(query)
      
      ids=[]
      for row in rows:
         ids.append(row[0])
         
      print ids
      return ids
      
   def _getProjectId(self, name):
      query = "SELECT idProject from scrumzu.Projects where name = '%s'" %name
      projectId = 0
      rows = self.runQuery(query)
      if(rows!=[]):
         projectId = rows[0][0]
      return projectId 
   
   def _deleteProjectAndRelatedItems(self, idProject):
      tables = ['PBIs', 'Attributes', 'Teams', 'Sprints', 'Projects']
      query = "";
      for table in tables:
            query += "DELETE FROM scrumzu.%s WHERE %s.idProject=%s;\n" % (table, table, idProject)
      if(query!=""):
         self.runQuery(query)
      
   def deleteTestPackageTM(self):
      names = ['TEST project management', 'TEST team management'
               'TEST pbi management', 'projektowy',
               'slon', 'kwiatki']
      pId = self._getProjectId('Testing Project')

      ids = self._getPbisIds(projectId=pId)
      self._deletePbisAndRelatedItems(ids)
      print "DELETED PBIs"
      
      self._deleteProjectAndRelatedItems(pId)
      
   def deleteTestPackage(self):
      query = "DELETE FROM scrumzu.WorkItems WHERE WorkItems.idPBI=(SELECT idPBI from scrumzu.PBIs WHERE PBIs.title='TEST project management');"
      self.runQuery(query)
      query = "DELETE FROM scrumzu.WorkItems WHERE WorkItems.idPBI=(SELECT idPBI from scrumzu.PBIs WHERE PBIs.title='TEST team management');"
      self.runQuery(query)
      query = "DELETE FROM scrumzu.WorkItems WHERE WorkItems.idPBI=(SELECT idPBI from scrumzu.PBIs WHERE PBIs.title='TEST pbi management');"
      self.runQuery(query)
      query = "DELETE FROM scrumzu.WorkItems WHERE WorkItems.idPBI=(SELECT idPBI from scrumzu.PBIs WHERE PBIs.title='projektowy');"
      self.runQuery(query)
      query = "DELETE FROM scrumzu.WorkItems WHERE WorkItems.idPBI=(SELECT idPBI from scrumzu.PBIs WHERE PBIs.title='kwiatki');"
      self.runQuery(query)
      query = "DELETE FROM scrumzu.WorkItems WHERE WorkItems.idPBI=(SELECT idPBI from scrumzu.PBIs WHERE PBIs.title='slon');"
      self.runQuery(query)
      '''
      query = "DELETE FROM scrumzu.PBIs_DoubleAttributes WHERE PBIs_DoubleAttributes.idPBI=(SELECT idPBI from scrumzu.PBIs WHERE PBIs.title='TEST project management');"
      self.runQuery(query)
      
      query = "DELETE FROM scrumzu.PBIs_DoubleAttributes WHERE PBIs_DoubleAttributes.idPBI=(SELECT idPBI from scrumzu.PBIs WHERE PBIs.title='TEST team management');"
      self.runQuery(query)
      
      query = "DELETE FROM scrumzu.PBIs_DoubleAttributes WHERE PBIs_DoubleAttributes.idPBI=(SELECT idPBI from scrumzu.PBIs WHERE PBIs.title='TEST pbi management');"
      self.runQuery(query)
      
      query = "DELETE FROM scrumzu.PBIs_DoubleAttributes WHERE PBIs_DoubleAttributes.idPBI=(SELECT idPBI from scrumzu.PBIs WHERE PBIs.title='projektowy');"
      self.runQuery(query)
      
      query = "DELETE FROM scrumzu.PBIs_DoubleAttributes WHERE PBIs_DoubleAttributes.idPBI=(SELECT idPBI from scrumzu.PBIs WHERE PBIs.title='slon');"
      self.runQuery(query)
      
      query = "DELETE FROM scrumzu.PBIs_DoubleAttributes WHERE PBIs_DoubleAttributes.idPBI=(SELECT idPBI from scrumzu.PBIs WHERE PBIs.title='kwiatki');"
      self.runQuery(query)
      
      
      query = "DELETE FROM scrumzu.PBIs_StringAttributes WHERE PBIs_DoubleAttributes.idPBI=(SELECT idPBI from scrumzu.PBIs WHERE PBIs.title='TEST project management');"
      self.runQuery(query)
      
      query = "DELETE FROM scrumzu.PBIs_StringAttributes WHERE PBIs_DoubleAttributes.idPBI=(SELECT idPBI from scrumzu.PBIs WHERE PBIs.title='TEST team management');"
      self.runQuery(query)
      
      query = "DELETE FROM scrumzu.PBIs_StringAttributes WHERE PBIs_DoubleAttributes.idPBI=(SELECT idPBI from scrumzu.PBIs WHERE PBIs.title='TEST pbi management');"
      self.runQuery(query)
      
      query = "DELETE FROM scrumzu.PBIs_StringAttributes WHERE PBIs_DoubleAttributes.idPBI=(SELECT idPBI from scrumzu.PBIs WHERE PBIs.title='projektowy');"
      self.runQuery(query)
      
      query = "DELETE FROM scrumzu.PBIs_StringAttributes WHERE PBIs_DoubleAttributes.idPBI=(SELECT idPBI from scrumzu.PBIs WHERE PBIs.title='slon');"
      self.runQuery(query)
      
      query = "DELETE FROM scrumzu.PBIs_StringAttributes WHERE PBIs_DoubleAttributes.idPBI=(SELECT idPBI from scrumzu.PBIs WHERE PBIs.title='kwiatki');"
      self.runQuery(query)
      '''
      
      query = "DELETE FROM scrumzu.WorkItems WHERE WorkItems.idPBI=(SELECT idPBI from scrumzu.PBIs order by idPBI desc LIMIT 1);"
      self.runQuery(query)
      
      query = "DELETE FROM scrumzu.Attributes WHERE Attributes.idProject=(SELECT idProject from scrumzu.Projects WHERE Projects.alias='TEST');"
      self.runQuery(query)
      query = "DELETE FROM scrumzu.PBIs WHERE PBIs.idProject=(SELECT idProject from scrumzu.Projects WHERE Projects.alias='TEST');"
      self.runQuery(query)
      query = "DELETE FROM scrumzu.Teams WHERE Teams.idProject=(SELECT idProject from scrumzu.Projects WHERE Projects.alias='TEST');"
      self.runQuery(query)
      query = "DELETE FROM scrumzu.Sprints WHERE Sprints.idProject=(SELECT idProject from scrumzu.Projects WHERE Projects.alias='TEST');"
      self.runQuery(query)
      query = "DELETE FROM scrumzu.Releases WHERE Releases.idProject=(SELECT idProject from scrumzu.Projects WHERE Projects.alias='TEST');"
      self.runQuery(query)
      query = "DELETE FROM scrumzu.Projects WHERE Projects.alias='TEST';"
      self.runQuery(query)