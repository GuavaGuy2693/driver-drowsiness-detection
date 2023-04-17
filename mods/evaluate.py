def infer(arr, factor):
    return True if (arr.count(0)/len(arr) < factor) else False

def update(arr, factor, value):
    if infer(arr, factor):
        arr += value
        n = int(factor*len(arr)/2)
        return arr[n:] + [0]*n