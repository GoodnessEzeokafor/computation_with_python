import datetime

class Person(object):
	def __init__(self, name):
		''' Create a person with name name'''
		self.name = name
		try:
			lastBlank = name.rindex(' ')
			self.lastName = name[lastBlank+1:]
		except:
			self.lastName = name
		self.birthday = None
	
	def getLastName(self):
		""" return self's last name"""
		return self.lastName
	
	def setBirthday(self, birthdate):
		self.birthday = birthdate
	
	def getAge(self):
		if self.birthday == None:
			return ValueError
		return (datetime.date.today() - self.birthday).days
	
	def __lt__(self, other):
		if self.lastName == other.lastName:
			return self.name < other.name
		return self.lastName < other.lastName

	
	def __str__(self):
		return self.name


class MITPerson(Person):
	nextIdNUm = 0
	def __init__(self, name):
		Person.__init__(self, name)
		self.idNum = MITPeron.nextIdNum
		MITPerson.nextIdNum += 1
	def getIdNum(self):
		return self.idNum
	def __lt__(self, other):
		return self.idNUm < other.idNum

class Student(MITPerson):
	pass
class UG(Student):
	def __init__(self, name, classYear):
		MITPerson.__init__(self, name)
		self.year = classYear
	def getClass(self):
		return self.year
class Grad(Student):
	pass

class Grades(object):
	""" A mapping from students to a list f grades """
	def __init__(self):
		""" Create empty grade book"""
		self.students= []  # list of students
		self.grades = {}	# a dictionary that maps the student id to the gades
		self.isSorted = True # checks if its sorted
	def addStudent(self, student):
		if student in self.students:
			raise ValueError('Duplicate student')
		self.students.append(student)
		self.grades[student.getIdNum()] = []
		self.isSorted = False
	
	def addGrades(self, student):
		try:
			self.grades[student.getIdNum()]append(grade)
		except:
			raise ValueError('Student not in mapping')
	
	def getGrades(self, student):
		try:
			return self.grades[student.getIdNum()][:]
		except:
			raise ValueError('Student not in mapping')
	
	def allStudents(self):
		if not self.isSorted:
			self.students.sort()
		return self.students[:]


def gradeReport(course):
	report = ''	
	for s in course.allStudents():
		tot = 0.0
		numGrades = 0
		for g in course.getGrades(s):
			tot += g
			numGrades += 1
		try:
			average = tot/numGrades
			report = report + '\n' + str(s) +  mean grade is str(average)
		except ZeroDivisionError:
			report = report + '\n' + str(s) + ' has no grades'
		return report





if __name__ == '__main__':
	me = Person('Goodness Ezeokafor')
	him = Person('Barack Hussein Obama')
	her = Person('Madonna')
	
	pList = [me, him, her]
	for p in pList:
		print(p)
	pList.sort()
	for p in pList:
		print(p)


	
