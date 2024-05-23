#1 Import libraries
import numpy as np
import matplotlib.pyplot as plt 

#2 Fix the Number of Workers
N = 1000

#3 Income Arrays Ccreation using Normal Distribution 
inc_occu_1 = np.random.normal(5000,1000,N)
inc_occu_2 = np.random.normal(7000,500,N)

# inspect the Income Arrays
print(inc_occu_1)
print(inc_occu_2)

#4 Scatterplot if Income Pairs
plt.scatter(inc_occu_1, inc_occu_2, c = 'orange')
plt.xlabel("Income Occupation 1")
plt.ylabel("Income Occupation 2")
plt.title("Scatterplot of Income Pairs")
plt.show()

#5 Generation of Random Integers 
#Schooling 
schooling = np.random.randint(1,17,N)
print(schooling)

#Experience 
experience = np.random.randint(1,40,N)
print(experience)

#6 Create an array occ_choice_1 of Booleans that indicates if workers choose occupation 1
occ_choice_1 = inc_occu_1 > inc_occu_2      #compares relevant elements in each array
print(occ_choice_1)

#7 Compute the share of worker in occupation 1
np.mean(1*occ_choice_1)
share_occu_1= np.sum(1*occ_choice_1)/N
print(share_occu_1)

#8 Use an If statement and a While Loop to compute the average years of schooling and average years of experience for workers in each occupation 
schooling_1 = np.zeros(N) 
exp_1       = np.zeros(N)
schooling_2 = np.zeros(N)
exp_2       = np.zeros(N)

i = 0 
while i < N:
    if inc_occu_1[i] > inc_occu_2[i]:
        schooling_1[i] = schooling[i]
        exp_1[i]       = experience[i]

    else:
        schooling_2[i] = schooling[i]
        exp_2[i]       = experience[i]

    i += 1 

print(schooling_1)
print(schooling_2)

# Compute Average Years of Schooling and Experience Conditional on Working in Each Occupation
mean_schooling_1 = np.mean(schooling_1[schooling_1 > 0])
mean_schooling_2 = np.mean(schooling_2[schooling_2 > 0])
mean_exp_1       = np.mean(exp_1[exp_1] > 0)
mean_exp_2       = np.mean(exp_2[exp_2] > 0)

print(mean_schooling_1)
print(mean_schooling_2)
print(mean_exp_1)
print(mean_exp_2)

# Alternative using a For Loop
schooling_1_alt = np.zeros(N)
exp_1_alt       = np.zeros(N)
schooling_2_alt = np.zeros(N)
exp_2_alt       = np.zeros(N)

for i in range(N):
    if inc_occu_1[i] > inc_occu_2[i]:
        schooling_1_alt[i] = schooling[i]
        exp_1_alt[i]       = experience[i]
    else:
        schooling_2_alt[i] = schooling[i]
        exp_2_alt[i]       = experience[i]
    
mean_schooling_1_alt = np.mean(schooling_1_alt[schooling_1_alt > 0])
mean_schooling_2_alt = np.mean(schooling_2_alt[schooling_2_alt > 0])
mean_exp_1_alt       = np.mean(exp_1_alt[exp_1_alt > 0])
mean_exp_2_alt       = np.mean(exp_2_alt[exp_2_alt > 0])

print(mean_schooling_1_alt)
print(mean_schooling_2_alt)
print(mean_exp_1_alt)
print(mean_exp_2_alt)