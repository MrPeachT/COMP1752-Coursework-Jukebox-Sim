import tkinter as tk                        
import tkinter.scrolledtext as tkst         
import track_library as lib                 
import font_manager as fonts                

class CreateTracksListApp:
    def __init__(self, window):
        window.geometry("700x400")
        window.title("Create Track List") 
        self.playlist = [] 
        fonts.configure() 

        self.track_number_label = tk.Label(window, text="Enter Track Number:")  
        self.track_number_label.grid(row=0, column=0, padx=10, pady=10)

        self.track_number_entry = tk.Entry(window, width=5)
        self.track_number_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.add_track_button = tk.Button(window, text="Add Track to Playlist", command=self.add_track) 
        self.add_track_button.grid(row=0, column=2, padx=10, pady=10)

        self.playlist_display = tkst.ScrolledText(window, width=50, height=10, wrap="none", state="disabled") 
        self.playlist_display.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        self.play_button = tk.Button(window, text="Play Playlist", command=self.play_playlist) 
        self.play_button.grid(row=3, column=0, padx=10, pady=10)

        self.reset_button = tk.Button(window, text="Reset Playlist", command=self.reset_playlist)
        self.reset_button.grid(row=3, column=1, padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10)) 
        self.status_lbl.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

    def add_track(self):
        track_number = self.track_number_entry.get()

        if track_number.isdigit() and lib.get_name(track_number) is not None:
            track_name = lib.get_name(track_number)
            self.playlist.append(track_number)
            self.update_playlist_display()
            self.status_lbl.config(text=f"Added {track_name} to playlist.")
        else:
            self.status_lbl.config(text="Invalid track number.")

    def update_playlist_display(self):
        self.playlist_display.config(state="normal")
        self.playlist_display.delete(1.0, tk.END)
        for track_number in self.playlist:
            track_name = lib.get_name(track_number)
            self.playlist_display.insert(tk.END, f"{track_number}: {track_name}\n")
        self.playlist_display.config(state="disabled")

    def play_playlist(self):
        for track_number in self.playlist:
            lib.increment_play_count(track_number)
        self.status_lbl.config(text="Played all tracks in the playlist.")

    def reset_playlist(self):
        self.playlist.clear()
        self.update_playlist_display()
        self.status_lbl.config(text="Playlist has been reset.")

if __name__ == "__main__":
    root = tk.Tk()
    fonts.configure()   
    app = CreateTracksListApp(root)
    root.mainloop()
