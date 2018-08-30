#!/usr/bin/env python
import pdb
import sys, time, copy, re

import superTypes
from superTypes import *

class _attribute:
    __attribute_key = ['type','value','private','owner']
    __name__  = None
    __type    = int
    __value   = None
    __private = False
    __default = None
    __owner   = None

    __nb_obj  = 0

    def __init__(self,name,val):
        if not isinstance(val,dict):
            raise TypeError("Attribute must a dict that contains at least keys: {}".format(str(self.__attribute_key)))
        for k in val.keys():
            if not k in self.__attribute_key: raise KeyError("Incorrect attribute key: '{}'".format(k,)) 
        missing = [k for k in self.__attribute_key if not k in val]
        if missing != []:
            raise KeyError("Missing input key: '{}'".format(missing,)) 
        #pdb.set_trace()
        superTypes.checkTypes([name,val['private'],val['value']],[str,bool,val['type']]).assertTypes()

        self.__name__  = name
        self.__type    = val['type']
        if isinstance(self.__type,list):
            self.__value   = val['value']
        else:
            self.__value = self.__type(val['value'])
        self.__private = val['private']
        self.__default = val['value']
        self.__owner   = val['owner']

        _attribute.__nb_obj+=1

    def set_value(self,val):
        superTypes.checkTypes(val,self.__type).assertTypes()

        self.__value = val

    @property
    def value(self):   return self.__value
    @property
    def private(self): return self.__private    #readonly parameter
    @property
    def default(self): return self.__default    #readonly parameter
    @property
    def type(self):    return self.__type       #readonly parameter
    @property
    def owner(self):   return self.__owner       #readonly parameter

    # count nb of object created, classmethod and staticmethod
    def get_nb_obj(cls):
        return cls.__nb_obj
    get_nb_obj = classmethod(get_nb_obj)

