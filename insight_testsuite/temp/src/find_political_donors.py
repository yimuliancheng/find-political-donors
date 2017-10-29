from heapq import *
import datetime


class zipInfo:

	def __init__(self, zip_C):
		self.heaps = [], []
		self.zip_C = zip_C
		self.totalAmt = 0
		self.size = 0

	def addNum(self, num):
		small, large = self.heaps
		heappush(small, - heappushpop(large, num))
		if len(large) < len(small):
			heappush(large, - heappop(small))

	def findMedian(self):
		small, large = self.heaps
		if len(large) > len(small):
			return large[0]
		return int(round((large[0] - small[0]) / 2.0))

	def addTotal(self, amount):
		self.totalAmt += amount
		return self.totalAmt

	def addSize(self):
		self.size +=1
		return self.size


class dateInfo:

	def __init__(self, cmteId, date):
		self.heaps = [], []
		self.date = date
		self.cmteId = cmteId
		self.totalAmt = 0
		self.size = 0

	def __cmp__(self, other):
		if(cmp(self.cmteId, other.cmteId)==1 or cmp(self.cmteId, other.cmteId)==-1):
			return cmp(self.cmteId, other.cmteId)
		elif(cmp(self.cmteId, other.cmteId) == 0):
			return cmp(self.date, other.date)

	def addNum(self, num):
		small, large = self.heaps
		heappush(small, - heappushpop(large, num))
		if len(large) < len(small):
			heappush(large, - heappop(small))

	def findMedian(self):
		small, large = self.heaps
		if len(large) > len(small):
			return large[0]
		return int(round((large[0] - small[0]) / 2.0))

	def addTotal(self, amount):
		self.totalAmt += amount
		return self.totalAmt

	def addSize(self):
		self.size +=1
		return self.size


zip_zipInfo = {}
date_dateInfo = {}
rightZipFormat = True
rightDateFormat = True


with open("input/itcont.txt") as f:
	with open('output/medianvals_by_zip.txt','w') as wf:
		
		for line in f:
			line_info = line.split('|')
			cmteId = line_info[0]
			zipCode = line_info[10]			
			date = line_info[13]
			amount = int(line_info[14])
			otherId = line_info[15]

			### Precheck otherId -> empty, cmteId -> not empty, amount -> not empty
			if(otherId != "" or cmteId == "" or amount == ""):
				continue

			### Precheck the format of zipCode, empty, length, alldigit
			if(len(zipCode) < 5 or zipCode == "" or zipCode.isdigit() == False):
				rightZipFormat = False

			### Precheck the format of date, empty, length, alldigit, date validation
			if(date == "" or len(date) != 8 or date.isdigit() ==  False):
				rightDateFormat = False

			month = int(date[0:2])
			day = int(date[2:4])
			year = int(date[4:8])

			try:
				newDate = datetime.datetime(year, month, day)
			except ValueError:
				rightDateFormat = False

			### Output to zip.txt if zipCode format is correct
			if (rightZipFormat ==  True):
				zipCode = zipCode[0:5]
				newZipInfo = 0
				if(zipCode not in zip_zipInfo):
					### new zipCode, initiate the class
					newZipInfo = zipInfo(zipCode)
				else:
					### get the old information
					newZipInfo = zip_zipInfo[zipCode]

				newZipInfo.addNum(amount)
				total = newZipInfo.addTotal(amount)
				size = newZipInfo.addSize()
				median = newZipInfo.findMedian()
				zip_zipInfo[zipCode] = newZipInfo
				wf.write(cmteId + "|" + zipCode + "|" + str(median) + "|" + str(size) + "|" + str(total) + "\n")


			### Output to date.txt if date format is correct
			if(rightDateFormat == True):
				newDateInfo = 0
				if(date not in date_dateInfo):
					newDateInfo = dateInfo(cmteId, newDate)
				else:
					newDateInfo = date_dateInfo[date]

				newDateInfo.addNum(amount)
				median = newDateInfo.findMedian()
				total = newDateInfo.addTotal(amount)
				size = newDateInfo.addSize()
				date_dateInfo[date] = newDateInfo
		
	with open('output/medianvals_by_date.txt','w') as df:
		sort_list = sorted(date_dateInfo.values())
		for d in sort_list:
			median = d.findMedian()
			df.write(d.cmteId + "|" + d.date.strftime('%m%d%Y') + "|" + str(median) + "|" + str(d.size) + "|" + str(d.totalAmt) + "\n")
	