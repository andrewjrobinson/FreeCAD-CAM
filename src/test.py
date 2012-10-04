'''
Created on 02/10/2012

@author: arobinson
'''
from cam2 import TPGFactory
                
if __name__ == "__main__":
    factory = TPGFactory.TPGFactory()
    print factory.listTPGs()
    tpg = factory.getTPG("ExampleTPG")
    print tpg.getActions()
    print tpg.getSettings()
    print tpg.run('rough')
#    factory._scanDir([])