class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        ind=[0]*numCourses
        for course,dest in prerequisites:
            graph[dest].append(course)
            ind[course]+=1
        q=deque([])
        for i in range(numCourses):
            if ind[i]==0:
                q.append(i)
        finish=[]
        while q:
            node=q.popleft()
            finish.append(node)
            for nei in graph[node]:
                ind[nei]-=1
                if ind [nei]==0:
                    q.append(nei)
        if len(finish)==numCourses:
            return finish
        return []