class intDict(object):
	def __init__(self, numBuckets):
		self.buckets = []
		self.numBuckets = numBuckets
		for i in range(numBuckets):
			self.buckets.append([])
	

	def addEntry(self, dictkey, dictVal):
		""" Assumes dictKey as an int. Adds an entry"""
		hashBucket = self.buxkets[dictkey%self.numBuckets]
		for i in range(len(hashBucket)):
			if hashBucket[i][0] == dictKey:
				hashBucket[i] = (dictKey, dictVal)
				return
		hashBucket.append((dictKey, divtVal))

	
	def getValue(self, dictKey):
		hashBucket = self.buckets[dictKey%self.numBuckets]
		for e in hashBucket:
			if e[0] == dictKey:
				return e[1]
		return None
	

	def __str__(self):
		res = '{'
		for b in self.buckets:
			for t in b:
				res = res+ str(t[0]) + ':' + str(t[1]) + ','
		return res[:-1] + "}"
