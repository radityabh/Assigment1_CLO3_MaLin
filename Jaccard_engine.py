from read_data import read_data

data = read_data()
rating = data.get_rating()
item = data.get_item()

#Number i
def jacardCoefficient(movie1,movie2):
	m11 = 0 #user who rated both of movie
	m10 = 0 #user who rated movie 1
	m01 = 0 #user who rated movie 2
	user_movie1 = [] #list user who rated movie one
	user_movie2 = [] #list user who rated movie two
	user_both = [] #list user who rated both of movie

	# insert list user rated movie1 and movie 2
	for i in rating:
		if i[1] == movie1:
			user_movie1.append(i[0])
		if i[1] == movie2:
			user_movie2.append(i[0])

	for i in range(len(user_movie1)):
		both_rate = False;
		for x in range(len(user_movie2)):
			#user who rated both of movie
			if user_movie1[i] == user_movie2[x]:
				both_rate = True
				user_both.append(user_movie1[i])
				break
		if both_rate:
			m11 +=1
		else:
			#user who rated movie 1
			m10 += 1
	
	#user who rated movie 2
	for i in range(len(user_movie2)):
		if user_movie2[i] not in user_both:
			m01 +=1

	return (m11/(m01+m10+m11))

def searchIdMovie(movie):
	for i in item:
		s = i[1].split(" (")
		if s[0] == movie:
			return int(i[0])

def searchNameMovie(id):
	for i in item:
		if int(i[0]) == id:
			s = i[1].split(" (")
			return str(s[0])

def fiveHighest(movie):
	coefficient = [] #list all coeficient
	tes = []
	s = ""
	for i in item:
		if int(i[0]) != movie:
			coefficient.append([int(i[0]),jacardCoefficient(int(movie),int(i[0]))])
	coefficient = sorted(coefficient,key=lambda x: x[1],reverse=True)
	for x in coefficient:
		tes.append(x[0])
	for i in range(5):
		s = s +str(tes[i])+". "+searchNameMovie(tes[i])+", "
	return s




		

