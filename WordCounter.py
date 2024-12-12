import tkinter as tk
from tkinter import messagebox


class WordCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Counter - Like Word")
        self.root.geometry("800x600")
        
        # Create the text editor
        self.text_area = tk.Text(root, wrap=tk.WORD, font=("Arial", 12))
        self.text_area.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Add a menu bar
        self.menu_bar = tk.Menu(root)
        root.config(menu=self.menu_bar)
        
        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Exit", command=root.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        
        # Edit menu
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Word Count", command=self.word_count_popup)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        
        # Status bar
        self.status_bar = tk.Label(root, text="Words: 0 | Characters: 0", anchor=tk.W, bg="lightgray", font=("Arial", 10))
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Bind events to dynamically update word/character counts
        self.text_area.bind("<KeyRelease>", self.update_status_bar)

    def new_file(self):
        """Clear the text area for a new file."""
        if messagebox.askyesno("Confirm", "Are you sure you want to create a new file?"):
            self.text_area.delete("1.0", tk.END)
            self.update_status_bar()

    def open_file(self):
        """Open a text file and display its contents."""
        from tkinter.filedialog import askopenfilename
        
        file_path = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert("1.0", content)
            self.update_status_bar()

    def save_file(self):
        """Save the current text to a file."""
        from tkinter.filedialog import asksaveasfilename
        
        file_path = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(self.text_area.get("1.0", tk.END).strip())
            messagebox.showinfo("Success", "File saved successfully!")

    def word_count_popup(self):
        """Show a popup with the word and character count."""
        text = self.text_area.get("1.0", tk.END).strip()
        word_count = len(text.split())
        char_count = len(text)
        messagebox.showinfo("Word Count", f"Words: {word_count}\nCharacters: {char_count}")

    def update_status_bar(self, event=None):
        """Update the status bar with the word and character count."""
        text = self.text_area.get("1.0", tk.END).strip()
        word_count = len(text.split())
        char_count = len(text)
        self.status_bar.config(text=f"Words: {word_count} | Characters: {char_count}")


if __name__ == "__main__":
    root = tk.Tk()
    app = WordCounterApp(root)
    root.mainloop()
