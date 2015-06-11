#*- coding: utf-8 -*
class info(object):

   @classmethod
   def sayclassmethod(cls):

       print 'say %s' % cls

   def saymethod(self):

       print 'say %s' % self


test = info()
test.saymethod()##实例调用方法

test.sayclassmethod()##实例调用类方法

info.saymethod(test)##类调用实例方法

info.sayclassmethod()##类调用类方法