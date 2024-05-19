import heapq

def merge_k_lists(lists):
    h = []
    for list in lists:
        for value in list:
            heapq.heappush(h, value)
    
    return [heapq.heappop(h) for _ in range(len(h))]

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)