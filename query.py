from movies import Movies

def main():
    movies = Movies('./movies.txt')
    
    while True:
        print("\nMenu:")
        print("• Enter list for listing all the movie names.")
        print("• Enter search for searching movies.")
        print("• Enter cast for searching cast.")
        print("• Enter q for exit.")
        
        choice = input("Enter your choice: ").lower()
        
        if choice == "list":
            list_movies(movies)
        elif choice == "search":
            search_movies(movies)
        elif choice == "cast":
            search_cast(movies)
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
        print("No result.")

def search_cast(movies):
    cast = input("Enter partial cast name to search: ").lower()
    searched_movies = []

    for movie in movies._movies:
        cast_list = [actor.lower() for actor in movie['cast']]
        if any(cast in actor for actor in cast_list):
            searched_movies.append((movie['name'], [actor for actor in movie['cast'] if cast in actor.lower()]))

    if searched_movies:
        for movie, cast in searched_movies:
            print(movie)
            print(cast)
    else:
        print("No result.")

if __name__ == "__main__":
    main()