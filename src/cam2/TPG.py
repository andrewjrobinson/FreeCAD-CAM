'''
Created on 02/10/2012

@author: arobinson
'''
from UnimplementedTPError import UnimplementedTPError

class TPG(object):
    '''A superclass for all Tool Path Generators.'''
        
    def getActions(self):
        '''Returns a list of actions that this TPG offers'''
        return []

    def getSettings(self, action=None):
        '''Returns a list of settings that the TPG 'Action' will take.  If 
        action is None, then this will return a dictionary of all actions 
        settings.  Each setting will be in format of (<name>, <label>, <type>, <defaultvalue>, <units>, <helptext>)'''
        if action:
            return []
        return {}
        
    def run(self, action, settings=[]):
        '''Runs the selected action and returns the resulting TP'''
        raise UnimplementedTPError(action) # The run() method of this TP hasn't been implemented

