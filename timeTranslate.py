from time import *
from datetime import datetime, timedelta


class TimeTranslate:
	"""时间转换"""
	
	DATEFMT = '%Y-%m-%d'
	DATETIMEFMT = '%Y-%m-%d %H:%M:%S'
	MONTHFMT = '%Y-%m'
	
	def __init__(self, t):
		self.t = t
		self.year = 0
		self.month = 0
		self.day = 0
		self.hour = 0
		self.minute = 0
		self.second = 0
		self.timestamp = 0
		self._handle_time()
		
	def strtime(self, fmt='%Y-%m-%d %H:%M:%S'):
		return self.d.strftime(fmt)
		
	def _handle_time(self):
		if isinstance(self.t, float) or isinstance(self.t, int):
			self.d = datetime.fromtimestamp(self.t)	
		if isinstance(self.t, str):
			self._deal_strtime()
		if isinstance(self.t, datetime):
			self.d = self.t
		if self.d:
			self.year = self.d.year
			self.month = self.d.month
			self.day = self.d.day
			self.hour = self.d.hour
			self.minute = self.d.minute
			self.second = self.d.second
			self.timestamp = mktime(self.d.timetuple())
			
	def _deal_strtime(self):
		date = ''
		date_list = []
		time_list = []
		if ' ' in self.t:
			date = self.t.split()[0]
			_time = self.t.split()[1]
			if '-' in date:
				date_list = date.split('-')
				date_list = [int(i) for i in date_list]
			if '/' in date:
				date_list = date.split('/')
				date_list = [int(i) for i in date_list]
			if ':' in _time:
				time_list = _time.split(':')
				time_list = [int(i) for i in time_list]
			if date_list and time_list:
				all_list = date_list + time_list
		else:
			if '-' in self.t:
				date_list = self.t.split('-')
				date_list = [int(i) for i in date_list]
			if '/' in self.t:
				date_list = self.t.split('/')
				date_list = [int(i) for i in date_list]
		all_list = date_list + time_list
		self.d = datetime(*all_list)
		
		
# tt = TimeTranslate('2018-8-12 23:34')
tt = TimeTranslate(1534088040.0)
