# Palindrome Checker Program
# Version 2.0
# Created by Han
# Finished on 21/4/2020

# import tkinter module
import tkinter as tk


# function to check user input for palindrome
def valid_palindrome(entry):

    formated_entry = entry.upper()
    for i in range(len(formated_entry)):
        if formated_entry[i] != formated_entry[-i-1]:
            result = "Not a palindrome."
            break
    else:
        result = "It's palindrome!"

    # allocate function result to label container in GUI
    label['text'] = result


# start of tkinter GUI program
root = tk.Tk()
root.title('Palindrome Verification Program Version 2.0')

canvas = tk.Canvas(root, height=150, width=500)
canvas.pack()

frame1 = tk.Label(root, bg='#6A6A6A')
frame1.place(relwidth=1, relheight=1)

upper_frame = tk.Frame(root)
upper_frame.place(relx=0.5, rely=0.04, relwidth=0.9, relheight=0.25, anchor='n')

upper_label = tk.Label(upper_frame, font='Consolas 20' ,bg='#6A6A6A', fg='#CDCCCE', anchor='w', text="Palindrome Checker")
upper_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#B5B5B5',bd=1)
frame.place(relx=0.5, rely=0.3, relwidth=0.9, relheight=0.3, anchor='n')

entry = tk.Entry(frame, font='Consolas 18', bg="#6A6A6A",fg='white', relief="flat")
entry.place(relwidth=1, relheight=1)

lower_frame = tk.Frame(root,bg='#6A6A6A')
lower_frame.place(relx=0.5, rely=0.62, relwidth=0.9, relheight=0.3, anchor='n')

button = tk.Button(lower_frame, text="Check for palindrome-ness",bg="green",fg="white", anchor="w", font='Consolas 11',relief="flat",command=lambda: valid_palindrome(entry.get()))
button.place(relx=0, rely=0.1, relheight=1, relwidth=0.46)

label = tk.Label(lower_frame, font='Helvetica 15' ,bg='#6A6A6A', fg='#5BC858', anchor='w')
label.place(relx=0.48, rely=0.1, relwidth=0.5, relheight=1)

root.mainloop()
