#!/usr/bin/env python

##
# If this module is run as a stand-alone application, import the parent package __init__.py file.
# The set_lib_package_path() function will be called to define the "lib" package path (before the following imports).
#
if __name__ == "__main__":
    import __init__

import lib
import unittest
import pdb, os, re, sys, os.path, shutil, time

from lib import attribute
from lib.attribute import attribute_ctrl
from lib.superTypes import *

class testA(attribute_ctrl):
    __class_name__="testA"

    __typedictA={
            'a': slist,
            'b': istr,
            'c': list
            }

    def __init__(self):
        attribute_ctrl.__init__(self)

        self.new__attribute('bar1',{'owner':None, 'type':istr,       'value':'0'})
        self.new__attribute('bar2',{'owner':'testA',  'type':[int,long], 'value':100})
        self.new__attribute('bar3',{'owner':'testA',  'type':islist,     'value':['0']})
        self.new__attribute('bar4',{'owner':'testA',  'type':make_dictType('dictA',elemType=self.__typedictA),     'value':{'a':['fabrice','aurelie'],'b':'123','c':['45','38']}})

    def get__bar1(self,*args):       return self.get__attrName('bar1',*args)
    def set__bar1(self,value,*args): self.set__attrName('bar1',value,*args)
    def get__bar2(self,*args):       return self.get__attrName('bar2',*args)
    def set__bar2(self,value,*args): self.set__attrName('bar2',value,*args)
    def get__bar3(self,*args):       return self.get__attrName('bar3',*args)
    def set__bar3(self,value,*args): self.set__attrName('bar3',value,*args)
    def get__bar4(self,*args):       return self.get__attrName('bar4',*args)
    def set__bar4(self,value,*args): self.set__attrName('bar4',value,*args)

    @accept_types(None,int)
    def inc_bar1(self,val):
        self.set__bar1(str(int(self.get__bar1())+val))
    def inc_bar2(self,val):
        self.set__bar2(self.get__bar2()+val)
    def inc_bar3(self,val):
        a=self.get__bar3()
        if isinstance(val,int):
            for i,v in enumerate(a): a[i]=str(int(v)+val)
            self.set__bar3(a)
        elif isinstance(val,list) and len(val) == len(a):
            for i,v in enumerate(a): a[i]=str(int(v)+int(val[i]))
            self.set__bar3(a)

class testB(testA):
    __class_name__="testB"

    def __init__(self):
        testA.__init__(self)

        self.new__attribute('bar5',{'owner':None, 'type':dict, 'value':{}})
        self.new__attribute('bar6',{'owner':'testB', 'type':[int,long], 'value':0})
        self.new__attribute('bar7',{'owner':'testB', 'type':list, 'value':[1,2,3]})

    def get__bar5(self,*args):       return self.get__attrName('bar5',*args)
    def set__bar5(self,value,*args): self.set__attrName('bar5',value,*args)
    def get__bar6(self,*args):       return self.get__attrName('bar6',*args)
    def set__bar6(self,value,*args): self.set__attrName('bar6',value,*args)

    def inc_bar6(self,val):
        self.set__bar6(self.get__bar6()+val)

##############################################################################################
##############################################################################################
##############################################################################################
class test_attribute(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    #=====================================================
    def test_00_attributeElem(self):
         self.assertRaises(TypeError, attribute._attribute)
         self.assertRaises(TypeError, attribute._attribute, 'test')
         self.assertRaises(TypeError, attribute._attribute, 'test', 0)
         self.assertRaises(KeyError,  attribute._attribute, 'test',{'val':0})
         self.assertRaises(KeyError, attribute._attribute, 'test',{'value':0,'type':list,'private':True})
         self.assertRaises(TypeError, attribute._attribute, 'test',{'value':0,'type':list,'private':True,'private':'toto','owner':'test'})

         A = attribute._attribute('test',{'value':[1,2],'type':list,'private':False,'owner':'test'})
         B = attribute._attribute('test',{'value':['1','2'],'type':islist,'private':True,'owner':'test'})
         self.assertTrue(isinstance(A,attribute._attribute))
         self.assertTrue(isinstance(B,attribute._attribute))

         self.assertEqual(A.value,[1,2])
         self.assertEqual(B.value,['1','2'])
         self.assertEqual(B.default,B.value)
         self.assertEqual(A.private,False)
         self.assertEqual(B.private,True)
         self.assertEqual(A.type,list)
         self.assertEqual(B.type,islist)

         self.assertRaises(TypeError, A.set_value, 3)
         self.assertRaises(TypeError, A.set_value, 'test')
         A.set_value([3])
         self.assertEqual(A.value,[3])
         self.assertRaises(TypeError, B.set_value, [3])
         B.set_value(['3'])
         self.assertEqual(B.value,['3'])



    def test_01_attribute_ctrl_new_has_del(self):
        A = attribute_ctrl()

        class test: pass
        self.assertFalse(A.has__attribute(test))
        self.assertRaises(AttributeError, A.del__attribute, test)
        self.assertRaises(TypeError, A.new__attribute, test)

        self.assertFalse(A.has__attribute('test'))
        self.assertRaises(TypeError, A.new__attribute, 'test')
        self.assertRaises(AttributeError, A.new__attribute, 'test','test')

        A.new__attribute('test',{'value':[1,2],'type':list,'private':False,'owner':'test'})
        self.assertTrue(A.has__attribute('test'))
        self.assertRaises(AttributeError, A.new__attribute, 'test',{'value':[1,2],'type':list,'private':False,'owner':'test'})

        A.del__attribute('test')
        self.assertFalse(A.has__attribute('test'))
        self.assertRaises(AttributeError, A.del__attribute, 'test')


    def test_02_attribute_usage(self):
        A=testA()
        B=testB()

        self.assertEqual(A.get__bar1(),'0')
        self.assertEqual(A.get__bar2(),100)

        self.assertRaises(TypeError,A.set__bar1,10)
        A.set__bar1('10')
        self.assertEqual(A.get__bar1(),'10')
        A.set__bar2(30)
        self.assertEqual(A.get__bar2(),30)

        self.assertEqual(B.get__bar1(),'0')

        self.assertRaises(AttributeError,B.get__bar2)
        self.assertRaises(AttributeError,B.set__bar2,40)

        self.assertRaises(TypeError,B.set__bar1,20)
        B.set__bar1('20')
        self.assertEqual(B.get__bar1(),'20')
        
        self.assertEqual(B.get__bar5(),{})
        self.assertEqual(B.get__bar6(),0)
        B.set__bar5({'val':50})
        B.set__bar6(60)
        self.assertEqual(B.get__bar5(),{'val':50})
        self.assertEqual(B.get__bar6(),60)
    
        self.assertRaises(AttributeError,A.get__bar5)

        self.assertEqual(B.get__bar7(),[1,2,3])
        B.set__bar7([1,2,"trois",4,[51,52,53],6,7,{'81':1,'82':4,'83':2},9,0])
        self.assertEqual(B.get__bar7(1),2)
        self.assertEqual(B.get__bar7(2),"trois")

        self.assertEqual(B.get__bar7([4,2]),53)
        self.assertEqual(B.get__bar7([7,'81']),1)

        B.set__bar7("deux",1)
        B.set__bar7([41,42],3)
        B.set__bar7(535,[4,2])
        B.set__bar7(3,[7,'81'])
        self.assertTrue(B.chkEq__bar7([1, 'deux', 'trois', [41, 42], [51, 52, 535], 6, 7, {'82': 4, '83': 2, '81': 3}, 9, 0]))

        B.rst__bar7()
        self.assertEqual(B.get__bar7(),[1,2,3])

        self.assertRaises(TypeError,A.set__bar4,{'a':'123', 'b':'123','c': [1, 'a']})
        A.set__bar4({'a':['a', '1'], 'b':'123','c': [1, 'a']})
        A.set__bar4(['something','else'],'e')
        A.set__bar4(['a', '1', '2'],'a')
        self.assertEqual(A.get__bar4(),{'a':['a', '1', '2'], 'b':'123','c': [1, 'a'],'e':['something','else']})

        print "Nb attribute created: {}".format(A.get_nb_attribute())

    #=====================================================
    def test_03_attribute_performance(self):

        print "\nSTRESS TEST:"
        start=time.time()
        A=testA()
        B=testB()
        duration=time.time()-start
        print "duration = ",duration*1000000,"us"

        start=time.time()
        A.set__bar1('1000')
        for i in range(1000000): A.inc_bar1(i)
        duration=time.time()-start
        print "A.inc_bar1, duration = ",duration

        start=time.time()
        B.set__bar1('1000')
        for i in range(1000000): B.inc_bar1(i)
        duration=time.time()-start
        print "B.inc_bar1, duration = ",duration

        start=time.time()
        B.set__bar6(1000)
        pdb.set_trace()
        for i in range(1000000): B.inc_bar6(i)
        duration=time.time()-start
        print "B.inc_bar5,6 duration = ",duration


    #=====================================================
    def test_04_pickler_performance(self):
        import pickle
        A=testA()
        
        with open("donnees",'wb') as fichier:
            mon_pickler = pickle.Pickler(fichier)
            mon_pickler.dump(A)


        with open("donnees",'rb') as fichier:
            mon_depickler = pickle.Unpickler(fichier)
            new_A = mon_depickler.load()



##
# If this module is run as a stand-alone application, call the main() function.
#
if __name__ == "__main__":
    unittest.main()
