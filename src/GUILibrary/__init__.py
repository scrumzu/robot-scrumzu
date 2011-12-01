
from BasicOperations import BasicOperations
from GUILibrary.CheckContent import CheckContent
from GUILibrary.Forms import Forms
from BasicObjects import *

class GUILibrary(BasicOperations, CheckContent, Forms):
   def __init__(self):
      BasicOperations.__init__(self);
      CheckContent.__init__(self);
      Forms.__init__(self);
      pass
