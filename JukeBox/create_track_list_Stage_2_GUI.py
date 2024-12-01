import tkinter as tk                        
import tkinter.scrolledtext as tkst         
import track_library as lib                 
import font_manager as fonts                

class CreateTracksListAppGUIOnly:
    def __init__(self, window):
        window.geometry("700x400")
        window.title("Create Track List") 
        self.playlist = [] 
        fonts.configure() 

        self.track_number_label = tk.Label(window, text="Enter Track Number:")  
        self.track_number_label.grid(row=0, column=0, padx=10, pady=10)

        self.track_number_entry = tk.Entry(window, width=5)
        self.track_number_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.add_track_button = tk.Button(window, text="Add Track to Playlist") 
        self.add_track_button.grid(row=0, column=2, padx=10, pady=10)

        self.playlist_display = tkst.ScrolledText(window, width=50, height=10, wrap="none", state="disabled") 
        self.playlist_display.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        self.play_button = tk.Button(window, text="Play Playlist") 
        self.play_button.grid(row=3, column=0, padx=10, pady=10)

        self.reset_button = tk.Button(window, text="Reset Playlist")
        self.reset_button.grid(row=3, column=1, padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10)) 
        self.status_lbl.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    fonts.configure()   
    app = CreateTracksListAppGUIOnly(root)
    root.mainloop()