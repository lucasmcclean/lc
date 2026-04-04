class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = dict()
        for fr, to in tickets:
            if fr not in graph:
                graph[fr] = []
            graph[fr].append(to)

        for fr in graph:
            graph[fr].sort(reverse=True)

        stack = ["JFK"]
        itinerary = []

        while stack:
            cur = stack[-1]
            if cur in graph and graph[cur]:
                nxt = graph[cur].pop()
                stack.append(nxt)
            else:
                itinerary.append(stack.pop())

        return itinerary[::-1]
