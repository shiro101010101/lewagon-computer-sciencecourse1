import sys

def main():
    """Implement the calculator"""
    # YOUR CODE HERE
    if sys.argv[2]=="+":
        return int(sys.argv[1])+int(sys.argv[3])
    elif sys.argv[2]=="-":
        return int(sys.argv[1])-int(sys.argv[3])
    else:
        return int(sys.argv[1])*int(sys.argv[3])

if __name__ == "__main__":

    print(main())
