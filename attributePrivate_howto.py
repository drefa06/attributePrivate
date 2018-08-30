#!/usr/bin/python
import sys
import pdb
import time

################################################################################
################################################################################
###    SOLUTION 1
################################################################################
################################################################################
class foo1_1(object):
    bar1_1   = 1100		#class attribute
    __bar2_1 = 1200		#private class attribute

    def __init__(self):
        self.bar3_1   = 1300	#attribute
        self.__bar4_1 = 1400	#protected attribute

    def inc1_bar1_1(self,val): 
        self.bar1_1+=val
        return self.bar1_1
    def inc2_bar1_1(self,val): 
        foo1_1.bar1_1+=val
        return foo1_1.bar1_1

    def inc1_bar2_1(self,val): 
        self.__bar2_1+=val
        return self.__bar2_1
    def inc2_bar2_1(self,val): 
        foo1_1.__bar2_1+=val
        return foo1_1.__bar2_1

    def inc1_bar3_1(self,val): 
        self.bar3_1+=val
        return self.bar3_1
    def inc2_bar3_1(self,val): 
        foo1_1.bar3_1+=val
        return foo1_1.bar3_1

    def inc1_bar4_1(self,val): 
        self.__bar4_1+=val
        return self.__bar4_1
    def inc2_bar4_1(self,val): 
        foo1_1.__bar4_1+=val
        return foo1_1.__bar4_1

################################################################################
################################################################################
class foo1_2(foo1_1):
    None      

