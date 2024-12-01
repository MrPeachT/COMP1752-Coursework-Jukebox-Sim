import tkinter as tk                        # import the tkinter library for GUI components
import tkinter.scrolledtext as tkst         # import scrolledtext widget for text boxes with scrollbars
import track_library as lib                 # import a custom library for managing track data
import font_manager as fonts                # import a custom library for managing font settings


def set_text(text_area, content):           # inserts content into the text_area 
    text_area.delete("1.0", tk.END)         # first the existing content is deleted
    text_area.insert(1.0, content)          # then the new content is inserted

class TrackViewer():
    def __init__(self, window):
        window.geometry("950x350")          # sets the size of the window
        window.title("View Tracks")         # sets the title of the window

        list_tracks_btn = tk.Button(window, text="List All Tracks", command=self.list_tracks_clicked)
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10) # adds the button to grid position (0, 0)

        enter_lbl = tk.Label(window, text="Enter Track Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)       # adds label to grid position (0, 1)

        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)  # text input field for track number

        check_track_btn = tk.Button(window, text="View Track", command=self.view_tracks_clicked)
        check_track_btn.grid(row=0, column=3, padx=10, pady=10) # button to view track details

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10) # adds a scrollable text area

        self.track_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10) # smaller text area for track details

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10) # status bar for messages

        self.list_tracks_clicked()

    def view_tracks_clicked(self):
        key = self.input_txt.get()  # retrieves the track number entered by the user
        name = lib.get_name(key)
        if name is not None:
            artist = lib.get_artist(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            track_details = f"{name}\n{artist}\nrating: {rating}\nplays: {play_count}"
            set_text(self.track_txt, track_details) # updates the track details text area
        else:
            set_text(self.track_txt, f"Track {key} not found")  # shows error in the text area
        self.status_lbl.configure(text="View Track button was clicked!")  # updates the status bar

    def list_tracks_clicked(self):
        track_list = lib.list_all()  # fetches the full list of tracks
        set_text(self.list_txt, track_list)  # updates the track list text area
        self.status_lbl.configure(text="List Tracks button was clicked!")  # updates the status bar

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    TrackViewer(window)     # open the TrackViewer GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc