import heapq

def solution(n, s, a, b, fares):
    INF = 10**15
    
    graph = [[] for _ in range(n+1)]
    for u, v, w in fares:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    def dijkstra(start):
        dist = [INF] * (n+1)
        dist[start] = 0
        
        heap = []
        heapq.heappush(heap, (0, start))  
        while heap:
            cost, node = heapq.heappop(heap)
            
            if cost > dist[node]:
                continue
            
            for next_node, weight in graph[node]:
                new_cost = cost + weight
                
                if new_cost < dist[next_node]:
                    dist[next_node] = new_cost
                    heapq.heappush(heap, (new_cost, next_node))
        
        return dist
    
    
    distS = dijkstra(s)
    distA = dijkstra(a)
    distB = dijkstra(b)
    
    
    answer = INF
    for k in range(1, n+1):
        answer = min(answer, distS[k] + distA[k] + distB[k])
    
    return answer