################################################################################
################################################################################
def attribute1():
    print "\n====================================================================="
    print "===   ATTRIBUTE ACCESS TEST 1:"
    print "Create class instance x111=foo1_1() and x112=foo1_1()"
    x111=foo1_1()
    x112=foo1_1()
    print "Create class instance x12=foo1_2() inherited from foo1_1"
    x12=foo1_2()


    print "\nAccess to bar1_1, foo1_1 class attribute: "
    print "    1- x111.bar1_1          =",x111.bar1_1," ==> OK"
    print "       x112.bar1_1          =",x112.bar1_1," ==> OK"
    print "       foo1_1.bar1_1       =",foo1_1.bar1_1," ==> OK"
    print "       x12.bar1_1          =",x12.bar1_1," ==> OK"
    print "       foo1_2.bar1_1       =",foo1_2.bar1_1," ==> OK"

    x111.bar1_1 += 50
    print "    2- x111.bar1_1 += 50           ==> OK"
    print "        -> x111.bar1_1      = ",x111.bar1_1,"         #modif instance attribute"
    print "        -> x112.bar1_1      = ",x112.bar1_1,"         #modif instance attribute"
    print "        -> foo1_1.bar1_1   = ",foo1_1.bar1_1,"         #do not modif class attribute"
    print "        -> x12.bar1_1      = ",x12.bar1_1,"         #!!! Always seen as class attribute from inherited class"
    print "        -> foo1_2.bar1_1   = ",foo1_2.bar1_1,"         #!!! idem"
    x112.bar1_1 += 60
    print "    2- x112.bar1_1 += 60           ==> OK"
    print "        -> x111.bar1_1      = ",x111.bar1_1,"         #modif instance attribute"
    print "        -> x112.bar1_1      = ",x112.bar1_1,"         #modif instance attribute"
    print "        -> foo1_1.bar1_1   = ",foo1_1.bar1_1,"         #do not modif class attribute"
    print "        -> x12.bar1_1      = ",x12.bar1_1,"         #!!! Always seen as class attribute from inherited class"
    print "        -> foo1_2.bar1_1   = ",foo1_2.bar1_1,"         #!!! idem"
    foo1_1.bar1_1 += 70
    print "    6- foo1_1.bar1_1 += 60          ==> OK"
    print "        -> x111.bar1_1      = ",x111.bar1_1,"         #instance attribute not change"
    print "        -> x112.bar1_1      = ",x112.bar1_1,"         #modif instance attribute"
    print "        -> foo1_1.bar1_1   = ",foo1_1.bar1_1,"         #class attribute changed"
    print "        -> x12.bar1_1      = ",x12.bar1_1,"         #!!! Always seen as class attribute"
    print "        -> foo1_2.bar1_1   = ",foo1_2.bar1_1,"         #!!! idem"
    x12.bar1_1 += 80
    print "    7- x12.bar1_1 += 70           ==> OK"
    print "        -> x111.bar1_1      = ",x111.bar1_1,"         #modif instance attribute"
    print "        -> x112.bar1_1      = ",x112.bar1_1,"         #modif instance attribute"
    print "        -> foo1_1.bar1_1   = ",foo1_1.bar1_1,"         #do not modif class attribute"
    print "        -> x12.bar1_1      = ",x12.bar1_1,"         #!!! Always seen as class attribute from inherited class"
    print "        -> foo1_2.bar1_1   = ",foo1_2.bar1_1,"         #!!! idem"
    foo1_2.bar1_1 += 90
    print "    8- foo1_2.bar1_1 += 80          ==> OK"
    print "        -> x111.bar1_1      = ",x111.bar1_1,"         #instance attribute not change"
    print "        -> x112.bar1_1      = ",x112.bar1_1,"         #modif instance attribute"
    print "        -> foo1_1.bar1_1   = ",foo1_1.bar1_1,"         #class attribute changed"
    print "        -> x12.bar1_1      = ",x12.bar1_1,"         #!!! Always seen as class attribute"
    print "        -> foo1_2.bar1_1   = ",foo1_2.bar1_1,"         #!!! idem"

    print "    9- call increment method"
    print "        -> x111.inc1_bar1_1(1) = ",x111.inc1_bar1_1(1),"         # => x11.bar1_1 + 1"
    print "        -> x111.inc2_bar1_1(2) = ",x111.inc2_bar1_1(2),"         # => foo1_1.bar1_1 + 2"
    print "        -> x112.inc1_bar1_1(3) = ",x112.inc1_bar1_1(3),"         # => x11.bar1_1 + 1"
    print "        -> x112.inc2_bar1_1(5) = ",x112.inc2_bar1_1(5),"         # => foo1_1.bar1_1 + 2"
    print "        -> x12.inc1_bar1_1(7) = ",x12.inc1_bar1_1(7),"         # => x12.bar1_1 + 3"
    print "        -> x12.inc2_bar1_1(11) = ",x12.inc2_bar1_1(11),"         # => foo1_1.bar1_1 + 5"
    print "        -> foo1_1.inc1_bar1_1(x111,14) = ",foo1_1.inc1_bar1_1(x111,14),"         # => x11.bar1_1 + 7"
    print "        -> foo1_1.inc2_bar1_1(x111,17) = ",foo1_1.inc2_bar1_1(x111,17),"         # => foo1_1.bar1_1 + 11"
    print "        -> foo1_1.inc1_bar1_1(x112,19) = ",foo1_1.inc1_bar1_1(x112,19),"         # => x11.bar1_1 + 7"
    print "        -> foo1_1.inc2_bar1_1(x112,23) = ",foo1_1.inc2_bar1_1(x112,23),"         # => foo1_1.bar1_1 + 11"
    print "        -> foo1_2.inc1_bar1_1(x12,27) = ",foo1_2.inc1_bar1_1(x12,27),"         # => x12.bar1_1 + 14"
    print "        -> foo1_2.inc2_bar1_1(x12,29) = ",foo1_2.inc2_bar1_1(x12,29),"         # => foo1_1.bar1_1 + 17"

    print "\nAccess to bar2_1, foo1_1 private class attribute: "
    try:
        print "    1-  x111.__bar2_1          ",x111.__bar2_1
    except:
        print "==> ERROR private var cannot be accessed directly"
        print "        ->  x111._foo1_1__bar2_1    =",x111._foo1_1__bar2_1," ==> OK"
    try:
        print "    2-  foo1_1.__bar2_1       ",foo1_1.__bar2_1
    except:
        print "==> ERROR private var cannot be accessed directly"
        print "        ->  foo1_1._foo1_1__bar2_1 =",foo1_1._foo1_1__bar2_1," ==> OK"

    try:
        print "    3-  x12.__bar2_1          ",x12.__bar2_1
    except:
        print "==> ERROR private var cannot be accessed directly"
        print "        ->  x12._foo1_1__bar2_1    =",x12._foo1_1__bar2_1," ==> OK"
    try:
        print "    4-  foo1_2.__bar2_1       ",foo1_2.__bar2_1
    except:
        print "==> ERROR private var cannot be accessed directly"
        print "        ->  foo1_2._foo1_1__bar2_1 =",foo1_2._foo1_1__bar2_1," ==> OK"

    try:
        x111.__bar2_1 += 10
    except:
        print "    5- x111.__bar2_1 += 10            ==> ERROR"
        x111._foo1_1__bar2_1 += 10
        print "       => x111._foo1_1__bar2_1 += 10     ==> OK"
        print "           -> x11._foo1_1__bar2_1      = ",x111._foo1_1__bar2_1
        print "           -> foo1_1._foo1_1__bar2_1    = ",foo1_1._foo1_1__bar2_1

    try:
        foo1_1.__bar2_1 += 20
    except:
        print "    6- foo1_1.__bar2_1 += 20        ==> ERROR"
        foo1_1._foo1_1__bar2_1+=20
        print "       => foo1_1._foo1_1__bar2_1 += 20   ==> OK"
        print "           -> x111._foo1_1__bar2_1      = ",x111._foo1_1__bar2_1
        print "           -> foo1_1._foo1_1__bar2 _1   = ",foo1_1._foo1_1__bar2_1

    try:
        x12.__bar2_1 += 30
    except:
        print "    7- x12.__bar2_1 += 30            ==> ERROR"
        x12._foo1_1__bar2_1 += 30
        print "       => x12._foo1_1__bar2_1 += 30     ==> OK"
        print "           -> x12._foo1_1__bar2_1      = ",x12._foo1_1__bar2_1
        print "           -> foo1_2._foo1_1__bar2_1    = ",foo1_2._foo1_1__bar2_1

    try:
        foo1_2.__bar2_1 += 40
    except:
        print "    8- foo1_2.__bar2_1 += 40        ==> ERROR"
        foo1_2._foo1_1__bar2_1+=40
        print "       => foo1_2._foo1_1__bar2_1 += 40   ==> OK"
        print "           -> x12._foo1_1__bar2_1      = ",x12._foo1_1__bar2_1
        print "           -> foo1_2._foo1_1__bar2 _1   = ",foo1_2._foo1_1__bar2_1

    print "    9- call increment method"
    print "        -> x111.inc1_bar2_1(1) = ",x111.inc1_bar2_1(1),"         # => x111.bar2_1 + 1"
    print "        -> x111.inc2_bar2_1(2) = ",x111.inc2_bar2_1(2),"         # => foo1_1.bar2_1 + 2"
    print "        -> x12.inc1_bar2_1(3) = ",x12.inc1_bar2_1(3),"         # => x12.bar2_1 + 3"
    print "        -> x12.inc2_bar2_1(5) = ",x12.inc2_bar2_1(5),"         # => foo1_1.bar1_1 + 5"
    print "        -> foo1_1.inc1_bar2_1(x111,7) = ",foo1_1.inc1_bar2_1(x111,7),"         # => x111.bar2_1 + 7"
    print "        -> foo1_1.inc2_bar2_1(x111,11) = ",foo1_1.inc2_bar2_1(x111,11),"         # => foo1_1.bar2_1 + 11"
    print "        -> foo1_2.inc1_bar2_1(x12,14) = ",foo1_2.inc1_bar2_1(x12,14),"         # => x12.bar2_1 + 14"
    print "        -> foo1_2.inc2_bar2_1(x12,17) = ",foo1_2.inc2_bar2_1(x12,17),"         # => foo1_1.bar2_1 + 17"


    print "\nAccess to bar3_1, a foo1_1 attribute: "
    print "    1-  x111.bar3_1          =",x111.bar3_1," ==> OK"
    try:
        print "    2-  foo1_1.bar3 _1       =",foo1_1.bar3_1
    except:
        print "=> ERROR class cannot access instance attribute"

    print "    3-  x12.bar3_1          =",x12.bar3_1," ==> OK"
    try:
        print "    4-  foo1_2.bar3 _1       =",foo1_2.bar3_1
    except:
        print "=> ERROR class cannot access instance attribute"

    x111.bar3_1+=10
    print "    5- x111.bar3_1 += 10            ==> OK"
    print "        -> x111.bar3_1             = ",x111.bar3_1
    try:
        foo1_1.bar3_1+=20
    except:
        print "    6- foo1_1.bar3_1 += 20          ==> ERROR class cannot access instance attribute"
    x12.bar3_1+=30
    print "    7- x12.bar3_1 += 10            ==> OK"
    print "        -> x12.bar3_1             = ",x12.bar3_1
    try:
        foo1_2.bar3_1+=40
    except:
        print "    8- foo1_2.bar3_1 += 20          ==> ERROR class cannot access instance attribute"

    print "    9- call increment method"
    print "        -> x111.inc1_bar3_1(1) = ",x111.inc1_bar3_1(1),"         # => x111.bar2_1 + 1"
    try:
        print "        -> x111.inc2_bar3_1(2) = ",x111.inc2_bar3_1(2)
    except:
        print "==> ERROR"
    print "        -> x12.inc1_bar3_1(3) = ",x12.inc1_bar3_1(3),"         # => x12.bar2_1 + 1"
    try:
        print "        -> x12.inc2_bar3_1(5) = ",x12.inc2_bar3_1(5)
    except:
        print "==> ERROR"

    print "        -> foo1_1.inc1_bar3_1(x11,7) = ",foo1_1.inc1_bar3_1(x111,7),"         # => x11.bar2_1 + 7"
    try:
        print "        -> foo1_1.inc2_bar3_1(x11,11) = ",foo1_1.inc2_bar3_1(x111,11)
    except:
        print "==> ERROR"
    print "        -> foo1_2.inc1_bar3_1(x12,14) = ",foo1_2.inc1_bar3_1(x12,14),"         # => x12.bar2_1 + 7"
    try:
        print "        -> foo1_2.inc2_bar3_1(x12,17) = ",foo1_2.inc2_bar3_1(x12,17)
    except:
        print "==> ERROR"




    print "\nAccess to bar4_1: "
    try:
        print "    1-  x111.__bar4_1        =",x111.__bar4_1
    except:
        print "=> ERROR private var cannot be accessed directly"
        print "        -> x111._foo1_1__bar4_1   =",x111._foo1_1__bar4_1," ==> OK"
    try:
        print "    2-  foo1_1.__bar4_1       ",foo1_1.__bar4_1
    except:
        print "==> ERROR private var of instance class cannot be accessed"
    try:
        print "        ->  foo1_1._foo1_1__bar4_1 =",foo1_1._foo1_1__bar4_1
    except:
        print "==> ERROR idem like this"
    try:
        print "    3-  x12.__bar4_1        =",x12.__bar4_1
    except:
        print "=> ERROR "
        print "        -> x12._foo1_1__bar4_1   =",x12._foo1_1__bar4_1," ==> OK"
    try:
        print "    4-  foo1_2.__bar4_1       ",foo1_2.__bar4_1
    except:
        print "==> ERROR private var of instance class cannot be accessed"
    try:
        print "        ->  foo1_2._foo1_2__bar4_1 =",foo1_2._foo1_2__bar4_1
    except: 
        print "==> ERROR idem like this"

    try:
        x111.__bar4_1+=10
    except:
        print "    5- x11.__bar4_1 += 10          ==> ERROR "       
        x111._foo1_1__bar4_1+=10
        print "       => x111._foo1_1__bar4_1 += 10   ==> OK"
        print "           -> x111._foo1_1__bar4_1      = ",x111._foo1_1__bar4_1
    try:
        foo1_1.__bar4_1+=20
    except:
        print "    6- foo1_1.__bar4_1 += 20      ==> ERROR "

    try:
        x12.__bar4_1+=30
    except:
        print "    7- x12.__bar4_1 += 30          ==> ERROR "       
        x12._foo1_1__bar4_1+=30
        print "       => x12._foo1_1__bar4_1 += 30   ==> OK"
        print "           -> x12._foo1_1__bar4_1      = ",x12._foo1_1__bar4_1
    try:
        foo1_2.__bar4_1+=40
    except:
        print "    8- foo1_2.__bar4_1 += 40      ==> ERROR "


        print "    9- call increment method"
    print "        -> x111.inc1_bar4_1(1) = ",x111.inc1_bar4_1(1),"         #inc +1 on instance attribute"
    try:
        print "        -> x111.inc2_bar4_1(2) = ",x111.inc2_bar4_1(2),"         #inc +3 on class attribute"
    except:
        print "==> ERROR"
    print "        -> x12.inc1_bar4_1(3) = ",x12.inc1_bar4_1(3),"         #!!! Always seen as class attribute so inc +1 on class attribute"
    try:
        print "        -> x12.inc2_bar4_1(5) = ",x12.inc2_bar4_1(5),"         #idem so inc +3 on class attribute"
    except:
        print "==> ERROR"

    print "        -> foo1_1.inc1_bar4_1(x11,7) = ",foo1_1.inc1_bar4_1(x111,7),"         #!!!"
    try:
        print "        -> foo1_1.inc2_bar4_1(x11,11) = ",foo1_1.inc2_bar4_1(x111,11),"         #!!!"
    except:
        print "==> ERROR"
    print "        -> foo1_2.inc1_bar4_1(x12,14) = ",foo1_2.inc1_bar4_1(x12,14),"         #!!!"
    try:
        print "        -> foo1_2.inc2_bar4_1(x12,17) = ",foo1_2.inc2_bar4_1(x12,17),"         #!!!"
    except:
        print "==> ERROR"

