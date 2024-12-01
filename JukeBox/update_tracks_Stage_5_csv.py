import tkinter as tk            
import track_library_Stage_5_csv as lib
import font_manager as fonts

class UpdateTracksApp:
    def __init__(self, window):
        window.geometry("500x250")
        window.title("Update Track Rating")
        fonts.configure()

        self.track_number_label = tk.Label(window, text="Enter Track Number:")
        self.track_number_label.grid(row=0, column=0, padx=10, pady=10)

        self.track_number_entry = tk.Entry(window, width=5)
        self.track_number_entry.grid(row=0, column=1, padx=10, pady=10)

        self.new_rating_label = tk.Label(window, text="Enter New Rating (1-5):")
        self.new_rating_label.grid(row=1, column=0, padx=10, pady=10)

        self.new_rating_entry = tk.Entry(window, width=5)
        self.new_rating_entry.grid(row=1, column=1, padx=10, pady=10)

        self.update_button = tk.Button(window, text="Update Rating", command=self.update_rating)
        self.update_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def update_rating(self):
        track_number = self.track_number_entry.get()
        new_rating = self.new_rating_entry.get()

        if track_number.isdigit():
            track_name = lib.get_name(track_number)
            if track_name is not None:
                if new_rating.isdigit() and 1 <= int(new_rating) <= 5:
                    lib.set_rating(track_number, int(new_rating))
                    
                    play_count = lib.get_play_count(track_number)
                    self.status_lbl.config(text=f"{track_name}: New rating - {new_rating}, Plays - {play_count}")
                else:
                    self.status_lbl.config(text="Invalid rating. Please enter a value between 1 and 5.")
            else:
                self.status_lbl.config(text="Track not found. Please enter a valid track number.")
        else:
            self.status_lbl.config(text="Invalid track number. Please enter a numeric value.")

if __name__ == "__main__":
    root = tk.Tk()
    fonts.configure()               
    app = UpdateTracksApp(root)
    root.mainloop()
