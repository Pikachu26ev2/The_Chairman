import tkinter as tk
import time

#settings
gameStart = 0
tmp = 1

def on_spacebar_press(event):
    if gameStart != 3:
        LoadScene() 

def on_w_press(event):
    global tmp

    if gameStart == 0:
        if tmp < 2:
            tmp = 2
        elif tmp > 1:
            tmp = 1 
    
    LoadAssets()
def on_s_press(event):
    global tmp
    if gameStart == 0:
        if tmp < 2:
            tmp = 2
        elif tmp > 1:
            tmp = 1 
    
    LoadAssets()
def on_enter_press(event):
    global gameStart
    if gameStart != 3:
        if tmp == 1:
            gameStart = 1
        elif tmp == 2:
            if gameStart == 0:
                gameStart = 2
            else:    
                gameStart = 0
        LoadAssets()

def type_text(text, idx=0, tmp_text=""):
            if idx < len(text):
                tmp_text += text[idx]
                canvas.itemconfig(text_id2, text=tmp_text)
                root.after(int(textSpeed * 1000), type_text, text, idx + 1, tmp_text)


root = tk.Tk()
root.resizable(False, False)
root.title("The Chairman")
root.overrideredirect(False)

#variables
with open("story.tronsky", "r") as file:
    saveCode = file.readlines()
with open("names.txt", "r") as file:
    names = file.readlines()
with open("settings.txt", "r") as file:
    settings = file.readlines()

saveIDX = 0
saveCode = "".join(saveCode)
value = ""
c1 = ""
c2 = ""
c3 = ""
cs = ""
dtext = ""
bg = ""


#functions(aka python's custom blocks, those pink blocks from scratch)
def ReadValue ():
    global saveIDX
    global saveCode
    global value
    value = ""
    
    c = saveCode[saveIDX].strip()
    while c != "|":  
        c = saveCode[saveIDX].strip()
        saveIDX += 1
        if saveIDX >= len(saveCode):  
            break
        if c == "|":  
            break
        value = value + c
        if c == "":
            value = value + " "
    return value
    

def LoadScene ():
    tmp2 = ReadValue()
    if tmp2 == "text":
        global c1
        global c2
        global c3
        global cs
        global dtext
        global bg
        c1 = ReadValue()
        c2 = ReadValue()
        c3 = ReadValue()
        cs = ReadValue()
        dtext = ReadValue()
    elif tmp2 == "bg":
        bg = ReadValue()
        LoadScene()
    elif tmp2 == "end":
        global gameStart
        gameStart = 3
    LoadAssets()

#key presses
root.bind("<space>", on_spacebar_press)
root.bind("<Return>", on_enter_press)
root.bind("<w>", on_w_press)
root.bind("<s>", on_s_press)
root.bind("<Up>", on_w_press)
root.bind("<Down>", on_s_press)

def LoadAssets ():
    canvas.delete("all")
    if gameStart == 1:
        global c1
        global c2
        global c3
        global cs
        global dtext
        global bg
        global tmp 

        
        #characters
        char1 = tk.PhotoImage(file="char/_" + c1 + ".png")
        char2 = tk.PhotoImage(file="char/_" + c2 + ".png")
        char3 = tk.PhotoImage(file="char/_" + c3 + ".png")
        page = tk.PhotoImage(file="char/page.png")
        background = tk.PhotoImage(file="background/_" + bg + ".png")

        #window


        #paint characters
        canvas.create_image(480*sizeDelta, 360*sizeDelta2, image=background)
        canvas.image = background
        canvas.create_image(140*sizeDelta, 600*sizeDelta2, image=char1)
        canvas.image = char1
        canvas.create_image(480*sizeDelta, 600*sizeDelta2, image=char2)
        canvas.image = char2
        canvas.create_image(820*sizeDelta, 600*sizeDelta2, image=char3)
        canvas.image = char3
        canvas.create_image(480*sizeDelta, 580*sizeDelta2, image=page)
        canvas.image = page
        text_id = canvas.create_text(100*sizeDelta, 500*sizeDelta2, text=names[int(cs) - 1], font=("Ubuntu", 24), fill="red", anchor="nw")
        global text_id2
        text_id2 = canvas.create_text(100*sizeDelta, 530*sizeDelta2, text="", font=("Ubuntu", 24), fill="black", anchor="nw", width=760*sizeDelta)
        type_text(dtext)



            

    if gameStart == 0:
        canvas.create_image(480*sizeDelta, 360*sizeDelta2, image=backgr)
        canvas.image = backgr
        if tmp == 1:
            canvas.create_text(100*sizeDelta, 300*sizeDelta2, text="> START", font=("Rubik", 80, "bold"), fill="black", anchor="w")
            canvas.create_text(100*sizeDelta, 400*sizeDelta2, text="CREDITS", font=("Rubik", 80, "bold"), fill="black", anchor="w")
        else:
            canvas.create_text(100*sizeDelta, 300*sizeDelta2, text="START", font=("Rubik", 80, "bold"), fill="black", anchor="w")
            canvas.create_text(100*sizeDelta, 400*sizeDelta2, text="> CREDITS", font=("Rubik", 80, "bold"), fill="black", anchor="w") 
    if gameStart == 2:
        canvas.create_text(480*sizeDelta, 100*sizeDelta2, text="PROGRAMMERS", font=("Rubik", 80, "bold"), fill="black", anchor="center")
        canvas.create_text(480*sizeDelta, 200*sizeDelta2, text="Poka26ev2", font=("Rubik", 40, "bold"), fill="black", anchor="center")
        canvas.create_text(480*sizeDelta, 300*sizeDelta2, text="STORY MADE BY", font=("Rubik", 80, "bold"), fill="black", anchor="center")
        canvas.create_text(480*sizeDelta, 400*sizeDelta2, text=settings[1], font=("Rubik", 40, "bold"), fill="black", anchor="center")
        canvas.create_text(480*sizeDelta, 500*sizeDelta2, text="Press ENTER to go back", font=("Rubik", 40, "bold"), fill="black", anchor="center")
    if gameStart == 3:
        backgr2 = tk.PhotoImage(file="assets/ending.png")
        canvas.create_image(480*sizeDelta, 360*sizeDelta2, image=backgr2)
        canvas.image = backgr2
    
    root.mainloop()

backgr = tk.PhotoImage(file="assets/backgr.png")
textSpeed = settings[2]
textSpeed = float(textSpeed)
sizeDelta = int(settings[0]) / 960
sizeDelta2 = sizeDelta
canvas = tk.Canvas(root, width=settings[0], height=720*sizeDelta, bg="lightblue")
canvas.pack()
#close_button = tk.Button(root, text="Close", command=root.destroy)
#close_button.place(x=0, y=0)
ReadValue()
LoadScene()