################################################################################
def stress1():
    print "\n====================================================================="
    print "===   STRESS TEST 1:"
    start=time.time()
    x11=foo1_1()
    x12=foo1_2()
    duration=time.time()-start
    print "duration = ",duration*1000000,"us"

    start=time.time()
    x11.bar1_1=1000
    for i in range(1000000): x11.inc1_bar1_1(i)
    duration=time.time()-start
    print "x11.inc1_bar1_1: duration = ",duration
    start=time.time()
    x12.bar1_1=1000
    for i in range(1000000): x12.inc1_bar1_1(i)
    duration=time.time()-start
    print "x12.inc1_bar1_1: duration = ",duration

    start=time.time()
    x11.bar2_1=1000
    for i in range(1000000): x11.inc1_bar2_1(i)
    duration=time.time()-start
    print "x11.inc1_bar2_1, duration = ",duration
    start=time.time()
    x12.bar2_1=1000
    for i in range(1000000): x12.inc1_bar2_1(i)
    duration=time.time()-start
    print "x21.inc1_bar2_1, duration = ",duration

    start=time.time()
    x11.bar3_1=1000
    for i in range(1000000): x11.inc1_bar3_1(i)
    duration=time.time()-start
    print "x11.inc1_bar3_1, duration = ",duration
    start=time.time()
    x12.bar3_1=1000
    for i in range(1000000): x12.inc1_bar3_1(i)
    duration=time.time()-start
    print "x12.inc1_bar3_1, duration = ",duration

    start=time.time()
    x11.bar4_1=1000
    for i in range(1000000): x11.inc1_bar4_1(i)
    duration=time.time()-start
    print "x11.inc1_bar4_1, duration = ",duration
    start=time.time()
    x12.bar4_1=1000
    for i in range(1000000): x12.inc1_bar4_1(i)
    duration=time.time()-start
    print "x12.inc1_bar4_1, duration = ",duration


################################################################################
################################################################################
###    SOLUTION 2
################################################################################
################################################################################
class foo2_1:
    bar1   = 1100		#class attribute
    __bar2 = 1200		#protected class attribute

    def __init__(self):
        self.bar3   = 1300	#attribute
        self.__bar4 = 1400	#protected attribute

    #bar1 accessor
    def get_bar1_1(self): return self.bar1
    def set_bar1_1(self, val): self.bar1=val

    def get_bar1_2(self): return foo2_1.bar1
    def set_bar1_2(self, val): foo2_1.bar1=val

    @property
    def bar1_3(self):  return self.bar1
    @bar1_3.setter
    def bar1_3(self,val): self.bar1=val

    @property
    def bar1_4(self):  return foo2_1.bar1
    @bar1_4.setter
    def bar1_4(self,val): foo2_1.bar1=val

    def get_bar1_5(self): return self.bar1
    def set_bar1_5(self, val): self.bar1=val
    property(get_bar1_5,set_bar1_5)

    #bar2 accessor
    def get_bar2_1(self): return self.__bar2
    def set_bar2_1(self, val): self.__bar2=val

    def get_bar2_2(self): return foo2_1.__bar2
    def set_bar2_2(self, val): foo2_1.__bar2=val

    @property
    def bar2_3(self):  return self.__bar2
    @bar2_3.setter
    def bar2_3(self,val): self.__bar2=val

    @property
    def bar2_4(self):  return foo2_1.__bar2
    @bar2_4.setter
    def bar2_4(self,val): foo2_1.__bar2=val

    #bar3 accessor
    def get_bar3_1(self): return self.bar3
    def set_bar3_1(self, val): self.bar3=val

    @property
    def bar3_2(self):  return self.bar3
    @bar3_2.setter
    def bar3_2(self,val): self.bar3=val

    #bar4 accessor
    def get_bar4_1(self): return self.__bar4
    def set_bar4_1(self, val): self.__bar4=val

    @property
    def bar4_2(self):  return self.__bar4
    @bar4_2.setter
    def bar4_2(self,val): self.__bar4=val


    #increment method
    def inc_bar1_1(self,val):    self.set_bar1_1(self.get_bar1_1()+val)
    def inc_bar1_2(self,val):    self.set_bar1_2(self.get_bar1_2()+val)
    def inc_bar1_3(self,val):    self.bar1_3+=val
    def inc_bar1_4(self,val):    self.bar1_4+=val
    def inc_bar1_5(self,val):    self.set_bar1_5(self.get_bar1_5()+val)

    def inc_bar2_1(self,val):    self.set_bar2_1(self.get_bar2_1()+val)
    def inc_bar2_2(self,val):    self.set_bar2_2(self.get_bar2_2()+val)
    def inc_bar2_3(self,val):    self.bar2_3+=val
    def inc_bar2_4(self,val):    self.bar2_4+=val

    def inc_bar3_1(self,val):    self.set_bar3_1(self.get_bar3_1()+val)
    def inc_bar3_2(self,val):    self.bar3_2+=val

    def inc_bar4_1(self,val):    self.set_bar4_1(self.get_bar4_1()+val)
    def inc_bar4_2(self,val):    self.bar4_2+=val

################################################################################
class foo2_2(foo2_1):
    None

################################################################################
class class_A(object):
    bar1_1   = 0		#class attribute
    __bar2_1 = []		#"private" class attribute

    def __init__(self):
        self.bar3_1   = ""	#instance attribute
        self.__bar4_1 = {}	#"private" instance attribute

    def get__bar2_1(self):       return self.__bar2_1
    def set__bar2_1(self,value): 
        if isinstance(value,list):
            self.__bar2_1 = value
        else:
            raise TypeError("list is needed")
    def del__bar2_1(self):       del self.__bar2_1

