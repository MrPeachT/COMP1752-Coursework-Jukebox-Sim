import tkinter as tk
import tkinter.scrolledtext as tkst
from PIL import Image, ImageTk
import track_library_Stage_5_csv as lib
import font_manager as fonts

class AppUI:
    def __init__(self, root):
        root.geometry("900x550")
        root.title("App UI")
        fonts.configure()

        lib.load_from_csv()

        tk.Label(root, text="Taoist MP3", font=("Helvetica", 16, "bold")).pack(pady=10)

        input_frame = tk.Frame(root)
        input_frame.pack(pady=10)
        tk.Label(input_frame, text="Track Number:").pack(side="left", padx=5)
        self.track_number_entry = tk.Entry(input_frame, width=5)
        self.track_number_entry.pack(side="left", padx=5)

        tk.Button(input_frame, text="View Track", command=self.view_track).pack(side="left", padx=5)
        tk.Button(input_frame, text="Add to Playlist", command=self.add_to_playlist).pack(side="left", padx=5)
        tk.Button(input_frame, text="Update Rating", command=self.update_rating).pack(side="left", padx=5)

        tk.Label(input_frame, text="New Rating (1-5):").pack(side="left", padx=5)
        self.new_rating_entry = tk.Entry(input_frame, width=5)
        self.new_rating_entry.pack(side="left", padx=5)

        display_frame = tk.Frame(root)
        display_frame.pack(pady=10)
        
        self.track_details = tkst.ScrolledText(display_frame, width=40, height=10, wrap="none", state="disabled")
        self.track_details.grid(row=0, column=0, padx=10)

        self.image_label = tk.Label(display_frame)
        self.image_label.grid(row=0, column=1, padx=10)

        playlist_frame = tk.Frame(root)
        playlist_frame.pack(pady=10)
        
        tk.Label(playlist_frame, text="Playlist:", font=("Helvetica", 12)).grid(row=0, column=0, sticky="w")
        self.playlist_display = tkst.ScrolledText(playlist_frame, width=60, height=5, wrap="none", state="disabled")
        self.playlist_display.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        tk.Button(playlist_frame, text="Play Playlist", command=self.play_playlist).grid(row=2, column=0, pady=5, sticky="w")
        tk.Button(playlist_frame, text="Reset Playlist", command=self.reset_playlist).grid(row=2, column=1, pady=5, sticky="e")

        self.status_label = tk.Label(root, text="", font=("Helvetica", 10))
        self.status_label.pack(pady=5)

        self.playlist = [] 

    def view_track(self):
        key = self.track_number_entry.get().strip()
        if lib.get_name(key):
            name, artist, rating, plays = lib.get_name(key), lib.get_artist(key), lib.get_rating(key), lib.get_play_count(key)
            self.track_details.config(state="normal")
            self.track_details.delete(1.0, tk.END)
            self.track_details.insert(tk.END, f"Name: {name}\nArtist: {artist}\nRating: {rating}\nPlays: {plays}")
            self.track_details.config(state="disabled")
            self.load_image(key)
            self.status_label.config(text="Track details loaded.")
        else:
            self.track_details.config(state="normal")
            self.track_details.delete(1.0, tk.END)
            self.track_details.insert(tk.END, "Track not found.")
            self.track_details.config(state="disabled")
            self.image_label.config(image="")
            self.status_label.config(text="Track not found.")

    def load_image(self, key):
        try:
            img = Image.open(f"images/{key}.jpg").resize((150, 150))
            img = ImageTk.PhotoImage(img)
            self.image_label.config(image=img)
            self.image_label.image = img
        except FileNotFoundError:
            self.image_label.config(image="")
            self.status_label.config(text="No image found for the track.")

    def add_to_playlist(self):
        key = self.track_number_entry.get().strip()
        if key.isdigit() and lib.get_name(key):
            self.playlist.append(key)
            self.update_playlist_display()
            self.status_label.config(text=f"Added {lib.get_name(key)} to playlist.")
        else:
            self.status_label.config(text="Invalid track number.")

    def update_playlist_display(self):
        self.playlist_display.config(state="normal")
        self.playlist_display.delete(1.0, tk.END)
        for key in self.playlist:
            self.playlist_display.insert(tk.END, f"{key}: {lib.get_name(key)}\n")
        self.playlist_display.config(state="disabled")

    def play_playlist(self):
        for key in self.playlist:
            lib.increment_play_count(key)
        self.status_label.config(text="Played all tracks in the playlist.")

    def reset_playlist(self):
        self.playlist.clear()
        self.update_playlist_display()
        self.status_label.config(text="Playlist has been reset.")

    def update_rating(self):
        key = self.track_number_entry.get().strip()
        new_rating = self.new_rating_entry.get().strip()
        if key.isdigit() and lib.get_name(key):
            if new_rating.isdigit() and 1 <= int(new_rating) <= 5:
                lib.set_rating(key, int(new_rating))
                self.status_label.config(text=f"Updated {lib.get_name(key)} to rating {new_rating}.")
                self.view_track()  
            else:
                self.status_label.config(text="Invalid rating. Enter a number between 1 and 5.")
        else:
            self.status_label.config(text="Invalid track number.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AppUI(root)
    root.mainloop()
