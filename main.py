import Jaccard_engine as je
import pearson_Engine as pe

#the answer from number 13a
print("13a. Jaccard_coefficient")
print ("Number i : ",je.jacardCoefficient(1,2))
print ("Number ii : ",je.jacardCoefficient(je.searchIdMovie("Three Colors: Red"),je.searchIdMovie("Three Colors: Blue")))
taxi = je.searchIdMovie("Taxi Driver")
print("Number iii : ",je.fiveHighest(taxi))
apollo = je.searchIdMovie("Apollo 13")
print("Number iV (Apollo 13) : ",je.fiveHighest(apollo))

#the answer from number 13b
print("\n\n13b. Pearson_correlation_coefficient")
print("Number ii : ",pe.pearsonCoefficient(1,2))
print("Number iii : ",pe.pearsonCoefficient(pe.searchIdMovie("Three Colors: Red"),pe.searchIdMovie("Three Colors: Blue")))
taxi = pe.searchIdMovie("Taxi Driver")
print("Number iv : ",pe.fiveHighest(taxi))
apollo = pe.searchIdMovie("Apollo 13")
print("Number v (Apollo 13) : ",pe.fiveHighest(apollo))