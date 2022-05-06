# A.V.N
# 2022-05-06

def string_combine(a, b):
    if type(a) is not str or type(b) is not str:
        raise TypeError("Please type only strings!")
    return (a + " " + b)

def word_split(string):
    return string.split()

def main():
    in1 = input()
    in2 = input()
    string = input("Please enter a string: ")
    str_comb = string_combine(in1, in2)
    str_split = word_split(string)
    print(f"Your combined: {str_comb}, your split: {str_split}")
if __name__ == "__main__":
    main()