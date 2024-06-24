import tkinter as tk
from spellchecker import SpellChecker

# Initialize the spellchecker
spell = SpellChecker()

def autocorrect(word):
    if word in spell:
        return word
    else:
        suggestions = spell.candidates(word)
        if suggestions:
            return suggestions.pop()
        else:
            return word

def on_key_release(event):
    # Get the content of the input field
    input_text = text_input.get("1.0", tk.END).strip()
    # Split the text into words
    words = input_text.split()
    corrected_text = ' '.join([autocorrect(word) for word in words])
    # Update the output field with corrected text
    text_output.config(state=tk.NORMAL)
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, corrected_text)
    text_output.config(state=tk.DISABLED)

# Set up the main application window
root = tk.Tk()
root.title("Autocorrect Keyboard")

# Input text widget
text_input = tk.Text(root, height=3, width=50)
text_input.pack()
text_input.bind("<KeyRelease>", on_key_release)

# Output text widget
text_output = tk.Text(root, height=3, width=50, state=tk.DISABLED)
text_output.pack()

# Run the application
root.mainloop()
