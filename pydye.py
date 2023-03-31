import tkinter as tk
from tkinter import filedialog
from pygments import lex
from pygments.lexers.python import PythonLexer
from pygments.token import Token

class IDE:
    def __init__(self, root):
        self.root = root
        self.filename = None
        self.textbox = tk.Text(self.root)
        self.textbox.pack(expand=True, fill='both')
        self.textbox.tag_configure('Token.Keyword', foreground='blue')
        self.textbox.tag_configure('Token.Comment', foreground='gray')
        self.textbox.tag_configure('Token.String', foreground='green')
        self.textbox.tag_configure('Token.Name.Builtin', foreground='purple')
        self.textbox.tag_configure('Token.Operator', foreground='red')
        self.textbox.tag_configure('Token.Literal.Number', foreground='magenta')

        # Create buttons for opening and saving files
        open_button = tk.Button(self.root, text='Open', command=self.open_file)
        open_button.pack(side='left', padx=5)
        save_button = tk.Button(self.root, text='Save', command=self.save_file)
        save_button.pack(side='left', padx=5)

        # Create an "About" button
        about_button = tk.Button(self.root, text='About', command=self.display_about)
        about_button.pack(side='right', padx=5)

        # Set the background color of the root window to navy blue
        self.root.configure(bg='#001f3f')

    def open_file(self):
        self.filename = filedialog.askopenfilename()
        if self.filename:
            with open(self.filename, 'r') as f:
                file_contents = f.read()
                self.textbox.delete(1.0, 'end')
                self.textbox.insert('end', file_contents)
                self.highlight_syntax()

    def save_file(self):
        if not self.filename:
            self.filename = filedialog.asksaveasfilename()
        if self.filename:
            with open(self.filename, 'w') as f:
                f.write(self.textbox.get(1.0, 'end'))

    def highlight_syntax(self):
        code = self.textbox.get(1.0, 'end')
        tokens = lex(code, PythonLexer())
        for token_type, token_value in tokens:
            self.textbox.mark_set('start', f'{token_type[0]}linestart+{token_type[1]}c')
            self.textbox.mark_set('end', 'start+' + str(len(token_value)) + 'c')
            self.textbox.tag_add(str(token_type), 'start', 'end')

    def display_about(self):
        about_message = 'IDE Created by Mason Hood. Built on the Python Language.'
        tk.messagebox.showinfo('About', about_message)

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Pydye V0.1')
    ide = IDE(root)
    root.mainloop()
