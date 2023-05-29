class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for i in range(len(people)):
        if "wife" in people[i] and people[i]["wife"] is not None:
            person_list[i].wife = Person.people[people[i]["wife"]]
        if "husband" in people[i] and people[i]["husband"] is not None:
            person_list[i].husband = Person.people[people[i]["husband"]]
    return person_list
