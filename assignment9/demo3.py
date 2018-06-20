#Q.1-
class circle:
	radius=7
	def getArea(self):
		c=3.14*self.radius*self.radius
		print("c=",c)
	def getCircumference(self):
		c=2*3.14*self.radius
		print("c=",c)
c2=circle()
c2.getArea()
c2.getCircumference()

#Q.2-
class student:
	def __init__(self,name,roll,subject):
		self.name=name
		self.roll=roll
		self.subject=subject
		
	def display(self):
		print(self.name,self.roll,self.subject)
		
s1=student("jyoti","a","english")
s1.display()	

#3.
class temprature:
	def __init__(self,fahrn,celc):
		 self.fahrn=fahrn
		 self.celc=celc
	def fah(self):
		fahrn=(1.8)*self.celc+32
		print("convert fahrenheit into celsius",fahrn)
	def cel(self):
		celc=(self.fahrn-32)*5/9
		print("convert celsius into fahrenheit",celc)
n=int(input("enter any fahrenheit temprature"))
m=int(input("enter any celsius temprature"))		
t1=temprature(n,m)
t1.fah()
t1.cel()

#4.
class moviedetail:
	def __init__(self,moviename,artistname,release,rating):
		self.moviename=moviename
		self.artistname=artistname
		self.release=release
		self.rating=rating
	def display(self):
		print("moviename",self.moviename)
		print("artistname",self.artistname)
		print("release",self.release)
		print("rating",self.rating)
	def update(self):
		self.moviename=input("enter moviename")
		self.artistname=input("enter any artistname")
		self.release=input("enter any release")
		self.rating=input("enter any rating")
		print("moviename",self.moviename)
		print("artistname",self.artistname)
		print("release",self.release)
		print("rating",self.rating)
m1=moviedetail('3idiots','amirkhan','2016','543')
m1.display()
m1.update()

#5.
class expenditure:
	def __init__(self,expenditure,saving):
		self.expenditure=expenditure
		self.saving=saving
	def display(self):
		print("expenditure",self.expenditure)
		print("saving",self.saving)
		
	def salary(self):
		self.salary=self.expenditure+self.saving
		print("salary is",self.salary)
e=expenditure(1000,500)
e.display()
e.salary()
		
		
	