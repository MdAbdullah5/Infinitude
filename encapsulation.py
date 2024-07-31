class _Person:
    def __init__(self,_name,_age):
        self._name=_name
        self._age=_age
    def _p(self):
        print(self._name,self._age)

a=_Person("Hi",1)
a._p()