################################################################################
################################################################################
def attribute2():
    print "\n====================================================================="
    print "===   ATTRIBUTE ACCESS TEST 2:"
    x21=foo2_1()
    x22=foo2_2()

    print "\nAccess to bar1: "
    print "     Without decorator"
    print "bar1-1-  x21.get_bar1_1() =",x21.get_bar1_1()
    print "bar1-2-  x21.get_bar1_1 =",x21.get_bar1_1
    print "bar1-3-  x21.get_bar1_2() =",x21.get_bar1_2()
    print "bar1-4-  x21.get_bar1_2 =",x21.get_bar1_2
    print "bar1-5-  foo2_1.get_bar1_1(x21) =",foo2_1.get_bar1_1(x21)
    print "bar1-6-  foo2_1.get_bar1_2(x21) =",foo2_1.get_bar1_2(x21)
    print "bar1-7-  x22.get_bar1_1() =",x22.get_bar1_1()
    print "bar1-8-  x22.get_bar1_1 =",x22.get_bar1_1
    print "bar1-9-  x22.get_bar1_2() =",x22.get_bar1_2()
    print "bar1-10-  x22.get_bar1_2 =",x22.get_bar1_2
    print "bar1-11-  foo2_2.get_bar1_1(x22) =",foo2_2.get_bar1_1(x22)
    print "bar1-12-  foo2_2.get_bar1_2(x22) =",foo2_2.get_bar1_2(x22)

    x21.set_bar1_1(x21.get_bar1_1()+10)
    print "bar1-13-  x21.set_bar1_1(x21.get_bar1_1()+10) => ",x21.get_bar1_1()
    x21.set_bar1_2(x21.get_bar1_2()+20)
    print "bar1-14-  x21.set_bar1_2(x21.get_bar1_2()+20) => ",x21.get_bar1_2()
    foo2_1.set_bar1_1(x21,foo2_1.get_bar1_1(x21)+30)
    print "bar1-15-  foo2_1.set_bar1_1(x21,foo2_1.get_bar1_1(x21)+30) => ",foo2_1.get_bar1_1(x21)
    foo2_1.set_bar1_2(x21,foo2_1.get_bar1_2(x21)+40)
    print "bar1-16-  foo2_1.set_bar1_2(x21,foo2_1.get_bar1_2(x21)+40) => ",foo2_1.get_bar1_2(x21)
    x22.set_bar1_1(x22.get_bar1_1()+50)
    print "bar1-17-  x22.set_bar1_1(x22.get_bar1_1()+50) => ",x22.get_bar1_1()
    x22.set_bar1_2(x22.get_bar1_2()+60)
    print "bar1-18-  x22.set_bar1_2(x22.get_bar1_2()+60) => ",x22.get_bar1_2()
    foo2_2.set_bar1_1(x22,foo2_2.get_bar1_1(x22)+70)
    print "bar1-19-  foo2_2.set_bar1_1(x22,foo2_2.get_bar1_1(x22)+70) => ",foo2_2.get_bar1_1(x22)
    foo2_2.set_bar1_2(x22,foo2_2.get_bar1_2(x22)+80)
    print "bar1-20-  foo2_2.set_bar1_2(x22,foo2_2.get_bar1_2(x22)+80) => ",foo2_2.get_bar1_2(x22)

    print "     With decorator"
    try:
        print "bar1-1-  x21.bar1_3() =",x21.bar1_3()
    except:
        print "=> ERROR: x21.bar1_3 is a 'int' => cannot be callable"
    print "bar1-2-  x21.bar1_3   =",x21.bar1_3
    try:
        print "bar1-3-  x21.bar1_4() =",x21.bar1_4()
    except:
        print "=> ERROR: x21.bar1_4 is a 'int' => cannot be callable"
    print "bar1-4-  x21.bar1_4   =",x21.bar1_4
    try:
        print "bar1-5-  x21.get_bar1_5() =",x21.get_bar1_5()
    except:
        print "=> ERROR: x21.get_bar1_5 is a 'int' => cannot be callable"
    print "bar1-4-  x21.get_bar1_5   =",x21.get_bar1_5

    print "bar1-2-  foo2_1.bar1_3   =",foo2_1.bar1_3
    try:
        print "bar1-2-  foo2_1.bar1_3(x21)   =",foo2_1.bar1_3(x21)
    except:
        print "=> ERROR: 'property' object is not callable"
    print "bar1-2-  foo2_1.bar1_4   =",foo2_1.bar1_4
    try:
        print "bar1-2-  foo2_1.bar1_4(x21)   =",foo2_1.bar1_4(x21)
    except:
        print "=> ERROR: 'property' object is not callable"
    try:
        print "bar1-5-  x22.bar1_3() =",x22.bar1_3()
    except:
        print "=> ERROR: x22.bar1_3 is a 'int' => cannot be callable"
    print "bar1-6-  x22.bar1_3   =",x22.bar1_3
    try:
        print "bar1-7-  x22.bar1_4() =",x22.bar1_4()
    except:
        print "=> ERROR: x22.bar1_4 is a 'int' => cannot be callable"
    print "bar1-8-  x22.bar1_4   =",x22.bar1_4

    x21.bar1_3=x21.bar1_3+10
    print "bar1-9-  x21.bar1_3=x21.bar1_3+10 => ",x21.bar1_3
    x21.bar1_4=x21.bar1_4+20
    print "bar1-10-  x21.bar1_4=x21.bar1_4+20 => ",x21.bar1_4
    x22.bar1_3=x22.bar1_3+30
    print "bar1-11-  x22.bar1_3=x22.bar1_3+30 => ",x22.bar1_3
    x22.bar1_4=x22.bar1_4+40
    print "bar1-12-  x22.bar1_4=x22.bar1_4+40 => ",x22.bar1_4
    x22.set_bar1_5(x22.get_bar1_5()+50)
    print "bar1-12-  x22.set_bar1_5(x22.get_bar1_5()+50) => ",x22.get_bar1_5()

    print "\nAccess to bar2: "
    print "     Without decorator"
    print "bar2-1-  x21.get_bar2_1() =",x21.get_bar2_1()
    print "bar2-2-  x21.get_bar2_1 =",x21.get_bar2_1
    print "bar2-3-  x21.get_bar2_2() =",x21.get_bar2_2()
    print "bar2-4-  x21.get_bar2_2 =",x21.get_bar2_2
    print "bar2-5-  foo2_1.get_bar2_1(x21) =",foo2_1.get_bar2_1(x21)
    print "bar2-6-  foo2_1.get_bar2_2(x21) =",foo2_1.get_bar2_2(x21)
    print "bar2-7-  x22.get_bar2_1() =",x22.get_bar2_1()
    print "bar2-8-  x22.get_bar2_1 =",x22.get_bar2_1
    print "bar2-9-  x22.get_bar2_2() =",x22.get_bar2_2()
    print "bar2-10-  x22.get_bar2_2 =",x22.get_bar2_2
    print "bar2-11-  foo2_2.get_bar2_1(x22) =",foo2_2.get_bar2_1(x22)
    print "bar2-12-  foo2_2.get_bar2_2(x22) =",foo2_2.get_bar2_2(x22)

    x21.set_bar2_1(x21.get_bar2_1()+10)
    print "bar2-13-  x21.set_bar2_1(x21.get_bar2_1()+10) => ",x21.get_bar2_1()
    x21.set_bar2_2(x21.get_bar2_2()+20)
    print "bar2-14-  x21.set_bar2_2(x21.get_bar2_2()+20) => ",x21.get_bar2_2()
    foo2_1.set_bar2_1(x21,foo2_1.get_bar2_1(x21)+30)
    print "bar2-15-  foo2_1.set_bar2_1(x21,foo2_1.get_bar2_1(x21)+30) => ",foo2_1.get_bar2_1(x21)
    foo2_1.set_bar2_2(x21,foo2_1.get_bar2_2(x21)+40)
    print "bar2-16-  foo2_1.set_bar2_2(x21,foo2_1.get_bar2_2(x21)+40) => ",foo2_1.get_bar2_2(x21)
    x22.set_bar2_1(x22.get_bar2_1()+50)
    print "bar2-17-  x22.set_bar2_1(x22.get_bar2_1()+50) => ",x22.get_bar2_1()
    x22.set_bar2_2(x22.get_bar2_2()+60)
    print "bar2-18-  x22.set_bar2_2(x22.get_bar2_2()+60) => ",x22.get_bar2_2()
    foo2_2.set_bar2_1(x22,foo2_2.get_bar2_1(x22)+70)
    print "bar2-19-  foo2_2.set_bar2_1(x22,foo2_2.get_bar2_1(x22)+70) => ",foo2_2.get_bar2_1(x22)
    foo2_2.set_bar2_2(x22,foo2_2.get_bar2_2(x22)+80)
    print "bar2-20-  foo2_2.set_bar2_2(x22,foo2_2.get_bar2_2(x22)+80) => ",foo2_2.get_bar2_2(x22)

    print "     With decorator"
    try:
        print "bar2-1- x21.bar2_3() =",x21.bar2_3()
    except:
        print "=> ERROR: x21.bar2_3 is a 'int' => cannot be callable"
    print "bar2-2- x21.bar2_3   =",x21.bar2_3
    print "bar2-3- x21.bar2_4   =",x21.bar2_4
    try:
        print "bar2-4-  x22.bar2_3() =",x22.bar2_3()
    except:
        print "=> ERROR: x22.bar2_3 is a 'int' => cannot be callable"
    print "bar2-5-  x22.bar2_3   =",x22.bar2_3
    print "bar2-6-  x22.bar2_4   =",x22.bar2_4
    x21.bar2_3=x21.bar2_3+10
    print "bar2-7-  x21.bar2_3=x21.bar2_3+10 => ",x21.bar2_3
    x21.bar2_4=x21.bar2_4+20
    print "bar2-8-  x21.bar2_4=x21.bar2_4+20 => ",x21.bar2_4
    x22.bar2_3=x22.bar2_3+30
    print "bar2-9-  x22.bar2_3=x22.bar2_3+10 => ",x22.bar2_3
    x22.bar2_4=x22.bar2_4+40
    print "bar2-10-  x22.bar2_4=x22.bar2_4+10 => ",x22.bar2_4


    print "\nAccess to bar3: "
    print "     Without decorator"
    print "bar3-1-  x21.get_bar3_1() =",x21.get_bar3_1()
    print "bar3-2-  x21.get_bar3_1 =",x21.get_bar3_1
    print "bar3-3-  foo2_1.get_bar3_1(x21) =",foo2_1.get_bar3_1(x21)
    print "bar3-4-  x22.get_bar3_1() =",x22.get_bar3_1()
    print "bar3-5-  x22.get_bar3_1 =",x22.get_bar3_1
    print "bar3-6-  foo2_2.get_bar3_1(x22) =",foo2_2.get_bar3_1(x22)
    x21.set_bar3_1(x21.get_bar3_1()+10)
    print "bar3-7-  x21.set_bar3_1(x21.get_bar3_1()+10) => ",x21.get_bar3_1()
    foo2_1.set_bar3_1(x21,foo2_1.get_bar3_1(x21)+30)
    print "bar3-8-  foo2_1.set_bar3_1(x21,foo2_1.get_bar3_1(x21)+30) => ",foo2_1.get_bar3_1(x21)
    x22.set_bar3_1(x22.get_bar3_1()+50)
    print "bar3-9-  x22.set_bar3_1(x22.get_bar3_1()+50) => ",x22.get_bar3_1()
    foo2_2.set_bar3_1(x22,foo2_2.get_bar3_1(x22)+70)
    print "bar3-10-  foo2_2.set_bar3_1(x22,foo2_2.get_bar3_1(x22)+70) => ",foo2_2.get_bar3_1(x22)

    print "     With decorator"
    try:
        print "bar3-1- x21.bar3_2() =",x21.bar3_2()
    except:
        print "=> ERROR: x21.bar3_2 is a 'int' => cannot be callable"
    print "bar3-2- x21.bar3_2   =",x21.bar3_2
    try:
        print "bar3-3-  x22.bar3_2() =",x22.bar3_2()
    except:
        print "=> ERROR: x22.bar3_2 is a 'int' => cannot be callable"
    print "bar3-4-  x22.bar3_2   =",x22.bar3_2
    x21.bar3_2=x21.bar3_2+10
    print "bar3-5-  x21.bar3_2=x21.bar3_2+10 => ",x21.bar3_2
    x22.bar3_2=x22.bar3_2+30
    print "bar3-6-  x22.bar3_2=x22.bar3_2+10 => ",x22.bar3_2


    print "\nAccess to bar4: "
    print "     Without decorator"
    print "bar4-1-  x21.get_bar4_1() =",x21.get_bar4_1()
    print "bar4-2-  x21.get_bar4_1 =",x21.get_bar4_1
    print "bar4-3-  foo2_1.get_bar4_1(x21) =",foo2_1.get_bar4_1(x21)
    print "bar4-4-  x22.get_bar4_1() =",x22.get_bar4_1()
    print "bar4-5-  x22.get_bar4_1 =",x22.get_bar4_1
    print "bar4-6-  foo2_2.get_bar4_1(x22) =",foo2_2.get_bar4_1(x22)
    x21.set_bar4_1(x21.get_bar4_1()+10)
    print "bar4-7-  x21.set_bar4_1(x21.get_bar4_1()+10) => ",x21.get_bar4_1()
    foo2_1.set_bar4_1(x21,foo2_1.get_bar4_1(x21)+30)
    print "bar4-8-  foo2_1.set_bar4_1(x21,foo2_1.get_bar4_1(x21)+30) => ",foo2_1.get_bar4_1(x21)
    x22.set_bar4_1(x22.get_bar4_1()+50)
    print "bar4-9-  x22.set_bar4_1(x22.get_bar4_1()+50) => ",x22.get_bar4_1()
    foo2_2.set_bar4_1(x22,foo2_2.get_bar4_1(x22)+70)
    print "bar4-10-  foo2_2.set_bar4_1(x22,foo2_2.get_bar4_1(x22)+70) => ",foo2_2.get_bar4_1(x22)

    print "     With decorator"
    try:
        print "bar4-1- x21.bar4_2() =",x21.bar4_2()
    except:
        print "=> ERROR: x21.bar4_2 is a 'int' => cannot be callable"
    print "bar4-2- x21.bar4_2   =",x21.bar4_2
    try:
        print "bar4-3-  x22.bar4_2() =",x22.bar4_2()
    except:
        print "=> ERROR: x22.bar4_2 is a 'int' => cannot be callable"
    print "bar4-4-  x22.bar4_2   =",x22.bar4_2
    x21.bar4_2=x21.bar4_2+10
    print "bar4-5-  x21.bar4_2=x21.bar4_2+10 => ",x21.bar4_2
    x22.bar4_2=x22.bar4_2+20
    print "bar4-6-  x22.bar4_2=x22.bar4_2+10 => ",x22.bar4_2

