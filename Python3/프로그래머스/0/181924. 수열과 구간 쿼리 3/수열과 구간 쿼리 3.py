def solution(arr, queries):
    answer = []
    for i in range(len(queries)):
        print(i)
        dif = arr[queries[i][0]]
        arr[queries[i][0]] = arr[queries[i][1]]
        arr[queries[i][1]] = dif
    return arr