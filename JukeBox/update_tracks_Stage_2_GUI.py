import tkinter as tk            
import track_library as lib
import font_manager as fonts

class UpdateTracksAppGUIOnly:
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

        self.update_button = tk.Button(window, text="Update Rating")
        self.update_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    fonts.configure()               
    app = UpdateTracksAppGUIOnly(root)
    root.mainloop()
