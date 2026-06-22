import pandas as pd
import matplotlib.pyplot as pl
import time

def intro():
    print("=" * 80)
    print("🎬 【﻿CineSort】 - your personal movie data manager!".center(80))
    print("Note: This data is fictional or for educational purposes.".center(80))
    print("=" * 80)
    time.sleep(1)

def load_data():
    try:
        df = pd.read_csv("/Users/santha/Desktop/BOX OFFICE.csv")
        print("CSV loaded successfully!")
        time.sleep(1)
        return df
    except:
        print("❌ File not found or error in reading file.")
        exit()

# ---------------------- Filter Functions (Case-insensitive with DataFrame output) ----------------------------

def filter_by_actor(df):
    name = input("Enter actor's name: ").lower()
    results = []
    for i in range(len(df)):
        if str(df.loc[i, 'ACTOR NAME']).lower() == name:
            results.append(df.loc[i, ['MOVIE NAME', 'ACTOR NAME', 'MONEY EARNED']])
    if results:
        output_df = pd.DataFrame(results)
        print("\nMATCHING MOVIES:\n")
        print(output_df.reset_index(drop=True))
    else:
        print("No matching actor found.")

def filter_by_actress(df):
    name = input("Enter actress's name: ").lower()
    results = []
    for i in range(len(df)):
        if str(df.loc[i, 'ACTRESS NAME']).lower() == name:
            results.append(df.loc[i, ['MOVIE NAME', 'ACTRESS NAME', 'MONEY EARNED']])
    if results:
        output_df = pd.DataFrame(results)
        print("\nMATCHING MOVIES:\n")
        print(output_df.reset_index(drop=True))
    else:
        print("No matching actress found.")

def filter_by_language(df):
    lang = input("Enter language: ").lower()
    results = []
    for i in range(len(df)):
        if str(df.loc[i, 'Language']).lower() == lang:
            results.append(df.loc[i, ['MOVIE NAME', 'Language', 'MONEY EARNED','RATING']])
    if results:
        output_df = pd.DataFrame(results)
        print("\nMATCHING MOVIES:\n")
        print(output_df.reset_index(drop=True))
    else:
        print("No matching language found.")

def filter_by_genre(df):
    genre = input("Enter genre (Romance, Action, Sci-Fi, Animation, Drama, Superhero, Horror,\n Comedy, Thriller, Fantasy, Adventure):").lower()
    results = []
    for i in range(len(df)):
        if str(df.loc[i, 'GENRE']).lower() == genre:
            results.append(df.loc[i, ['MOVIE NAME', 'GENRE', 'MONEY EARNED','Language']])
    if results:
        output_df = pd.DataFrame(results)
        print("\nMATCHING MOVIES:\n")
        print(output_df.reset_index(drop=True))
    else:
        print("No matching genre found.")

def filter_by_rating(df):
    try:
        rating = float(input("Enter minimum rating (e.g., 7.5): "))
        results = []
        for i in range(len(df)):
            if float(df.loc[i, 'RATING']) >= rating:
                results.append(df.loc[i, ['MOVIE NAME', 'RATING', 'MONEY EARNED']])
        if results:
            output_df = pd.DataFrame(results)
            print("\nMOVIES WITH RATING ",rating," OR ABOVE")
            print(output_df.reset_index(drop=True))
        else:
            print("No movies found with that rating or above.")
    except:
        print("Please enter a valid number.")

# ---------------------- Top Movies ----------------------------

def top_earning_movies(df):
    print("\nTOP 10 EARNING MOVIES:")
    top = df.sort_values(by='Money earned in millions', ascending=False).head(10)
    print(top[['MOVIE NAME', 'MONEY EARNED']].reset_index(drop=True))


def latest_movies(df):
    recent = df.sort_values(by='YEAR OF RELEASE', ascending=False).head(10)
    print("\nLATEST MOVIES:\n")
    print(recent[['MOVIE NAME', 'YEAR OF RELEASE', 'MONEY EARNED']].reset_index(drop=True))

def older_movies(df):
    try:
        year = int(input("Show movies before which year? "))
        result = df[df['YEAR OF RELEASE'] < year][['MOVIE NAME', 'YEAR OF RELEASE', 'MONEY EARNED']]
        if not result.empty:
            print("\nMOVIES RELEASED BEFORE",year,"\n")
            print(result.reset_index(drop=True))
        else:
            print("No movies found before that year.")
    except:
        print("Invalid year input.")

# ---------------------- Filter Menu ----------------------------

