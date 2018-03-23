from collections import deque

graph = {
    "YOU": ["BOB", "CLAIRE", "ALICE"],
    "BOB": ["ANUJ", "PEGGY"],
    "ALICE": ["PEGGY"],
    "CLAIRE": ["THOM", "JONNY"],
    "PEGGY": [],
    "ANUJ": [],
    "THOM": [],
    "JONNY": [],
}

start, end = "YOU", "JONNY"


def breadth_search(dict_data, start, end):
    search_deque = deque()
    search_deque += dict_data.get(start)
    searched = []
    while search_deque:
        person = search_deque.popleft()
        if person not in searched:
            if person_is_seller(person, end):
                print("That's is searched item")
                return True
            else:
                search_deque += dict_data.get(person)
            searched.append(person)
    return False


def person_is_seller(name, end_name):
    return name[:-1] == end_name[:-1]


print(breadth_search(graph, start, end))
