import json

from logic import load_movies, save_movies, add_movie, mark_watched, find_by_year

DATA_FILE = "movies.json"


def main():
    movies = load_movies(DATA_FILE)

    while True:
        print("\nКаталог фильмов")
        print("1. Показать все фильмы")
        print("2. Добавить фильм")
        print("3. Отметить фильм как просмотренный")
        print("4. Найти фильмы по году")
        print("0. Выход")

        choice = input("Выберите пункт: ")

        if choice == "1":
            if movies:
                for movie in movies:
                    status = "✓" if movie['watched'] else " "
                    print(f"{movie['id']}. {movie['title']} ({movie['year']}) {status}")
            else:
                print("Список фильмов пуст.")

        elif choice == "2":
            print("Добавление фильма")
            title = input("Название: ").strip()
            if not title:
                print("Ошибка: название не может быть пустым.")
                continue

            try:
                year = int(input("Год: ").strip())
                if year < 1800 or year > 2100:
                    print("Ошибка: год должен быть в диапазоне 1800-2100.")
                    continue
            except ValueError:
                print("Ошибка: год должен быть числом.")
                continue

            movies = add_movie(movies, title, year)
            print(f"Фильм '{title}' добавлен!")

        elif choice == "3":
            try:
                movie_id = int(input("ID фильма: ").strip())
                updated_movies = mark_watched(movies, movie_id)
                if updated_movies != movies:
                    movies = updated_movies
                    print("Фильм отмечен как просмотренный!")
                else:
                    print("Фильм с таким ID не найден.")
            except ValueError:
                print("Ошибка: ID должен быть числом.")

        elif choice == "4":
            try:
                year = int(input("Год: ").strip())
                found = find_by_year(movies, year)
                if found:
                    print(f"Фильмы за {year}:")
                    for movie in found:
                        status = "✓" if movie['watched'] else " "
                        print(f"  {movie['id']}. {movie['title']} {status}")
                else:
                    print(f"Фильмы за {year} не найдены.")
            except ValueError:
                print("Ошибка: год должен быть числом!!!!!!!!")

        elif choice == "0":
            save_movies(DATA_FILE, movies)
            print("LДо скорой встречи!")
            break

        else:
            print("Неверный пункт меню.")


if __name__ == "__main__":
    main()
