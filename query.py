from movies import Movies

def main():
    movies = Movies('./movies.txt')

    while True:
        print("\nMenu:")
        print("• Enter q for exit")

        choice = input("Please enter the search term: ").lower()

        if choice == 'q':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()