class attribute_ctrl:
    __attribute_accessor = ['has_','get_','set_','setItems_','rst_','getDefault_','chkEq_','chkType_']
    __attribute_key = ['type','value','default','private']

    def __init__(self):
        self.__my_attribute=dict()

    def __getattr__(self,attr):
        cmd = re.split('__',attr)[0]+'_'		#'__' for debug, '_' unless
        if cmd in self.__attribute_accessor and attr.startswith(cmd):
            attrName =re.sub(r'^'+cmd+'_','',attr)	#r'^'+cmd+'_' for debug, r'^'+cmd unless

            def wrapper(*args):
                return getattr(self,cmd+'_attrName')(attrName, *args)
            return wrapper
            #return lambda *x: self._attribute_accessor_execute(cmd,attrName,*x)
        else:
            raise AttributeError("Undefined attribute "+attr)

    def get_nb_attribute(self):
        return _attribute.get_nb_obj()

    #Attribute creation/deletion
    def new__attribute(self,attrName,attrValue):
        if not isinstance(attrName,str):
            raise TypeError("Attribute name must be a str")
        if not isinstance(attrValue,dict):
            raise TypeError("Attribute must a dict that contains at least keys: {}".format(str(_attribute.__attribute_key)))

        if self.__my_attribute.has_key(attrName):
            raise AttributeError("Cannot recreate an existing attribute: {}".format(attrName))
        
        if attrValue['owner']==None:
            attrValue['private']=False
        else:
            attrValue['private']=True

        self.__my_attribute[attrName]=_attribute(attrName,attrValue)

    def del__attribute(self,attrName):
        if not self.has__attribute(attrName):
            raise AttributeError("Cannot delete a missing attribute: %s" % (attrName,))

        del self.__my_attribute[attrName]


    def has__attribute(self,attrName):
        return  self.__my_attribute.has_key(attrName) 


    #private method to set, get or del private attribute __attribute
    def _set__attribute(self,attrName,args):
        if len(args) > 1:
            newValue = self.__insertItems(self.__my_attribute[attrName].value,args[0], args[1])
            self.__my_attribute[attrName].set_value(newValue)
        else:
            self.__my_attribute[attrName].set_value(args[0])

    def _get__attribute(self,attrName, args=[]):
        value = self.__my_attribute[attrName].value 
        if len(args) > 0:
            value = self.__extractItems(value, args[0])
        return value

    def _rst__attribute(self,attrName):
        self.__my_attribute[attrName].set_value(self.__my_attribute[attrName].default)

    def _getDefault__attribute(self,attrName):
        return self.__my_attribute[attrName].default

    def _checkEqual__attribute(self,attrName,args):
        return  self.__my_attribute[attrName].value == args[0]

    def _checkType__attribute(self,attrName,args):
        superTypes.superTypesCheck([self.__my_attribute[attrName].value], [self.__my_attribute[attrName].type]).chkTypes()

    def _remove__attribute(self,attrName,args):
        return self.__extractItems(value, args[0])

    def _append__attribute(self,attrName,args):
        val = self._get__attribute(attrName, args)
        self._set__attribute(val.extend(args))

    def _attribute_accessor_execute(self,accessor,attrName, *args):

        if accessor.startswith('has_'):		return self.has__attribute(attrName)
        else:
            if not self.has__attribute(attrName): raise AttributeError("Undefined variable "+attrName)
            if self.__my_attribute[attrName].private != False and self.__my_attribute[attrName].owner != self.__class_name__:
                raise AttributeError("%s is Private attribute of class %s" % (attrName,self.__my_attribute[attrName].owner))

            if accessor.startswith('get_'):          return self._get__attribute(attrName, args=list(args))
            elif accessor.startswith('set_'):        return self._set__attribute(attrName, args=list(args))
            elif accessor.startswith('rst_'):        return self._rst__attribute(attrName)
            elif accessor.startswith('getDefault_'): return self._getDefault__attribute(attrName)
            elif accessor.startswith('chkEq_'):      return self._checkEqual__attribute(attrName, args=list(args))
            elif accessor.startswith('chkType_'):    return self._chkType__attribute(attrName, args=list(args))
            elif accessor.startswith('remove_'):      return self._remove__attribute(attrName, args=list(args))
            elif accessor.startswith('append_'):    return self._append__attribute(attrName, args=list(args))

            else:
                raise AttributeError("Incorrect attribute accessor %s ", (accessor))

    def get__attrName(self,attrName,*args):           return self._attribute_accessor_execute('get_',attrName, *args)
    def set__attrName(self,attrName,attrValue,*args): self._attribute_accessor_execute('set_',attrName, attrValue, *args)
    def rst__attrName(self,attrName,*args):           return self._attribute_accessor_execute('rst_',attrName, *args)
    def getDefault__attrName(self,attrName,*args):    return self._attribute_accessor_execute('getDefault_',attrName, *args)
    def chkEq__attrName(self,attrName,*args):         return self._attribute_accessor_execute('chkEq_',attrName, *args)
    def chkType__attrName(self,attrName,*args):       return self._attribute_accessor_execute('chkType_',attrName, *args)
    def remove__attrName(self,attrName,*args):           return self._attribute_accessor_execute('remove_',attrName, attrValue, *args)
    def append__attrName(self,attrName,*args):           self._attribute_accessor_execute('append_',attrName, attrValue, *args)

    def __extractItems(self,value,args):
        if isinstance(args,list):
            arg=args.pop(0)
            if len(args)==0: args=None
        else:
            arg=args
            args=None
        
        outputValue=value[arg]
        
        if args!=None:
            return self.__extractItems(outputValue,args)
        else:
            return outputValue
        
    def __insertItems(self,attr,value,pos):
        if isinstance(pos,list):
            p=pos.pop(0)
            if len(pos) == 1: pos=pos[0]
            newAttr=attr[p]
            attr[p] = self.__insertItems(newAttr,value,pos)
            return attr
        else:
            attr[pos]=value
            return attr




if __name__ == '__main__':
    main(sys.argv[1:])
