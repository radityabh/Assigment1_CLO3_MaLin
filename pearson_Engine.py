from read_data import read_data
import numpy as np

data = read_data()
rating = data.get_rating()
item = data.get_item()

def pearsonCoefficient(movie1,movie2):
	user_movie1 = [] #list user who rated movie one
	user_movie2 = [] #list user who rated movie two
	user_both = [] #list user who rated both of movie
	rate_movie1 = [] #list rate movie one from user who rated both of movie
	rate_movie2 = [] #list rate movie two from user who rated both of movie
	n = 0 #len of data
	sum1 = 0
	sum2 = 0
	sum3 = 0
	r = 0 #pearson coefficient

	for i in rating:
		if i[1] == movie1:
			user_movie1.append([i[0],i[1],i[2]])
		if i[1] == movie2:
			user_movie2.append([i[0],i[1],i[2]])

	for i in range(len(user_movie1)):
		for x in range(len(user_movie2)):
			#user who rated both of movie
			if user_movie1[i][0] == user_movie2[x][0]:
				rate_movie1.append(user_movie1[i][2])
				rate_movie2.append(user_movie2[x][2])
				n +=1
	rate_movie1 = np.array(rate_movie1)
	rate_movie2 = np.array(rate_movie2)


	for i in range(n):
			sum1 = sum1 + ((rate_movie1[i]-np.mean(rate_movie1))*(rate_movie2[i]-np.mean(rate_movie2)))
			sum2 = sum2 + (rate_movie1[i]-np.mean(rate_movie1))**2
			sum3 = sum3 + (rate_movie2[i]-np.mean(rate_movie2))**2
	if sum1 == 0 or sum2 == 0 or sum3 == 0:
		r = 0
	else:
		r = sum1/(np.sqrt(sum2)*np.sqrt(sum3))
	return r

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
			coefficient.append([int(i[0]),pearsonCoefficient(movie,int(i[0]))])
	coefficient = sorted(coefficient,key=lambda x: x[1],reverse=True)
	for x in coefficient:
		tes.append(x[0])
	for i in range(5):
		s = s +str(tes[i])+". "+searchNameMovie(tes[i])+", "
	return s

