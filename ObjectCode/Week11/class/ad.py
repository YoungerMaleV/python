import abc
class Computer:
	def __init__(self,name):
		self._name=name

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self,value):
		self._name=value

	def __str__(self):
		return 'the {} computer'.format(self._name)

	def execute(self):
		print('execute a computer program')

class Human:
	def __init__(self,name):
		self._name=name
	def __str__(self):
		return '{} is an human'.format(self._name)
	def speak(self):
		print('an human speaks')

class Synthesizer:
	def __init__(self,name):
		self._name=name
	def __str__(self):
		return 'the {} synthesizer'.format(self._name)
	def play(self):
		print('play a synthesizer')

class Adapter:
	def __init__(self,adp_obj,adp_methods):
		self.obj=adp_obj
		self.__dict__.update(adp_methods)

	def __str__(self):
		return str(self.obj)

class Target(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def execute(self):
		pass

class HumanAdapter(Target):
	def __init__(self,human):
		self.human=human

	def execute(self):
		self.human.speak()

class SynthesizerAdapter(Target):
	def __init__(self,syn):
		self.syn=syn
	def execute(self):
		self.syn.play()

def main():
	objects=[Computer('mac')]
	syn=Synthesizer('yamaha')
	objects.append(Adapter(syn,dict(execute=syn.play)))
	h=Human('zjc')
	objects.append(Adapter(h,dict(execute=h.speak)))
	for obj in objects:
		obj.execute()


	objects2=[Computer('mac')]
	objects2.append(HumanAdapter(h))
	objects2.append(SynthesizerAdapter(syn))
	for obj in objects2:
		obj.execute()

if __name__=='__main__':main()
