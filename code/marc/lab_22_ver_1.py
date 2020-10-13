# Lab 22 counting imported text and calculating an ari value

def main():
    
    with open('lincoln.txt', 'r') as open_linc:
        contents = open_linc.read()
    words = list(contents(" "))

    print (words)


main()