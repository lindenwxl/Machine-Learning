from __future__ import print_function, division
from collections import deque

def search(name):
    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["jonny", "thom"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["jonny"] = []
    graph["thom"] = []
    
    search_queue = deque()
    search_queue += graph[name]
    searched = []                             # 这个数组用于记录检查过的人 
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if is_seller(name):
                print(person + "is a mongo seller! ")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)    
    return False
    

def is_seller(name):
    return name[-1] == "m"
    

def main():
    search("you")


if __name__ == "__main__":
    main()