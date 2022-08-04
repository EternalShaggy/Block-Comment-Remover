import tkinter as tk
from tkinter import LEFT, RIGHT

class Comment_Remover():
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x500")
        self.root.resizable(False, False)
        self.root.title("Comment Remover")
        self.root.configure(bg="grey")


        self.document = tk.Text(root, width=100, height=25, border=0)  
        self.document.place(x=45,y=60)

        

        self.button = tk.Button(root, command=self.comment_remover, text="Strip", width=4,height=1, border=0)
        self.button.place(x=45,y=20)

    def comment_remover(self):
        out=[]
        f = self.document.get("1.0", "end").split("\n")
        for line in f:
            if('#' not in line) and (line!=''):
                out.append(line) 
        self.document.delete("1.0", "end")
        self.document.insert("1.0", "\n".join(out))


main = tk.Tk()
Comment_Remover(main)
main.mainloop()
