import numpy as np

def itp_arr():
    arr = np.array(([0,0,0],[0,0,0],[0,0,0]))
    for s in range(0,3):
        for m in range(0,3):
            if s == m:
                arr[s][m] = 1
            else:
                arr[s][m] = 0
    print(arr)
    print("\n")

    for s in range(0,3):
        for m in range(0,3):
            if s == m:
                arr[s][m] = 1
            else:
                arr[s][m] = 3
    print(arr)
    print("\n")

    arr = np.delete(arr, 2, 1)
    print(arr)

if __name__ == "__main__":
    itp_arr()

