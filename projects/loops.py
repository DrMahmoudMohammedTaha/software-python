# LOOPS

#FOR LOOP
people = ['John', 'Sara', 'Tim', 'Bob']
for person in people:
    print('Current Person: ', person)
    
# Iterate by seq index
for i in range(len(people)):
    print('Current Person: ',people[i])
    
for i in range(0, 10):
    print(i)
    
# WHILE lOOP

count = 0
while count <= 10:
    print('Count: ', count)
    if count == 5:
        break
    count = count + 1