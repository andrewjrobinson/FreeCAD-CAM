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
            if not tpg[1]:
                tpg[1] = tpg[0]()
            return tpg[1]
            
        
    def _scanDirs(self, reload = False):
        '''Scans the entire searchpath for TPGs'''
        for path in self._searchpath:
            self._scanDir(path, reload)
        
    def _scanDir(self, path, reload = False):
        '''Scans a directory for TPGs'''
        package = __import__(path, globals(), locals(), [], -1)
#        print dir(package.tpg)
        for modname in dir(package.tpg):
            mod = getattr(package.tpg, modname)
            if type(mod) == types.ModuleType:
                for classname in dir(mod):
                    cls = getattr(mod, classname)
                    if inspect.isclass(cls) and issubclass(cls, TPG) and cls != TPG:
                        if reload or classname not in self._tpgs:
                            self._tpgs[classname] = [cls, None]
#                        print "from tpg.%s import %s" %(modname, classname)
                
