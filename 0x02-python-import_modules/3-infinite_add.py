#!/usr/bin/python3
if __name__ == "__main__":
    """INFINITE ADDITION!."""
    import sys
count = len(sys.argv) - 1
sum = 0
def is_digit(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
for i in range(count):
    x = sys.argv[i + 1]
    if is_digit(x):
       sum = sum + int(sys.argv[i + 1])
    else:
       sum = 0
print("{}".format(sum))

