class Solution:
    # Function to perform DFS traversal
    def dfs(self, node, adj_list, visited):
        # Mark current node as visited
        visited[node] = True

        # Visit all unvisited neighbors
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                self.dfs(neighbor, adj_list, visited)

    # Function to count provinces
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        V = len(isConnected)
        # Create adjacency list from adjacency matrix
        adj_list = [[] for _ in range(V)]

        # Convert matrix to list
        for i in range(V):
            for j in range(V):
                if isConnected[i][j] == 1 and i != j:
                    adj_list[i].append(j)
                    adj_list[j].append(i)

        # Visited array
        visited = [False] * V

        # Count of provinces
        count = 0

        # Traverse all nodes
        for i in range(V):
            if not visited[i]:
                # Perform DFS and increment count
                count += 1
                self.dfs(i, adj_list, visited)

        return count