################################################################################
def stress2():
    print "\n====================================================================="
    print "===   STRESS TEST 2:"
    start=time.time()
    x11=foo2_1()
    x12=foo2_2()
    duration=time.time()-start
    print "duration = ",duration*1000000,"us"

    start=time.time()
    x11.bar1=1000
    for i in range(1000000): x11.inc_bar1_1(i)
    duration=time.time()-start
    print "x11.inc_bar1_1, duration = ",duration
    start=time.time()
    foo2_1.bar1=1000
    for i in range(1000000): x11.inc_bar1_2(i)
    duration=time.time()-start
    print "x11.inc_bar1_2, duration = ",duration
    start=time.time()
    x12.bar1=1000
    for i in range(1000000): x12.inc_bar1_1(i)
    duration=time.time()-start
    print "x12.inc_bar1_1, duration = ",duration
    start=time.time()
    foo2_2.bar1=1000
    for i in range(1000000): x12.inc_bar1_2(i)
    duration=time.time()-start
    print "x12.inc_bar1_2, duration = ",duration

    start=time.time()
    x11.bar2=1000
    for i in range(1000000): x11.inc_bar2_1(i)
    duration=time.time()-start
    print "x11.inc_bar2_1, duration = ",duration
    start=time.time()
    foo2_1.bar2=1000
    for i in range(1000000): x11.inc_bar2_2(i)
    duration=time.time()-start
    print "x11.inc_bar2_2, duration = ",duration
    start=time.time()
    x12.bar2=1000
    for i in range(1000000): x12.inc_bar2_1(i)
    duration=time.time()-start
    print "x12.inc_bar2_1, duration = ",duration
    start=time.time()
    foo2_2.bar2=1000
    for i in range(1000000): x12.inc_bar2_2(i)
    duration=time.time()-start
    print "x12.inc_bar2_2, duration = ",duration

    start=time.time()
    x11.bar3=1000
    for i in range(1000000): x11.inc_bar3_1(i)
    duration=time.time()-start
    print "x11.inc_bar3_1, duration = ",duration
    start=time.time()
    x11.bar3=1000
    for i in range(1000000): x11.inc_bar3_2(i)
    duration=time.time()-start
    print "x11.inc_bar3_2, duration = ",duration
    start=time.time()
    x12.bar3=1000
    for i in range(1000000): x12.inc_bar3_1(i)
    duration=time.time()-start
    print "x12.inc_bar3_1, duration = ",duration
    start=time.time()
    x12.bar3=1000
    for i in range(1000000): x12.inc_bar3_2(i)
    duration=time.time()-start
    print "x12.inc_bar3_2, duration = ",duration

    start=time.time()
    x11.bar4=1000
    for i in range(1000000): x11.inc_bar4_1(i)
    duration=time.time()-start
    print "x11.inc_bar4_1, duration = ",duration
    start=time.time()
    x11.bar4=1000
    for i in range(1000000): x11.inc_bar4_2(i)
    duration=time.time()-start
    print "x11.inc_bar4_2, duration = ",duration
    start=time.time()
    x11.bar4=1000
    for i in range(1000000): x12.inc_bar4_1(i)
    duration=time.time()-start
    print "x12.inc_bar4_1, duration = ",duration
    start=time.time()
    x12.bar4=1000
    for i in range(1000000): x12.inc_bar4_2(i)
    duration=time.time()-start
    print "x12.inc_bar4_2, duration = ",duration


