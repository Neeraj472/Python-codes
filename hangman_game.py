#                   Hangman game (you can also use images)
import tkinter as tk
import random as rd
r =tk.Tk()
r.title('Hangman game')
r.geometry("400x500")
r.config(bg="black")
word=""
guessed=""
attempts =6
#hang_image =[tk.PhotoImage(file=f"hang{i}.png") for i in range(7)]
stages = [
    """
     -----
     |   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """
]


def start():
    global word,guessed,attempts
    words=["python", "computer", "hangman", "science", "programming", "college"]
    word =rd.choice(words)
    guessed ="_"*len(word)
    attempts =6
    guessed_label.config(text=guessed)
    attempt_label.config(text=f"attempts left :{attempts}")
    result_label.config(text="")
    guess_entry.delete(0,tk.END)
    stage_label.config(text=stages[0],fg="white")
    #image_label.config(image=hang_image[0])

def check():
    global word,guessed,attempts
    guess =guess_entry.get().lower()
    guess_entry.delete(0,tk.END)
    
    if len(guess)!=1 and not guess.isalpha():
        result_label.config(text="please enter a single alphbet letter",fg="red")
        return
    
    if guess in word:
        new_guess =""
        for i in range(len(word)):
            if word[i]==guess:
                new_guess+=guess
            else:
                new_guess+=guessed[i]
        guessed =new_guess
        guessed_label.config(text=guessed)
        result_label.config(text="correct",fg="green")
    else:
        attempts-=1
        attempt_label.config(text=f"attempts left :{attempts}")
        result_label.config(text="Wrong",fg="red")
        stage_label.config(text=stages[6-attempts])
        #image_label.config(image=hang_image[6-attempts])
    if "_" not in guessed:
        result_label.config(text="you win",fg="#E8B938")
        return
    elif attempts==0:
        result_label.config(text=f"game over, the word is {word}")
        stage_label.config(text=stages[6],fg="red") 
        #image_label.config(image=hang_image[6])
                
        

game_name =tk.Label(r,text="Hangman game",font=("Arial",20),bg="black",fg="#940808")
game_name.pack(pady=10)

guessed_label =tk.Label(r,text="",font=("Arial",15),bg="black",fg="#328EB3")
guessed_label.pack(pady=10)

attempt_label =tk.Label(r,text="attempts left :6",font=("Arial",10),bg="black",fg="#328EB3")
attempt_label.pack(pady=5)

stage_label=tk.Label(r,text="",bg="black",fg="white")
stage_label.pack(pady=10)
#image_label =tk.Label(r,image=hang_image[0])
#image_label.pack(pady=10)

guess_entry =tk.Entry(r)
guess_entry.pack(pady=5)

start_button =tk.Button(r,text="start",font=("Arial",10),bg="green",fg="white",command=start)
start_button.pack(pady=5)
check_button =tk.Button(r,text="check",font=("Arial",10),bg="green",fg="white",command=check)
check_button.pack(pady=10,padx=20)
result_label =tk.Label(r,text="",font=("Arial",15),bg="black",fg="white")
result_label.pack(pady=10)

r.mainloop()