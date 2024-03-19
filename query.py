from movies import Movies

def main():
    movies = Movies('./movies.txt')

    while True:
        print("\nMenu:")
        print("• Enter list for listing all the movie names.")
        print("• Enter q for exit.")

        choice = input("Please enter the search term: ").lower()

        if choice == "list":
            list_movies(movies)
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please try again.")

def list_movies(movies):
    for movie in movies._movies:
        print(movie['name'])

if __name__ == "__main__":
    main()