# Make an empty list to store people in.
people = []

# Define some people, and add them to the list.
person = {
    'first_name': 'Zain',
    'last_name': 'Zahid',
    'age': 23,
    'city': 'Karachi',
}
people.append(person)

person = {
    'first_name': 'Aney',
    'last_name': 'Zahid',
    'age': 24,
    'city': 'Karachi',
}
people.append(person)

person = {
    'first_name': 'Sherry',
    'last_name': 'Zahid',
    'age': 27,
    'city': 'Karachi',
}
people.append(person)

# Display all of the information in the dictionary.
for person in people:
    name = person['first_name'].title() + " " + person['last_name'].title()
    age = str(person['age'])
    city = person['city'].title()

    print(name + ", From " + city + ", is " + age + " years old.")