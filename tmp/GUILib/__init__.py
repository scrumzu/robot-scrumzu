
from BasicOperations import BasicOperations
from GUILibrary.CheckContent import CheckContent
from GUILibrary.Breadcrumbs import Breadcrumbs

class GUILibrary(BasicOperations, CheckContent):
   def __init__(self):
      BasicOperations.__init__(self);
      CheckContent.__init__(self);
      Breadcrumbs.__init__(self);
      pass
