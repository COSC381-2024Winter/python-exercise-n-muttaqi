from movies import Movies

def main():
    movies = Movies('./movies.txt')
    
    while True:
        print("\nMenu:")
        print("• Enter list for listing all the movie names.")
        print("• Enter search for searching movies.")
        print("• Enter q for exit.")
        
        choice = input("Enter your choice: ").lower()
        
        if choice == "list":
            list_movies(movies)
        elif choice == "search":
            search_movies(movies)
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please try again.")

def list_movies(movies):
    for movie in movies._movies:
        print(movie['name'])

def search_movies(movies):
    term = input("Please enter the search term: ").lower()
    searched_movies = []

    for movie in movies._movies:
        if term in movie['name'].lower():
            searched_movies.append(movie['name'])

    if searched_movies:
        for movie in searched_movies:
            print(movie)
    else:
        print(".")

if __name__ == "__main__":
    main()