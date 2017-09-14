class read_data:
	def __init__ (self):
		self.file_rating_path = "data/u.data"
		self.file_item_path = "data/u.item"
		self.rating_data = []
		self.item_data = []
		self.read_rating()
		self.read_item()

	#read rating data to list
	def read_rating(self):
		file_rating = open(self.file_rating_path,"r")
		for i in file_rating:
			self.rating_data.append(tuple(int(x)for x in i.split("\t")))
		file_rating.close()

	#get list data rating
	def get_rating(self):
		return self.rating_data

	#read item data to list
	def read_item(self):
		file_item = open(self.file_item_path,"r")
		for i in file_item:
			self.item_data.append(tuple(str(x)for x in i.split("|")))
		file_item.close()

	#get list data item
	def get_item(self):
		return self.item_data