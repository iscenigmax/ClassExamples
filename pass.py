import itertools as it

if __name__ == "__main__":
    for l in range(1, 7):
        for a in it.product('abcdefghijklmnopqrstuvwxyz', repeat=l):
            if ''.join(a) == 'secret':
                print(f"Password found: {''.join(a)}")
                break
        else:
            continue
        break