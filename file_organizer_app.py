import os
import shutil
from customtkinter import *
from tkinter import messagebox
from PIL import Image

# Variables to track files
skipped_files = 0
moved_files = 0

# Appearance
set_appearance_mode('Light')
# Making the window
app = CTk()
app.title("File Organizer")
app.geometry("1920x1080")
app.configure(fg_color="#FFFFFF")

# Extensions dictionary
extensions = {
    ".png": "Pictures",
    ".jpg": "Pictures",
    ".aseprite": "Pictures",
    ".gif": "Pictures",
    ".heic": "Pictures",
    ".heif": "Pictures",
    ".mp4": "Videos",
    ".avi": "Videos",
    ".pdf": "Documents",
    ".docx": "Documents",
    ".py": "Python",
    ".html": "WebDev",
    ".css": "WebDev",
    ".mp3": "Music",
    ".wav": "Music",
    ".m4a": "Music",
    ".mov": "Videos",
    ".rkt": "Racket"
}
def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_entry.delete(0, END)
        folder_entry.insert(0, folder_selected)

def organize_files():
    directory = folder_entry.get()
    
    if not directory:
        messagebox.showerror('Error!', 'Selected object is not a folder.')
        return
        
    if not os.path.exists(directory):
        messagebox.showerror('Error!', 'Directory does not exist.')
        return
    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        global moved_files
        global skipped_files
        
        if os.path.isfile(file_path):
            extension = os.path.splitext(filename)[1].lower()
            if extension in extensions:
                folder_name = extensions[extension]
                folder_path = os.path.join(directory, folder_name)
                os.makedirs(folder_path, exist_ok=True)
                
                destination_path = os.path.join(folder_path, filename)
                shutil.move(file_path, destination_path)
                
                print(f"Moved {filename} to {destination_path}.")
                moved_files += 1
                
            else:
                print(f"Skipped {filename}, unknown file extension.")
                skipped_files += 1
        else:
            print(f"Skipped {filename}, it is not a file.")
            skipped_files += 1
            
    print("File organization complete!")
    messagebox.showinfo("Success", 
                       f"Files organized successfully!\n\n"
                       f"📁 Files moved: {moved_files}\n"
                       f"⏭️ Files skipped: {skipped_files}")
    
#GUI
# Title at the top
header_full = CTkFrame(app, fg_color="transparent")
header_full.pack(fill="x", pady=(30, 20))

# Main horizontal container
main_horizontal = CTkFrame(app, fg_color="transparent")
main_horizontal.pack(expand=True, fill="both", padx=50, pady=30)

# Configure grid weights for proportional sizing
main_horizontal.grid_columnconfigure(0, weight=3)  # Left side - 3 parts
main_horizontal.grid_columnconfigure(1, weight=2)  # Right side - 2 parts (wider)
main_horizontal.grid_rowconfigure(0, weight=1)

# Left column
left_container = CTkFrame(main_horizontal, fg_color="transparent")
left_container.grid(row=0, column=0, sticky="nsew", padx=(0, 30))

# Right column
right_container = CTkFrame(main_horizontal, fg_color="transparent")
right_container.grid(row=0, column=1, sticky="nsew")
# Header section
header_frame = CTkFrame(header_full, fg_color="transparent")
header_frame.pack(pady=(0, 0))


folder_image = CTkImage(light_image=Image.open("/Users/zishine/VSCODE/Python/foldersprite.png"), size=(160,160))
folderimage = CTkLabel(header_frame, image=folder_image, text=' ')
folderimage.pack()

title = CTkLabel(header_frame, text=('File Organizer'),
                 font=CTkFont(family='Upheaval TT (BRK)', size=80, weight='bold'), text_color="#192832")
title.pack(pady=(5, 5))

subheading = CTkLabel(header_frame, text=('Organize all the files in any directory on your computer!'),
                      font=CTkFont(family='Upheaval TT (BRK)', size=20), text_color="#718186")
subheading.pack()

card = CTkFrame(left_container, 
                     fg_color="#F8F9FA", 
                     border_color="#E9ECEF", 
                     border_width=2,
                     corner_radius=20)
card.pack(fill="x", pady=(0,20), ipady = 10)

CTkLabel(card, 
         text="Select Folder to Organize",
         font=CTkFont(family='Upheaval TT (BRK)', size=30, weight='bold'),
         text_color="#0098DC").pack(pady=(25, 15))

# Folder input with button
input_frame = CTkFrame(card, fg_color="transparent")
input_frame.pack(fill="x", padx=30, pady=15)
# Info text or features inside the card
info_text = CTkLabel(card, 
                    text="• Supports 15+ file types\n• Creates organized folders automatically\n• Check your files after!",
                    font=CTkFont(family='Upheaval TT (BRK)', size=16),
                    text_color="#718186",
                    justify="left")
info_text.pack(pady=0)

folder_entry = CTkEntry(input_frame, height=50, width=650,
                        placeholder_text=("Click 'Browse' to select a folder, or paste the path here..."),
                        font=CTkFont(family='Upheaval TT (BRK)', size=20))
folder_entry.pack(side='left', fill='x', expand=True, padx=(0,10))

browse_button = CTkButton(input_frame, height=50, width=120,
                          text=('Browse'), command=browse_folder,
                          font=CTkFont(family='Upheaval TT (BRK)', size=20),
                          fg_color="#0098DC",
                          hover_color="#0069AA")
browse_button.pack(side='right')
# Action section
action_frame = CTkFrame(left_container, fg_color="transparent")
action_frame.pack(pady=0)

organize_button = CTkButton(action_frame, 
                           text="🚀 Start Organizing!", 
                           command=organize_files, 
                           font=CTkFont(family='Upheaval TT (BRK)', size=30, weight='bold'),
                           height=60,
                           width=400,
                           fg_color="#5AC54F",
                           hover_color="#33984B",
                           text_color="white",
                           corner_radius=15)
organize_button.pack(pady=(15,0))

# Right sidebar
features_card = CTkFrame(right_container, 
                        fg_color="#F8F9FA", 
                        border_color="#E9ECEF", 
                        border_width=2,
                        corner_radius=20)
features_card.pack(fill="both", pady=(0, 15))

CTkLabel(features_card, 
         text="Supported File Types",
         font=CTkFont(family='Upheaval TT (BRK)', size=30, weight='bold'),
         text_color="#0098DC").pack(pady=(25, 10))

features_frame = CTkFrame(features_card, fg_color="transparent")
features_frame.pack(fill="both", expand=True, padx=20, pady=10, ipady=(10))

file_categories = [
    "🖼️  Images (.png, .jpg, .gif)",
    "🎵  Music (.mp3, .wav, .m4a)",
    "🎬  Videos (.mp4, .mov, .avi)", 
    "📄  Documents (.pdf, .docx)",
    "💻  Code (.py, .html, .css, .rkt)",
    "🎨  Other (.aseprite)"
]

for category in file_categories:
    CTkLabel(features_frame, 
             text=category,
             font=CTkFont(family='Upheaval TT (BRK)', size=16),
             text_color="#718186").pack(anchor="w", pady=3)
app.mainloop()