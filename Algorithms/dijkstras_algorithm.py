# graph["YOU"] = ["ALICE", "BOB", "CLAIRE"]
    # "BOB": ["ANUJ", "PEGGY"],
    # "ALICE": ["PEGGY"],
    # "CLAIRE": ["THOM", "JONNY"],
# }

graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

infinity = float("inf")
costs = {
    "a": 6,
    "b": 2,
    "fin": infinity
}

parents = {
    "a": "start",
    "b": "start",
    "fin": None
}

processed = []



