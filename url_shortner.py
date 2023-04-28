import tkinter as tk
import pyshorteners
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
import clipboard
import urllib.parse

def is_valid_url(url):
    parsed_url = urllib.parse.urlparse(url)
    return bool(parsed_url.scheme) and bool(parsed_url.netloc)
def shorten_url():
    url = url_entry.get()
    if not is_valid_url(url):
        msgbox.showerror("Error", "Invalid URL.")
        return
    if url == "" :
        short_label.configure(text="")
    else:
        shorten = pyshorteners.Shortener()
        flag = short_url = shorten.tinyurl.short(url)
        short_label.configure(text=short_url)

def copy_to_clipboard():
    short_url = short_label.cget("text")
    clipboard.copy(short_url)
    msgbox.showinfo("Copied", "The shortened URL has been copied to the clipboard.")


# create the main window
root = tk.Tk()
root.geometry("700x50")
root.title("URL Shortener")

# create a label and entry widget for entering the URL
Long_label = tk.Label(root, text="Enter URL:")
Long_label.pack(side=tk.LEFT)
url_entry = tk.Entry(root,width=50)
url_entry.pack(side=tk.LEFT)

# create a button for shortening the URL
shorten_button = tk.Button(root, text="Shorten URL", command=shorten_url)
shorten_button.pack(side=tk.LEFT)

# create a label for displaying the shortened URL
short_label = tk.Label(root, text="")
short_label.pack(side=tk.LEFT)

# create a button for copying the shortened URL to the clipboard
copy_button = ttk.Button(root, text="Copy", command=copy_to_clipboard)
copy_button.pack(side=tk.LEFT)

# start the main loop
root.mainloop()
