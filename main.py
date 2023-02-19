# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_barckets_stack.append(Bracket(next,i))
            

        if next in ")]}":
            if not opening_brackets_stack :
                return i+1
            
            x = opening_brackets_stack.pop()
            if not are_matching:
                return i+1
            
    if opening_brackets_stack:
        x = opening_brackets_stack.pop()
        return x.position+1
    return "Success"

            


def main():
    a=input("F or I ->")
    if a in "F":
        filen=input("Insert name of file")
        with open(filen,"r", izmanit = "latin1") as file:
            text =file.read()
        j=find_mismatch(text)
        if j == "Success":
            print("Success")
        else:
            print(j)
    elif a in "I":
        text = input()
        j=find_mismatch(text)
        if j == "Success":
            print("Success")
        else:
            print(j)
    else:
        print("Input error")


if __name__ == "__main__":
    main()
