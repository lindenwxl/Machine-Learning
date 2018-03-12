# -*- coding:utf-8 -*-
#__author__ = "lindenwxl"
#__date__ = "2018-03-12"

from __future__ import print_function, division

def find_lowest_cost_node(costs, processed):
    lowest_cost = float("inf") # 设置初始开销为无穷大，因为你现在很茫然
    lowest_cost_node = None # 设置初始最低开销节点为 None
    for node in costs: # 遍历所有的节点
        cost = costs[node]
        if cost < lowest_cost and node not in processed: # 如果当前节点的开销更低且未处理过，
            lowest_cost = cost # 就将其视为开销最低的节点。
            lowest_cost_node = node # 最低开销节点为当前的节点。
    return lowest_cost_node

def best_route():
    # 存储所有节点及其下一个节点开销的字典
    graph = {"start": {"a": 6, "b": 2}, 
             "a": {"fin": 1}, 
             "b": {"a": 3, "fin": 5}, 
             "fin": {}}
     # 从起点开始，包含所有下一个节点开销的字典
    infinity = float("inf")
    costs = {"a": 6, "b": 2, "fin": infinity}
    
    # 从起点开始，存储所有父节点的散列表
    parents = {"a": "start", "b": "start", "fin": None}
    best_route = ""
    processed = []
    
    node = find_lowest_cost_node(costs, processed) # 在未处理的节点中找出开销最小的节点
    while node is not None:
        # 这个 while 循环在所有节点都被处理过后结束
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys(): # 遍历当前节点的所有邻居
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost: # 如果经当前节点前往该邻居最近，
                costs[n] = new_cost # 就更新该邻居的开销
                parents[n] = node  # 同时将该邻居的父节点设置为当前节点
        processed.append(node) # 将当前借调标记为已处理
        node = find_lowest_cost_node(costs, processed) # 找出接下来要处理的节点，并循环。
        
    p = parents["fin"]
               
    while True:  
        best_route += "%s<——" % p
        p = parents[p]
        
        if p is "start":
            break               
                
    return "到达终点的最终路径是: 终点<——%s起点。\n最快到达的时间是%s分钟" % (best_route, costs["fin"])      
        
if __name__ == "__main__":
    best_route = best_route()
    print(best_route)