################################################################################
################################################################################
###    SOLUTION 3
################################################################################
################################################################################
class foo3_1(object):
    __name__='foo3_1'

    def __init__(self):
        self.__public={
            'bar1':{'type':[int,long],'value':10}
        }
        self.__private={
            'bar2':{'type':[int,long],'value':20}
        }

        self._bar3=10


    def get_bar1(self): return self.__public['bar1']['value']
    def set_bar1(self,val):
        type_good=False
        for t in self.__public['bar1']['type']:
            if isinstance(val,t): 
                type_good=True
                break

        if not type_good: raise TypeError("bar1 must be %s " % str(self.__public['bar1']['type']))

        self.__public['bar1']['value']=val
    property(get_bar1,set_bar1)

    @property
    def bar1(self):       return self.__public['bar1']['value']
    @bar1.setter
    def bar1(self,val): 
        type_good=False
        for t in self.__public['bar1']['type']:
            if isinstance(val,t): 
                type_good=True
                break

        if not type_good: raise TypeError("bar1 must be %s " % str(self.__public['bar1']['type']))

        self.__public['bar1']['value']=val


    @property
    def bar2(self):       
        if self.__name__ != 'foo3_1':
            raise AttributeError("bar2 is Private attribute of class foo3_1 ")
        return self.__private['bar2']['value']
    @bar2.setter
    def bar2(self,val): 
        if self.__name__ != 'foo3_1':
            raise AttributeError("bar2 is Private attribute of class foo3_1 ")

        type_good=False
        for t in self.__private['bar2']['type']:
            if isinstance(val,t): 
                type_good=True
                break

        if not type_good: raise TypeError("bar2 must be %s " % str(self.__private['bar2']['type']))


        self.__private['bar2']['value']=val

    @property
    def bar3(self):       
        return self._bar3
    @bar3.setter
    def bar3(self,val): 
        self._bar3=val


    def inc_bar1_1(self,val):  self.set_bar1(self.get_bar1()+val)
    def inc_bar1_2(self,val):  self.bar1+=val
    def inc_bar2(self,val):    self.bar2+=val
    def inc_bar3(self,val):    self.bar3+=val



################################################################################
class foo3_2(foo3_1):
    __name__='foo3_2'


################################################################################
################################################################################
def attribute3():
    print "\n====================================================================="
    print "===   ATTRIBUTE ACCESS TEST 3:"
    x31=foo3_1()

    print "1-  x31.get_bar1()                 =",x31.get_bar1()
    print "3-  x31.bar1                       =",x31.bar1
    print "4-  x31._foo3_1__protected['bar1'] =",x31._foo3_1__public['bar1']

    x31.bar1 *= 2
    print "5-  x31.bar1 * 2                 =",x31.bar1
    
    try:
        x31.bar1 = 'toto'
    except Exception, err:
        print "6-  x31.bar1 = 'toto' ==> ERROR: ",str(err)


    x32=foo3_2()
    print "7-  x32.bar1 (public)         =",x32.bar1
    try:
        print "8-  x32.bar2 (private)           =",x32.bar2
    except Exception, err:
        print str(err)

################################################################################
def stress3():
    print "\n====================================================================="
    print "===   STRESS TEST 3:"
    start=time.time()
    x31=foo3_1()
    x32=foo3_2()
    duration=time.time()-start
    print "duration = ",duration*1000000,"us"

    start=time.time()
    x31.set_bar1(1000)
    for i in range(1000000): x31.inc_bar1_1(i)
    duration=time.time()-start
    print "x31.inc_bar1_1, duration = ",duration
    start=time.time()
    x31.bar1=1000
    for i in range(1000000): x31.inc_bar1_2(i)
    duration=time.time()-start
    print "x31.inc_bar1_2, duration = ",duration
    start=time.time()
    x32.set_bar1(1000)
    for i in range(1000000): x32.inc_bar1_1(i)
    duration=time.time()-start
    print "x32.inc_bar1_1, duration = ",duration
    start=time.time()
    x32.bar1=1000
    for i in range(1000000): x32.inc_bar1_2(i)
    duration=time.time()-start
    print "x32.inc_bar1_2, duration = ",duration
    
    start=time.time()
    x31.bar2=1000
    for i in range(1000000): x31.inc_bar2(i)
    duration=time.time()-start
    print "x31.inc_bar2, duration = ",duration

    start=time.time()
    x31.bar3=1000
    for i in range(1000000): x31.inc_bar3(i)
    duration=time.time()-start
    print "x31.inc_bar3, duration = ",duration
    start=time.time()
    x32.bar3=1000
    for i in range(1000000): x32.inc_bar3(i)
    duration=time.time()-start
    print "x32.inc_bar3, duration = ",duration

       
################################################################################
################################################################################
###    SOLUTION 4
################################################################################
################################################################################
class _attribute4:
    __name__= None
    __order = 'public'
    __type = int
    __value = None

    def __init__(self,name,val):
        self.__name__ = name
        self.__type   = val['type']
        self.__value  = val['value']
        self.__private = val['private']

    @property
    def value(self): return self.__value
    @value.setter
    def value(self,val):
        if not isinstance(val,self.__type):
            raise TypeError("%s must be %s " % (self.__name__,str(self.__type))) 
        self.__value = val

    @property
    def private(self): return self.__private    #readonly parameter


################################################################################
class foo4_1(object):
    __name__='foo4_1'
    __attr_init=False

    def __init__(self):
        # to be sure to create dictionnary only once
        if not self.__attr_init:
            self.__my_attribute=dict()
            self.__attr_init = True

        # create attribute bar1 and bar3 that can be called via accessor
        self.new_attributeValue('bar1',{'private':False,   'type':int, 'value':None})
        self.new_attributeValue('bar3',{'private':'foo4_1','type':int, 'value':None})


    #private method to set, get or del private attribute __attribute
    def __set__attribute(self,key,val):
        self.__my_attribute[key]=val

    def __get__attribute(self,inAttrName):
        if self.__my_attribute.has_key(inAttrName):
            if self.__my_attribute[inAttrName].private != False and self.__my_attribute[inAttrName].private != self.__name__:
                raise AttributeError("%s is Private attribute of class %s" % (inAttrName,self.__my_attribute[inAttrName].private))
            else:
                return self.__my_attribute[inAttrName]
        else:
            raise AttributeError("%s is not a known attribute" % (inAttrName,))

    def __del__attribute(self,inAttrName):
        if self.__my_attribute.has_key(inAttrName):
            del self.__my_attribute[inAttrName]
        else:
            raise AttributeError("%s is not a known attribute" % (inAttrName,))


    def __attributeValue(self, operation,attrName,newValue=None):
        if operation == 'new': 
            attr=_attribute4(attrName,newValue)
            self.__set__attribute(attrName,attr)

        elif operation == 'del':
            self.__del__attribute(attrName)

        else:
            attr=self.__get__attribute(attrName)

            if operation == 'get':
                return attr.value
            elif operation == 'set':
                attr.value=newValue
                self.__set__attribute(attrName,attr)

    #public accessor to __attribute via private intermediate private methode __attributeValue
    def get_attributeValue(self,attrName):          return self.__attributeValue('get',attrName)
    def set_attributeValue(self,attrName,newValue): self.__attributeValue('set',attrName,newValue)
    def new_attributeValue(self,attrName,newValue): self.__attributeValue('new',attrName,newValue)
    def del_attributeValue(self,attrName):          self.__attributeValue('del',attrName)

    @property
    def bar1(self): return self.get_attributeValue('bar1')
    @bar1.setter
    def bar1(self,val): self.set_attributeValue('bar1',val)

    @property
    def bar3(self): return self.get_attributeValue('bar3')
    @bar3.setter
    def bar3(self,val): self.set_attributeValue('bar3',val)


    def inc_bar1(self,val): self.bar1+=val
    def inc_bar3(self,val): self.bar3+=val

################################################################################
class foo4_2(foo4_1):
    __name__='foo4_2'

    def __init__(self):
        foo4_1.__init__(self)

        self.new_attributeValue('bar2',{'private':False,     'type':int, 'value':None})
        self.new_attributeValue('bar4',{'private':'foo4_2', 'type':int, 'value':None})

    @property
    def bar2(self): return self.get_attributeValue('bar2')
    @bar2.setter
    def bar2(self,val): self.set_attributeValue('bar2',val)

    @property
    def bar4(self): return self.get_attributeValue('bar4')
    @bar4.setter
    def bar4(self,val): self.set_attributeValue('bar4',val)

    def inc_bar2(self,val): self.bar2+=val
    def inc_bar4(self,val): self.bar4+=val


