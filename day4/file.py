
import csv
import os


# with open('day4/tested.csv','r') as csvfile:

#     csvreader =  csv.DictReader(csvfile)
    
#     for row in csvreader:
#         print(row['Sex'])



with open('day4/names_csv.csv', 'w',newline='') as csvfile:
    fieldnames = ['Name', "Age", 'LastName']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter='\t')
    writer.writeheader()


    writer.writerow({'Name':'Ali', 'Age':40, 'LastName':'karimi'})
    writer.writerow({'Name':'karima', 'Age':4, 'LastName':'rahimi'})
    writer.writerow({'Name':'marwa', 'Age':30, 'LastName':'Muradi'})
    writer.writerow({'Name':'Zahra', 'Age':15, 'LastName':'Ahmadi'})

    print("data added")



# with open('day4/names_csv.csv','r') as csvfile:

#     csvreader =  csv.DictReader(csvfile)
    
#     for row in csvreader:
#         for k,v in row.items():
#             print(f'{k} : {v} \n')   

       

# os.remove("day4/names_csv.csv")      
# print("file deleted")