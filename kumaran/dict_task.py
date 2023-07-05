people = [
    {
        "firstName": "ocean",
        "lastName": "Academy",
        "year": 2005,
        "address": "pondy"
    },
    {
        "firstName": "John",
        "lastName": "Doe",
        "year": 1990,
        "address": "New York"
    },
    {
        "firstName": "Jane",
        "lastName": "Smith",
        "year": 1985,
        "address": "London"
    },
    {
        "firstName": "Alice",
        "lastName": "Johnson",
        "year": 1995,
        "address": "Paris"
    },
    {
        "firstName": "Michael",
        "lastName": "Brown",
        "year": 1982,
        "address": "Los Angeles"
    },
    {
        "firstName": "Emily",
        "lastName": "Wilson",
        "year": 2000,
        "address": "Sydney"
    },
    {
        "firstName": "Daniel",
        "lastName": "Chen",
        "year": 1998,
        "address": "Tokyo"
    },
    {
        "firstName": "Sophia",
        "lastName": "Garcia",
        "year": 1993,
        "address": "Mexico City"
    },
    {
        "firstName": "Oliver",
        "lastName": "Wang",
        "year": 1987,
        "address": "Shanghai"
    },
    {
        "firstName": "Mia",
        "lastName": "Lee",
        "year": 2003,
        "address": "Seoul"
    },
    {
        "firstName": "Ethan",
        "lastName": "Nguyen",
        "year": 1996,
        "address": "Ho Chi Minh City"
    },
    {
        "firstName": "Isabella",
        "lastName": "Chung",
        "year": 1991,
        "address": "Hong Kong"
    }
]

# Total count of people in the list
total_people = len(people)
print("Total People:", total_people)

for i in range(total_people):
    people[i]["fullName"] = people[i]["firstName"] + \
        " " + people[i]["lastName"]
    print(people[i], "\n")
