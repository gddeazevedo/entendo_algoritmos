from collections import deque, namedtuple


Person = namedtuple("Person", ["name", "job"])

graph = {}
graph["you"] = [
    Person("alice", "seller"),
    Person("bob", "cooker"),
    Person("claire", "car driver")
]
graph["bob"] = [Person("anuj", "writter"), Person("peggy", "seller")]
graph["alice"] = [Person("peggy", "seller")]
graph["claire"] = [Person("thom", "programmer"), Person("jonny", "cashier")]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def is_person_seller(person: Person) -> bool:
    '''Checks if a person's job is seller'''
    return person.job == 'seller'


def breadth_first_search(name: str) -> bool:
    '''Search for a mango seller in a graph'''
    queue = deque()
    queue.extend(graph[name])
    verified_names = []

    while queue:
        person = queue.popleft() # gets the first person in the queue

        if person.name not in verified_names:
            if is_person_seller(person): # check if the person is a seller
                print(f"{person.name} is a mango seller!")
                return True # yes, they're a seller

            # no, they ain't a seller, add all their friends to the queue
            queue.extend(graph[person.name])
            verified_names.append(person.name)

    return False
