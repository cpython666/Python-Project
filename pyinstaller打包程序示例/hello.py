import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python hello_world.py [your_name]")
        return
    
    user_name = sys.argv[1]
    print(f"Hello, {user_name}!")

if __name__ == "__main__":
    main()