def filter_menu(df):
    while True:
        print("\nFILTER OPTIONS:")
        print("1. Search by Actor")
        print("2. Search by Actress")
        print("3. Search by Language")
        print("4. Search by Genre")
        print("5. Search by Ratings")
        print("6. Search Top Earning Movies")
        print("7. Search Latest Movies")
        print("8. Search Older Movies")
        print("9. Back to Main Menu")
        
        choice = input("Choose (1-9): ")
        if choice == '1':
            filter_by_actor(df)
        elif choice == '2':
            filter_by_actress(df)
        elif choice == '3':
            filter_by_language(df)
        elif choice == '4':
            filter_by_genre(df)
        elif choice == '5':
            filter_by_rating(df)
        elif choice == '6':
            top_earning_movies(df)
        elif choice == '7':
            latest_movies(df)
        elif choice == '8':
            older_movies(df)
        elif choice == '9':
            break
        else:
            print("Invalid choice. Try again.")
#------------------------Charts------------------------------------
def chart_menu(df):
    while True:
        print("\nCHART OPTIONS:")
        print("1. Chart of Money Earned")
        print("2. Chart of Rating")
        print("3. Back to main menu")
        choice = input("Choose (1-3): ")
        if choice == '1':
            # Plot money earned
            pl.figure(figsize=(12, 6))
            pl.bar(df['MOVIE NAME'], df['Money earned in millions'])
            pl.xticks(rotation=90)
            pl.xlabel('Movie Name')
            pl.ylabel('Money Earned (in Millions $)')
            pl.title('Money Earned by Movies')
            pl.tight_layout()
            pl.show()
        elif choice == '2':
            pl.figure(figsize=(12, 6))
            pl.bar(df['MOVIE NAME'], df['RATING'])
            pl.xticks(rotation=90)
            pl.xlabel('Movie Name')
            pl.ylabel('IMDB Rating')
            pl.title('IMDB Ratings of Movies')
            pl.tight_layout()
            pl.show()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")
# ----------------------------Edit---------------------------------
def edit_menu(df):
    while True:
        print("Choose the column you want to change:")
        print("1. Release Date")
        print("2. Year of Release")
        print("3. Money Earned")
        print("4. IMDB Rating")
        print("5. Actor Name")
        print("6. Actress Name")
        print("7. Genre")
        print("8. Language")
        print("9. Back to home page")
        
        column_option = input("Choose (1-9): ")
        if column_option == '1':
            movie_name = input("Enter the movie name to update release date: ").lower()
            lowermovie= df['MOVIE NAME'].str.lower()
            if movie_name in lowermovie.values:
                new_release_date = input("Enter the new release date (e.g., June 10, 2015): ")
                index_to_update = df[lowermovie == movie_name].index
                df.loc[index_to_update, 'DATE OF RELEASE'] = new_release_date
                print("Release date updated successfully.")
                print(df.loc[index_to_update])
            else:
                print("Movie not found in the data.")
        elif column_option == '2':
            movie_name = input("Enter the movie name to update year of release: ").lower()
            lowermovie= df['MOVIE NAME'].str.lower()
            if movie_name in lowermovie.values:
                new_year_of_release = input("Enter the new year of release(e.g. 2015): ")
                index_to_update = df[lowermovie == movie_name].index
                df.loc[index_to_update, 'YEAR OF RELEASE'] = new_year_of_release
                print("Release year updated successfully.")
                print(df.loc[index_to_update])
            else:
                print("Movie not found in the data.")

        elif column_option == '3':
            movie_name = input("Enter the movie name to update year of release: ").lower()
            lowermovie= df['MOVIE NAME'].str.lower()
            if movie_name in lowermovie.values:
                new_money_earned = input("Enter the new money earned(e.g. $15.5 million): ")
                index_to_update = df[lowermovie == movie_name].index
                df.loc[index_to_update, 'MONEY EARNED'] = new_money_earned
                print("Money earned, updated successfully.")
                print(df.loc[index_to_update])
            else:
                print("Movie not found in the data.")

        elif column_option == '4':
            movie_name = input("Enter the movie name to update rating: ").lower()
            lowermovie= df['MOVIE NAME'].str.lower()
            if movie_name in lowermovie.values:
                new_rating = input("Enter the new rating out of 10(e.g. 7.7): ")
                index_to_update = df[lowermovie == movie_name].index
                df.loc[index_to_update, 'RATING'] = new_rating
                print("Rating, updated successfully.")
                print(df.loc[index_to_update])
            else:
                print("Movie not found in the data.")

        elif column_option == '5':
            movie_name = input("Enter the movie name to update actor name: ").lower()
            lowermovie= df['MOVIE NAME'].str.lower()
            if movie_name in lowermovie.values:
                new_actor = input("Enter the new Actor name(e.g.Nathan Blaire): ")
                index_to_update = df[lowermovie == movie_name].index
                df.loc[index_to_update, 'ACTOR NAME'] = new_actor
                print("Actor Name, updated successfully.")
                print(df.loc[index_to_update])
            else:
                print("Movie not found in the data.")

        elif column_option == '6':
            movie_name = input("Enter the movie name to update actress name: ").lower()
            lowermovie= df['MOVIE NAME'].str.lower()
            if movie_name in lowermovie.values:
                new_actress = input("Enter the new Actress name(e.g. Emma Watson): ")
                index_to_update = df[lowermovie == movie_name].index
                df.loc[index_to_update, 'ACTRESS NAME'] = new_actress
                print("Actress Name, updated successfully.")
                print(df.loc[index_to_update])
            else:
                print("Movie not found in the data.")
                
        elif column_option == '7':
            movie_name = input("Enter the movie name to update genre: ").lower()
            lowermovie= df['MOVIE NAME'].str.lower()
            if movie_name in lowermovie.values:
                new_genre = input("Enter the new genre(e.g. Fantasy): ")
                index_to_update = df[lowermovie == movie_name].index
                df.loc[index_to_update, 'GENRE'] = new_genre
                print("Genre, updated successfully.")
                print(df.loc[index_to_update])
            else:
                print("Movie not found in the data.")

        elif column_option == '8':
            movie_name = input("Enter the movie name to update actress name: ").lower()
            lowermovie= df['MOVIE NAME'].str.lower()
            if movie_name in lowermovie.values:
                new_language = input("Enter the new language(e.g. English): ")
                index_to_update = df[lowermovie == movie_name].index
                df.loc[index_to_update, 'LANGUAGE'] = new_language
                print("Language, updated successfully.")
                print(df.loc[index_to_update])
            else:
                print("Movie not found in the data.")

        elif column_option == '9':
            break
        else:
            print("Invalid choice. Try again.")

