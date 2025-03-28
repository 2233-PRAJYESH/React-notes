employees = [
    {"firstName": "sai", "lastName": "kiran", "age": 27},
    {"firstName": "rahul", "lastName": "sharma", "age": 30},
    {"firstName": "priya", "lastName": "singh", "age": 25},
    {"firstName": "anil", "lastName": "kumar", "age": 40},
    {"firstName": "deepa", "lastName": "verma", "age": 22},
    {"firstName": "ravi", "lastName": "yadav", "age": 28},
    {"firstName": "pallavi", "lastName": "gupta", "age": 33},
    {"firstName": "amit", "lastName": "joshi", "age": 29},
    {"firstName": "neha", "lastName": "shah", "age": 31},
    {"firstName": "vikas", "lastName": "mehta", "age": 26},
    {"firstName": "arun", "lastName": "patel", "age": 35},
    {"firstName": "sunita", "lastName": "rathod", "age": 23},
    {"firstName": "mohan", "lastName": "nair", "age": 32},
    {"firstName": "lakshmi", "lastName": "rao", "age": 24},
    {"firstName": "suresh", "lastName": "reddy", "age": 27},
    {"firstName": "geeta", "lastName": "iyer", "age": 28},
    {"firstName": "vijay", "lastName": "shukla", "age": 26},
    {"firstName": "meena", "lastName": "pandey", "age": 34},
    {"firstName": "arjun", "lastName": "desai", "age": 37},
    {"firstName": "swati", "lastName": "kothari", "age": 29},
    {"firstName": "naveen", "lastName": "chopra", "age": 22}
]

print(employees[0]['firstName'] + employees[0]['lastName'])

m = map(lambda x: x['firstName'] + x['lastName'], employees)
print(list(m))

f = filter(lambda x: x['age'] < 30, employees)
print(list(f))

# [{'firstName': 'sai', 'lastName': 'kiran', 'age': 27},
#  {'firstName': 'priya', 'lastName': 'singh', 'age': 25},
#  {'firstName': 'deepa', 'lastName': 'verma', 'age': 22},
#  {'firstName': 'ravi', 'lastName': 'yadav', 'age': 28},
#  {'firstName': 'amit', 'lastName': 'joshi', 'age': 29},
#  {'firstName': 'vikas', 'lastName': 'mehta', 'age': 26},
#  {'firstName': 'sunita', 'lastName': 'rathod', 'age': 23},
#  {'firstName': 'lakshmi', 'lastName': 'rao', 'age': 24},
#  {'firstName': 'suresh', 'lastName': 'reddy', 'age': 27},
#  {'firstName': 'geeta', 'lastName': 'iyer', 'age': 28},
#  {'firstName': 'vijay', 'lastName': 'shukla', 'age': 26},
#  {'firstName': 'swati', 'lastName': 'kothari', 'age': 29},
#  {'firstName': 'naveen', 'lastName': 'chopra', 'age': 22}]
