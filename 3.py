import time

def func(vasakule, n):
    if vasakule == []: return n
    if vasakule[0]:
        return func(vasakule[1:], n)
    else:
        return func(vasakule[1:], n + 2**(len(vasakule)-1))

def main(filename):
    lines = open(filename).readlines()
    juhised = lines[0].split(" ")
    vasakule = []
    for j in juhised:
        if j == "v": vasakule.append(True)
        else: vasakule.append(False)
    return func(vasakule, 0) + 1
    

if __name__ == "__main__":
    start = time.time()

    print(main("input.txt"))

    end = time.time()
    print("Aeg: " + str(end-start))