import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = '2a60cb5a'

def get_rating():
    movie_title = entry_movie.get()
    if movie_title:
        url = f"http://www.omdbapi.com/?s={movie_title}&apikey={API_KEY}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data["Response"] == "True":
                print(data['Search'][0]['imdbID'])
                url2 = f"http://www.omdbapi.com/?i={data['Search'][0]['imdbID']}&apikey={API_KEY}"
                response_movie = requests.get(url2)
                if response_movie.status_code == 200:
                    data_movie = response_movie.json()
                    print(data_movie)
                    if data_movie["Response"] == "True":
                        rating = data_movie["imdbRating"]
                        messagebox.showinfo("Movie-Rating", f"The rating of {movie_title} and is {rating}")
                    else:
                        messagebox.showerror("Error", f"{movie_title} can't find")
                else:
                    messagebox.showerror("Error", "Error making request")
            else:
                messagebox.showerror("Error", f"{movie_title} can't find")
        else:
            messagebox.showerror("Error", "Error making request")
        entry_movie.delete(0, tk.END)
        
    else:
        messagebox.showerror("Error", "Please, enter title of a movie")
        
#Create main window
window = tk.Tk()
window.title("Find score of a movie")

#Label and input for movie title
movie_label = tk.Label(window, text="Movie title: ")
movie_label.pack()
entry_movie = tk.Entry(window)
entry_movie.pack()

#Custom button to get rating
btn_get_score = tk.Button(window, text="Get rating", command=get_rating)
btn_get_score.pack()

#Execute events in the window
window.mainloop()