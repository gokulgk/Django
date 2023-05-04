import csv
import os

i=0
k=0
# Open the CSV file in read mode
with open('log.csv', mode='r') as file:

    # Create a CSV reader object
    reader = csv.reader(file)

    # Read all rows into a list
    rows = list(reader)
    
    for row in rows:
        if(row[5]!="Completed" ):
            if(row[8]=="High"):
                row[8]="High(Prority Assigned)"
                new_row=row
                index2=k
                rows.pop(k)
                print(k)
                break
        k=k+1
        
    for row in rows:
        if(row[5]!="Completed" and row[5]!="Status" and row[8]!="High(Prority Assigned)"):
            index=i
            print(i)
            rows.insert(index, new_row)
            break
        i=i+1
            

# Open the CSV file in write mode
with open('log.csv', mode='w', newline='') as file:

    # Create a CSV writer object
    writer = csv.writer(file)

    # Write all rows to the CSV file
    writer.writerows(rows)


with open("status.txt", "w") as f: 
   f.write("priority") 

