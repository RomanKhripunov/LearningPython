from mymod import test


if __name__ == "__main__":
    import os

    try:
        print(test(os.path.join("OneMoreTime", "mymod.py")))
    except FileNotFoundError:
        print(test("mymod.py"))