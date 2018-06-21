#Q.1- Create a class Animal as a base class and define method animal_attribute. Create another class Tiger which is inheriting Animal and access the base class method.
class animal:
	def animal_attribute(self):
		print("class animal")
class tiger(animal):
	def display(self):
		print("class tiger")
b=tiger()
b.animal_attribute()
b.display()

#2.
class A:
	def f(self):
		return self.g()
	def g(self):
		return ('A')
class B(A):
	def g(self):
		return ('B')
		
a=A()
b=B()
print(a.f(),b.f())
print(a.g(),b.g())

#output.
A B
A B

#3.
class cop:
		def add(self,name,age,work_exp,designation):
			self.name=name
			self.age=age
			self.work_exp=work_exp
			self.designation=designation
		def display(self):
			print("name:",self.name)
			print("age:",self.age)
			print("work experience:",self.work_exp)
			print("designation:",self.designation)
		def update(self,name,age,work_exp,designation):
			self.name=name
			self.age=age
			self.work_exp=work_exp
			self.designation=designation
class mission(cop):
		def add_mission_details(self,mission):
			self.mission=mission
			print(self.mission)
m1=mission()
m1.add_mission_details("assigned to petrollium")
m1.add("jyoti",19,"hcgjg","IAS")
m1.display()
m1.update("harman",20,"dsdv","dr")			
m1.display()		

#4.
class shape:
	def __init__(self,length,breadth):
		self.length=length
		self.breadth=breadth
class rectangle(shape):
	def area(self):
		area=self.length*self.breadth
		print(area)
class square(shape):
	def area(self):
		area=self.length*self.breadth
		print(area)
b=rectangle(4,5)
s=square(2,2)
b.area()
s.area()
		
		

		