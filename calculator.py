class SafeFourCal(FourCal):
	def div(self):
	if self.second == 0:
		return 0
	else:
		return self.first / self.second

class	MoreFourCal(Fourcal):
	def pow(self):
		result = self.first ** self.second
		return result

class FourCal:
	def setdata(self, first, second):
		self.first = first
		self.second = second
	def sum(self):
		result = self.first + self.second
		return result
	def mul(self):
		result = self.first * self.second
		return result
	def sub(self):
		result = self.first - self.second
		return result
	def div(self):
		result = self.first / self.second
		return result





	


