'''
Created on 02/10/2012

@author: arobinson
'''
import inspect, types

from TPG import TPG

class TPGFactory(object):
    '''This is a factory class used to find and initialise Tool Path Generators (TPG)'''
    
    
    def __init__(self, searchpath=['cam2.tpg']):
        '''Creates a new TPGFactory
        
        <searchpath>
            A list of strings which represent the include path to check in for 
            TPG's.  e.g. ['cam2.tpg',]
        '''
        self._searchpath = searchpath
        self._tpgs = {} # elements [<class>, <instance>]
    
    def listTPGs(self):
        '''Rescans the TPG Module for new TPGs and returns a list of their names'''
        self._scanDirs()
        return self._tpgs.keys()
        
    def getTPG(self, name, reload=False):
        '''Gets an instance (Singleton) of a given TPG by name.  reload==True causes the module to be rescanned for changes.'''
        if reload: #TODO: only reload the selected TPG
            self._scanDirs(reload)
        if name in self._tpgs:
            tpg = self._tpgs[name]
            # instanciate the singleton if required
            if not tpg[1]:
                tpg[1] = tpg[0]()
            return tpg[1]
            
    def _scanDirs(self, reload = False):
        '''Scans the entire searchpath for TPGs'''
        for path in self._searchpath:
            self._scanDir(path, reload)
        
    def _scanDir(self, path, reload = False):
        '''Scans <path> package for TPGs'''
        package = __import__(path, globals(), locals(), [], -1)
        # loop through all modules (or special packages @see examples in tpg folder)
        for modname in dir(package.tpg):
            mod = getattr(package.tpg, modname)
            if type(mod) == types.ModuleType:
                # loop through all the definitions in the module
                for classname in dir(mod):
                    cls = getattr(mod, classname)
                    # filter out only Classes that extend the TPG superclass
                    if inspect.isclass(cls) and issubclass(cls, TPG) and cls != TPG:
                        if reload or classname not in self._tpgs:
                            self._tpgs[classname] = [cls, None]
## End TPGFactory ##
