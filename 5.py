import time

def main(filename):
    lines = open(filename).readlines()
    


    return 1
    

if __name__ == "__main__":
    start = time.time()

    print(main("test.txt"))

    end = time.time()
    print("Aeg: " + str(end-start))