#------------------------new entry---------------------------------
def entry(df):
    while True:
        Mv_name=input('Enter your movie name:')
        Release_date=input('Enter the release date, e.g. June 10, 2020:')
        Year_released=input('Enter the year of release:')
        Money_earned=input('Enter the money earned by movie,e.g. $1.2 billion:')
        Rating=input('Enter the rating, e.g. 7.8:')
        Actor_name=input('Enter the actor name, e.g. Shah Rukh Khan:')
        Actress_name=input('Enter the actress name, e.g. Alia Bhatt:')
        Genre=input('Enter the movie genre, e.g. fantasy:')
        Lang=input('Enter the language:')
        Mon_in_millions=input('Enter the money earned in millions, e.g. 15:')
        new_data={'MOVIE NAME':Mv_name,'DATE OF RELEASE':Release_date,
                  'YEAR OF RELEASE':Year_released,'MONEY EARNED':Money_earned,
                  'RATING':Rating,'ACTOR NAME':Actor_name,
                  'ACTRESS NAME':Actress_name,'GENRE':Genre,'Language':Lang,
                  'Money earned in millions':Mon_in_millions}
        df.loc[len(df)]=new_data
        print(df)
        break
# ---------------------- Main Menu --------------------------------

def main_menu(df):
    while True:
        print("\nMAIN MENU")
        print("1. Search Movies")
        print("2. View charts")
        print("3. Display movie list")
        print("4. Change/update list")
        print("5. Enter New Data")
        print("6. Delete Data")
        print("7. Save movie list")
        print("8. Exit")
        
        main_choice = input("Choose (1-8): ")
        if main_choice == '1':
            filter_menu(df)
        elif main_choice == '2':
            chart_menu(df)
        elif main_choice == '3':
            pd.set_option('display.max_rows', None)
            pd.set_option('display.max_columns', None)
            print(df)
        elif main_choice == '4':
            edit_menu(df)
        elif main_choice == '5':
            entry(df)
        elif main_choice == '6':
            dele_mv= input("Please enter movie name to be deleted: ").lower()
            if dele_mv in df['MOVIE NAME'].str.lower().values:
                df.drop(df[df['MOVIE NAME'].str.lower() == dele_mv].index,inplace=True)
                print("Movie deleted successfully.")
                print(df)
            else:
                print("Movie not found.")

        elif main_choice == '7':
            df.to_csv("/Users/santha/Desktop/CineSort_new.csv")
            print("File sucessfully downloaded!")
            
        elif main_choice == '8':
            print("Goodbye! Thank you for using CineSort!")
            break
        else:
            print("Invalid choice. Try again.")

# ---------------------- Main Function ----------------------------

def main():
    intro()
    df = load_data()
    main_menu(df)

main()

#-------------------------------------------------------------
