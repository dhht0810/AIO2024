def find_max_number_in_k(list, k, n):
    # Write your code here
    ans = []
    for i in range(n-k):
        current_window = list[i:k+i]
        print(current_window)
        ans.append(max(current_window))
    return ans


# Example
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
res = find_max_number_in_k(num_list, k, len(num_list))
print(res)
