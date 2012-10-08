'''
Created on 02/10/2012

@author: arobinson
'''
from cam2.TPG import TPG
from cam2.UnimplementedTPError import UnimplementedTPError

__all__=['ExampleTPG3']

class ExampleTPG3(TPG):
    '''This is an example TPG that demonstrates how to create a TPG for the 
    CAM2 module'''
    
    '''
    Each settings is made up of a 6-tuple (<name>, <label>, <type>, 
    <defaultvalue>, <unit>, <helptext>)
    <name>
        A unique (within the action) identifier for the given setting.  It may 
        be preceded by one or more group names (separated by ':') which are 
        used by the UI to construct a setting Tree.
        
    <label>
        The text to display to the user for this setting.
    
    <type>
        May be 'Cam::Group' for a group header (i.e. not a real setting) OR one
        of the built in types
        @see: http://sourceforge.net/apps/mediawiki/free-cad/index.php?title=Scripted_objects#Available_properties
        
    <defaultvalue>
        The default value that will appear on screen before the user makes 
        changes.
        
    <unit>
        Optional help text that identifies the units that this setting expects
        
    <helptext>
        Optional description of this setting; it is useful to include examples 
        of desirable options
    '''
    settings = {
                'rough': [('tolerance','Tolerance', 'App::PropertyInteger', 1, 'mm', 'How close to run tool to final depth'),
                          ],
                'finish': [('tolerance','Tolerance', 'Cam::Group', None, '', ''), # this is optional way to specify the label of the group
                           # these are the sub elements of tolerance group
                           ('tolerance:min','Minimum', 'App::PropertyInteger', 0.0, 'mm', 'How close to run tool to final depth'),
                           ('tolerance:max','Maximum', 'App::PropertyInteger', 0.1, 'mm', 'How close to run tool to final depth'),
                           ],
                }
    
    def getActions(self):
        '''Returns a list of actions that this TPG offers'''
        return self.settings.keys()

    def getSettings(self, action=None):
        '''Returns a list of settings that the TPG 'Action' will take.  If 
        action is None, then this will return a dictionary of all actions 
        settings.  Each setting will be in format of (<name>, <label>, <type>, <defaultvalue>)
        NOTE: the resulting dictionary or list should be considered read-only!'''
        if action:
            if action in self.settings:
                return self.settings[action]
            raise UnimplementedTPError(action)
        return self.settings
        
    def run(self, action, settings=[]):
        '''Runs the selected action and returns the resulting TP'''
        #TODO: implement an example (Note: need to define the output interface i.e. what it will return)
        raise UnimplementedTPError(action)
    
    