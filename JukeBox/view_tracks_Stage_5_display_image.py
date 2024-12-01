import tkinter as tk                        
import tkinter.scrolledtext as tkst         
import track_library as lib                 
import font_manager as fonts                

from PIL import Image, ImageTk   

def set_text(text_area, content):          
    text_area.delete("1.0", tk.END)         
    text_area.insert(1.0, content)         

class TrackViewer():
    def __init__(self, window):
        window.geometry("950x350")          
        window.title("View Tracks")                       

        list_tracks_btn = tk.Button(window, text="List All Tracks", command=self.list_tracks_clicked)
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10) 

        enter_lbl = tk.Label(window, text="Enter Track Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)       

        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10) 

        check_track_btn = tk.Button(window, text="View Track", command=self.view_tracks_clicked)
        check_track_btn.grid(row=0, column=3, padx=10, pady=10) 

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10) 

        self.track_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10) 
        
        self.image_label = tk.Label(window)
        self.image_label.grid(row=1, column=4, sticky="NW", padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10) 

        self.list_tracks_clicked()

    def view_tracks_clicked(self):
        key = self.input_txt.get()  
        name = lib.get_name(key)
        if name is not None:
            artist = lib.get_artist(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            track_details = f"{name}\n{artist}\nrating: {rating}\nplays: {play_count}"
            set_text(self.track_txt, track_details) 
            self.load_image(key)  
        else:
            set_text(self.track_txt, f"Track {key} not found") 
            self.image_label.config(image="") 
        self.status_lbl.configure(text="View Track button was clicked!")  

    def list_tracks_clicked(self):
        track_list = lib.list_all()  
        set_text(self.list_txt, track_list) 
        self.status_lbl.configure(text="List Tracks button was clicked!")  
        
    def load_image(self, key):
        try:
            img_path = f"images/{key}.jpg"
            img = Image.open(img_path)
            img = img.resize((150, 150))  
            img = ImageTk.PhotoImage(img) 
            self.image_label.config(image=img)
            self.image_label.image = img  
        except FileNotFoundError:
            self.image_label.config(image="")  
            self.status_lbl.configure(text=f"No image found for Track {key}")

if __name__ == "__main__":  
    window = tk.Tk()        
    fonts.configure()      
    TrackViewer(window)     
    window.mainloop()       