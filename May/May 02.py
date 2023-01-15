class Solution:
	def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:

		length = len(vals)

		graph = defaultdict(list)

		for source, destination in edges:
			heappush(graph[source], (vals[destination], destination))
			heappush(graph[destination], (vals[source], source))

		loc = list(range(length))

		def find(x):
			if loc[x] != x:
				loc[x] = find(loc[x])
			return loc[x]

		def union(x, y):
			source, destination = find(x), find(y)
			if source != destination:
				loc[destination] = source

		value_to_index = defaultdict(list)
		for index, value in enumerate(vals):
			value_to_index[value].append(index)

		result = length

		for key in sorted(value_to_index):
			for node in value_to_index[key]:
				while graph[node] and graph[node][0][0] <= key:
					neighbour_value, neighbour_index = heappop(graph[node])
					union(node, neighbour_index)

			group = Counter([find(x) for x in value_to_index[key]])

			result = result + sum(math.comb(x, 2) for x in group.values())            

		return result
		