################################################################################
class foo4_3(foo4_2):
    __name__='foo4_3'

    def __init__(self):
        foo4_2.__init__(self)

        self.new_attributeValue('bar5',{'private':False, 'type':str, 'value':''})
        self.new_attributeValue('bar7',{'private':'foo4_3', 'type':dict, 'value':{}})

    @property
    def bar5(self): return self.get_attributeValue('bar5')
    @bar5.setter
    def bar5(self,val): self.set_attributeValue('bar5',val)

    @property
    def bar7(self): return self.get_attributeValue('bar7')
    @bar7.setter
    def bar7(self,val): self.set_attributeValue('bar7',val)

################################################################################
class foo4_4(foo4_1):
    __name__='foo4_4'

    def __init__(self):
        foo4_1.__init__(self)

        self.new_attributeValue('bar6',{'private':False, 'type':list, 'value':[]})
        self.new_attributeValue('bar8',{'private':'foo4_4','type':long, 'value':1000000000})

    @property
    def bar6(self): return self.get_attributeValue('bar6')
    @bar6.setter
    def bar6(self,val): self.set_attributeValue('bar6',val)

    @property
    def bar8(self): return self.get_attributeValue('bar8')
    @bar8.setter
    def bar8(self,val): self.set_attributeValue('bar8',val)

################################################################################
class foo4_5(foo4_3,foo4_4):
    __name__='foo4_5'

    def __init__(self):
        foo4_3.__init__(self)
        foo4_4.__init__(self)

        self.new_attributeValue('bar9',{'private':'foo4_5', 'type':int, 'value':0})

    @property
    def bar9(self): return self.get_attributeValue('bar9')
    @bar9.setter
    def bar9(self,val): self.set_attributeValue('bar9',val)

################################################################################
################################################################################
def attribute4():
    print "\n====================================================================="
    print "===   ATTRIBUTE ACCESS TEST 4:"
    x41=foo4_1()
    x42=foo4_2()

    x45=foo4_5()

    print "1-  read x41.bar1 =",x41.bar1
    print "    read x41.bar3 =",x41.bar3
    print "    set x41.bar1 = 10"

    x41.bar1 = 10
    print "    => x41.bar1 =",x41.bar1
    print "    set x41.bar3 = 30"
    x41.bar3 = 30
    print "    => x41.bar3 =",x41.bar3

    print "2-  read x42.bar1 =",x42.bar1
    try:
        print "    read x42.bar3 =",x42.bar3
    except Exception,err:
        print str(err)
    print "    set x42.bar1 = 20"
    x42.bar1 = 20
    print "   => x42.bar1 =",x42.bar1
    try:
        print "    set x42.bar3 = 40"
        x42.bar3 = 40
    except Exception,err:
        print str(err)

    print "    read x42.bar2 =",x42.bar2
    print "    read x42.bar4 =",x42.bar4
    print "    set x42.bar2 = 50"
    x42.bar2 = 50
    print "    => x42.bar2 =",x42.bar2
    print "    set x42.bar4 = 60"
    x42.bar4 = 60
    print "    => x42.bar4 =",x42.bar4
    
    try:
        print "13-  read x41.bar5 =",x41.bar5
    except Exception,err:
        print str(err)
    
    try:
        print "14-  read x42.bar5 =",x42.bar5
    except Exception,err:
        print str(err)

    #pdb.set_trace()
    print "14-  read x45.bar1 =",x45.bar1
    print "     read x45.bar2 =",x45.bar2
    try:
        print "     read x45.bar3 =",x45.bar3
    except Exception,err:
        print str(err)
    try:
        print "     read x45.bar4 =",x45.bar4
    except Exception,err:
        print str(err)
    print "     read x45.bar5 =",x45.bar5
    print "     read x45.bar6 =",x45.bar6
    try:
        print "     read x45.bar7 =",x45.bar7
    except Exception,err:
        print str(err)
    try:
        print "     read x45.bar8 =",x45.bar8
    except Exception,err:
        print str(err)
    print "     read x45.bar9 =",x45.bar9

    print "15- set  x45.bar1 = 10"
    x45.bar1 = 10
    print "     => x45.bar1 =",x45.bar1

    print "    set x45.bar2 = 20"
    x45.bar2 = 20
    print "     => x45.bar2 =",x45.bar2
    print "     set x45.bar5 = \"Hello\""
    x45.bar5 = "Hello"
    print "     => x45.bar5 =",x45.bar5
    print "     set x45.bar6 = {1: \"oui\", 2:\"non\"}"
    x45.bar6 = {1: "oui", 2:"non"}
    print "     => x45.bar6 =",x45.bar6 
    print "     set x45.bar9 = 1000"
    x45.bar9 = 1000
    print "     => x45.bar9 =",x45.bar9

    print x41.__dict__
    print x42.__dict__
    print x45.__dict__

################################################################################
def stress4():
    print "\n====================================================================="
    print "===   STRESS TEST 4:"
    start=time.time()
    x41=foo4_1()
    x42=foo4_2()
    duration=time.time()-start
    print "duration = ",duration*1000000,"us"

    x41.bar1=1000
    for i in range(1000000): x41.inc_bar1(i)
    duration=time.time()-start
    print "x41.inc_bar1, duration = ",duration
    start=time.time()
    x42.bar1=1000
    for i in range(1000000): x42.inc_bar1(i)
    duration=time.time()-start
    print "x42.inc_bar1, duration = ",duration
    
    start=time.time()
    x42.bar2=1000
    for i in range(1000000): x42.inc_bar2(i)
    duration=time.time()-start
    print "x42.inc_bar2, duration = ",duration

    start=time.time()
    x41.bar3=1000
    for i in range(1000000): x41.inc_bar3(i)
    duration=time.time()-start
    print "x41.inc_bar3, duration = ",duration

    start=time.time()
    x42.bar4=1000
    for i in range(1000000): x42.inc_bar4(i)
    duration=time.time()-start
    print "x42.inc_bar4, duration = ",duration


################################################################################
################################################################################
###    SOLUTION 5
################################################################################
################################################################################
import re

class _attribute5:
    __name__  = None
    __type    = int
    __value   = None
    __private = False
    __default = None

    def __init__(self,name,val):
        self.__name__  = name
        self.__type    = val['type']
        self.__value   = val['value']
        self.__private = val['private']
        self.__default = val['value']

    @property
    def value(self): return self.__value
    @value.setter
    def value(self,val):
        if not isinstance(val,self.__type):
            raise TypeError("Incorrect type %s it must be %s " % (self.__name__,str(self.__type))) 
        self.__value = val

    @property
    def private(self): return self.__private    #readonly parameter
    @property
    def default(self): return self.__default    #readonly parameter
    @property
    def type(self):    return self.__type       #readonly parameter
  

