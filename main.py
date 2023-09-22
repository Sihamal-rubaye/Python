import os
import csv


csvpath = os.path.join("PyPoll/Resources/election_data.csv")

with open(csvpath, 'r') as csvfile:   #Reading the CSV file
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    Candidates_list = []
    Names=[]
    Values=[]
    Numbers=[]
    Candidates={}
    Candidates_Total=0


    for row in csvreader:
        Candidates_list.append(row[2]) #Making list for the candidate's row which will count as the total number of votes cast


        
    
    
    for i in range(len(Candidates_list)-1):
        if Candidates_list[i] not in Names: 
           Names.append(Candidates_list[i])  #A complete list of candidates who received votes

    for i in range(len(Names)):
        for j in range(len(Candidates_list)):
            if Names[i] == Candidates_list[j]:
                Candidates_Total += 1    
        Numbers.append (Candidates_Total)  #The total number of votes each candidate won

        Percentage = round((Candidates_Total/len(Candidates_list))*100,3)  #The percentage of votes each candidate won
        Values.append(Percentage)
        Candidates_Total=0

#Result analysis that prints to terminal  

spaces = "-------------------------"

print("\nElection Results\n")

print(spaces,"\n")

print("Total Votes:", len(Candidates_list)) #Total number of votes

print(spaces,"\n")

Candidates = dict(zip(Names,Values))
j=0

for key,value in Candidates.items():  #A complete list of candidates who received votes and thier total number of votes with the percentage of the votes they received 
    print (f'{key}: {value}%  ({Numbers[j]})\n')
    j+=1

print(spaces,"\n")

Maximum = max(Candidates.values())  #Maximum value of votes received

for key,value in Candidates.items():
    if value == Maximum:  #Maximum value received compared to the votes recieved by each candidate 
        print("Winner: ", key,"\n") #The name of the candidate who won the election

print(spaces,"\n")

#Exporting to text file 

f = open("PyPoll/Analysis/Results.txt", 'w') 

spaces = "-------------------------"

print("\nElection Results\n", file = f)

print(spaces,"\n", file = f)

print("Total Votes:", len(Candidates_list),"\n", file = f)

print(spaces,"\n", file = f)

Candidates = dict(zip(Names,Values))
j=0

for key,value in Candidates.items():
    print (f'{key}: {value}%  ({Numbers[j]})\n', file = f)
    j+=1

print(spaces,"\n", file = f)

Maximum = max(Candidates.values())

for key,value in Candidates.items():
    if value == Maximum:
        print("Winner: ", key,"\n", file = f)

print(spaces,"\n", file = f)


f.close()