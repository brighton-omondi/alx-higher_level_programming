import sys

def main():
    argv = sys.argv[1:]  # Exclude the script name from the arguments
    num_args = len(argv)

    if num_args == 0:
        print("argument(s):.")
        print(":")  # No arguments were passed, print a dot
    else:
        plural = "s" if num_args > 1 else ""
        print(f"{num_args} argument(s):")
        print(f"Argument{plural}:")
        for i, arg in enumerate(argv, start=1):
            print(f"{i}: {arg}")

if __name__ == "__main__":
    main()