################################################################################
class attribute_ctrl:
    __attribute_accessor = ['has_','get_','set_','setItems_','rst_','getDefault_','chkEq_','chkType_']

    def __init__(self):
        self.__my_attribute=dict()

    def __getattr__(self,attr):
        my_accessor = re.split('__',attr)[0]+'_'		#'__' for debug, '_' unless
        
        if my_accessor in self.__attribute_accessor and attr.startswith(my_accessor):
            attrName =re.sub(r'^'+my_accessor+'_','',attr)	#r'^'+cmd+'_' for debug, r'^'+cmd unless
            return lambda *x: self._attribute_accessor_execute(my_accessor,attrName,*x)

        else:
            raise AttributeError("Undefined attribute "+attr)

    #Attribute creation/deletion
    def new__attribute(self,attrName,attrValue):
        if self.__my_attribute.has_key(attrName):
            raise AttributeError("Cannot recreate an existing attribute: %s" % (attrName,))
        
        attr=_attribute5(attrName,attrValue)
        self.__my_attribute[attrName]=attr

        #setattr(self, attrName, attr.default)

    def del__attribute(self,attrName):
        if not self.__my_attribute.has_key(attrName):
            raise AttributeError("Cannot delete a missing attribute: %s" % (attrName,))

        del self.__my_attribute[attrName]


    def has__attribute(self,attrName):
        return  self.__my_attribute.has_key(attrName) 


    #private method to set, get or del private attribute __attribute
    def _set__attribute(self,attrName,args):
        if len(args) > 1:
            newValue = self.__insertItems(self.__my_attribute[attrName].value,args[0], args[1])

            self.__my_attribute[attrName].value=newValue
        else:
            myTypeIsGood=False
            if isinstance(self.__my_attribute[attrName].type,list):
                
                for t in self.__my_attribute[attrName].type:
                    if isinstance(args[0],t): 
                        myTypeIsGood = True
                        break
                
            elif isinstance(args[0],self.__my_attribute[attrName].type):
                myTypeIsGood = True

            if not myTypeIsGood:
                raise TypeError("%s: Incorrect type %s it must be %s " % (args[0],str(type(args[0])),str(self.__my_attribute[attrName].type))) 

            self.__my_attribute[attrName].value=args[0]

    def _get__attribute(self,attrName, args=[]):
        value = self.__my_attribute[attrName].value
        if len(args) > 0: 
            value = self.__extractItems(value, args[0])
        return value

    def _rst__attribute(self,attrName):
        self.__my_attribute[attrName].value=self.__my_attribute[attrName].default

    def _getDefault__attribute(self,attrName):
        return self.__my_attribute[attrName].default

    def _checkEqual__attribute(self,attrName,args):
        return  self.__my_attribute[attrName].value == args[0]

    def _checkType__attribute(self,attrName,args):
        myTypeIsGood=False
        if isinstance(self.__my_attribute[attrName].type,list):
            for t in self.__my_attribute[attrName].type:
                if isinstance(args[0],t): 
                    myTypeIsGood = True
                    break
                
        elif isinstance(args[0],self.__my_attribute[attrName].type):
            myTypeIsGood = True

        return  myTypeIsGood


    def _attribute_accessor_execute(self,accessor,attrName, *args):
        if accessor.startswith('has_'):		return self.has__attribute(attrName)
        else:
            if not self.has__attribute(attrName): raise AttributeError("Undefined variable "+attrName)
            if self.__my_attribute[attrName].private != False and self.__my_attribute[attrName].private != self.__name__:
                raise AttributeError("%s is Private attribute of class %s" % (attrName,self.__my_attribute[attrName].private))

            if accessor.startswith('get_'):          return self._get__attribute(attrName, args=list(args))
            elif accessor.startswith('set_'):        return self._set__attribute(attrName, args=list(args))
            elif accessor.startswith('rst_'):        return self._rst__attribute(attrName)
            elif accessor.startswith('getDefault_'): return self._getDefault__attribute(attrName)
            elif accessor.startswith('chkEq_'):      return self._checkEqual__attribute(attrName, args=list(args))
            elif accessor.startswith('chkType_'):    return self._chkType__attribute(attrName, args=list(args))
            else:
                raise AttributeError(attrName)

    def get__attrName(self,attrName,*args):           return self._attribute_accessor_execute('get_',attrName, *args)
    def set__attrName(self,attrName,attrValue,*args): self._attribute_accessor_execute('set_',attrName, attrValue, *args)
    def rst__attrName(self,attrName,*args):           return self._attribute_accessor_execute('rst_',attrName, *args)
    def getDefault__attrName(self,attrName,*args):    return self._attribute_accessor_execute('getDefault_',attrName, *args)
    def chkEq__attrName(self,attrName,*args):         return self._attribute_accessor_execute('chkEq_',attrName, *args)
    def chkType__attrName(self,attrName,*args):       return self._attribute_accessor_execute('chkType_',attrName, *args)


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
       


################################################################################
class foo5_1(attribute_ctrl):
    __name__='foo5_1'

    def __init__(self):
        attribute_ctrl.__init__(self)

        # create attribute bar1 and bar3 that can be called via accessor
        self.new__attribute('bar1',{'private':False,   'type':[int,long], 'value':0})
        self.new__attribute('bar2',{'private':'foo5_1','type':[int,long],  'value':100})
        self.new__attribute('bar3',{'private':'foo5_1','type':list, 'value':[]})

    def get__bar1(self,*args):       return self.get__attrName('bar1',*args)
    def set__bar1(self,value,*args): self.set__attrName('bar1',value,*args)

    def inc_bar1(self,val): self.set__bar1(self.get__bar1() + val)
    def inc_bar2(self,val): self.set__bar2(self.get__bar2() + val)


################################################################################
class foo5_2(attribute_ctrl,foo5_1):
    __name__='foo5_2'

    def __init__(self):
        foo5_1.__init__(self)

        # create attribute bar1 and bar3 that can be called via accessor
        self.new__attribute('bar4',{'private':False,   'type':dict, 'value':{}})
        self.new__attribute('bar5',{'private':'foo5_2','type':[int,long],  'value':0})
        self.new__attribute('bar6',{'private':'False','type':list, 'value':[]})

    def inc_bar5(self,val): self.set__bar5(self.get__bar5() + val)


################################################################################
################################################################################
def attribute5():
    print "\n====================================================================="
    print "===   ATTRIBUTE ACCESS TEST 5:"
    x51=foo5_1()
    x52=foo5_2()

    print "1-  read x51.bar1 =",x51.get__bar1()
    print "    read x51.bar2 =",x51.get__bar2()
    print "    set x51.bar1 = 10"
    x51.set__bar1(10)
    print "    => x51.bar1 =",x51.get__bar1()
    print "    set x51.bar2 = 30"
    x51.set__bar2(30)
    print "    => x51.bar2 =",x51.get__bar2()

    print "2-  read x52.bar1 =",x52.get__bar1()
    try:
        print "    read x52.bar2 =",x52.get__bar2()
    except Exception,err:
        print str(err)
    print "    set x52.bar1 = 20"
    x52.set__bar1(20)
    print "   => x52.bar1 =",x52.get__bar1()
    try:
        print "    set x52.bar2 = 40"
        x52.set__bar2(40)
    except Exception,err:
        print str(err)

    print "    read x52.bar4 =",x52.get__bar4()
    print "    read x52.bar5 =",x52.get__bar5()
    print "    set x52.bar4 = 50"
    x52.set__bar4({'val':50})
    print "    => x52.bar4 =",x52.get__bar4()
    print "    set x52.bar5 = 60"
    x52.set__bar5(60)
    print "    => x52.bar5 =",x52.get__bar5()
    
    try:
        print "13-  read x51.bar5 =",x51.get__bar4()
    except Exception,err:
        print str(err)
    
    try:
        print "14-  read x52.bar5 =",x52.get__bar5()
    except Exception,err:
        print str(err)

    x51.set__bar3([1,2,"trois",4,[51,52,53],6,7,{'81':1,'82':4,'83':2},9,0])
    print "2nd element = ",x51.get__bar3(1)
    print "3rd element = ",x51.get__bar3(2)
    print "3rd part of 5th element = ",x51.get__bar3([4,2])
    print "index '81' of 7th element = ",x51.get__bar3([7,'81'])

    x51.set__bar3("deux",1)
    print x51.get__bar3()
    x51.set__bar3([31,32],3)
    print x51.get__bar3()
    x51.set__bar3(54,[4,2])
    print x51.get__bar3()
    x51.set__bar3(3,[7,'81'])
    print x51.get__bar3()


    print x51.__dict__
    print x52.__dict__


################################################################################
def stress5():
    print "\n====================================================================="
    print "===   STRESS TEST 5:"
    start=time.time()
    x51=foo5_1()
    x52=foo5_2()
    duration=time.time()-start
    print "duration = ",duration*1000000,"us"

    x51.set__bar1(1000)
    for i in range(1000000): x51.inc_bar1(i)
    duration=time.time()-start
    print "x51.inc_bar1, duration = ",duration
    start=time.time()
    x52.set__bar1(1000)
    for i in range(1000000): x52.inc_bar1(i)
    duration=time.time()-start
    print "x52.inc_bar1, duration = ",duration
    
    start=time.time()
    x51.set__bar2(1000)
    for i in range(1000000): x51.inc_bar2(i)
    duration=time.time()-start
    print "x51.inc_bar2, duration = ",duration

    start=time.time()
    x52.set__bar5(1000)
    for i in range(1000000): x52.inc_bar5(i)
    duration=time.time()-start
    print "x52.inc_bar5_1, duration = ",duration



################################################################################
################################################################################
###    MAIN
################################################################################
################################################################################
def main(args):
    attribute1()
    attribute2()
    attribute3()
    attribute4()
    attribute5()
    stress1()
    stress2()
    stress3()
    stress4()
    stress5()


if __name__ == '__main__':
    main(sys.argv[1:])
