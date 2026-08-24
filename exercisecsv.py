#1



shopping_list = ["milk", "bread", "apple"]

with open("shopping.txt", "w", encoding="utf-8") as file:
    for product in shopping_list:
        file.write(product + "\n")

with open("shopping.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())           


#3

total = 0  



with open("names.txt","r",encoding="utf-8")as file:
        for line in file:
            total+=1 
print(total)            




#4 


with open("input.txt","r",encoding="utf-8")as source:
     with open("output.txt","w",encoding="utf-8")as target:
          for line in source :
               target.write(line)
                  
#5 
longest = ""
with open("words.txt", "r",encoding="utf-8")as f:
    for line in f :
        word= line.strip()
        if len(word)>len(longest):
            longest = word 
print(longest)            



#6 
def add_visit(name):
     with open("visits.txt", "a", encoding="utf-8")as file :
          file.write(name+"\n")


def count_visits():
     total = 0 
     with open ("visits.txt","r", encoding="utf-8") as file:
        for line in file :
             total+=1
     return total      



#7 
import csv 
with open ("students.csv", "r", encoding="utf-8")as doc:
     reader = csv.DictReader(doc)
     total = 0 
     count = 0 
     for row in reader :
          name = row["name"]
          grade = int(row["grade"])
          total += grade 
          count += 1 
     average = total / count 
print (average)

    



#9 
import csv 
with open("students.csv","r",encoding="utf-8")as file:
   with open ("passing_students.csv", "w",encoding="utf-8", newline="") as file2:
        reader = csv.DictReader(file)
        writer = csv.DictWriter(file2, fieldnames=["name", "grade"])
        writer.writeheader()
        for row in reader :
             grade = int(row["grade"])
             if grade >= 60 :
                  writer.writerow(row)



#10 projet

