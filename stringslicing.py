#string slicing

name = "bhavani"
print(name[0:1])
print(name[ : ])
print(name[ :3])


#reverse a string

name = "bhavani"
print(name[:: -1])

#reverse a string without slicing

name = "bhavani"
name="".join(reversed(name))
print(name)

#reverse a list items

attendees:list=["bhavani","chinni","sravya"]
print(attendees[0:1])
print(attendees[0: ])
print(attendees[:])
print(attendees[0:3])
print(attendees[0:2])
print(attendees[-1:2])