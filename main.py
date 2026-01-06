from tkinter import *
from tkinter import filedialog
from FaceShape import detectFaceShape
from PIL import ImageTk, Image
import os
import random
from new import newFaceShape


def open_photo():
    filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    FaceShape = detectFaceShape(filepath)
    shapeOfFace = newFaceShape(filepath)
    shape_label.config(text=shapeOfFace)


path = "C:\Pycharm\MiniProject\EarRings\\"
files = os.listdir(path)
ear_rings_list = []
for file in files:
    if file.endswith(('.jpg', '.png', 'jpeg')):
        img_path = ear_rings_list.append(file)

N_path = "C:\Pycharm\MiniProject\\Necklace\\"
N_files = os.listdir(N_path)
necklace_list = []
for file in N_files:
    if file.endswith(('.jpg', '.png', 'jpeg')):
        img_path = necklace_list.append(file)

M_ER_path = "C:\Pycharm\MiniProject\MER\\"
M_ER_files = os.listdir(M_ER_path)
M_ER_list = []
for file in M_ER_files:
    if file.endswith(('.jpg', '.png', 'jpeg')):
        img_path = M_ER_list.append(file)

MN_path = "C:\Pycharm\MiniProject\MN\\"
MN_files = os.listdir(MN_path)
MN_list = []
for file in MN_files:
    if file.endswith(('.jpg', '.png', 'jpeg')):
        img_path = MN_list.append(file)

fb_path = "C:\Pycharm\MiniProject\FB\\"
files = os.listdir(fb_path)
fb_list = []
for file in files:
    if file.endswith(('.jpg', '.png', 'jpeg')):
        img_path = fb_list.append(file)

mb_path = "C:\Pycharm\MiniProject\MB\\"
files = os.listdir(mb_path)
mb_list = []
for file in files:
    if file.endswith(('.jpg', '.png', 'jpeg')):
        img_path = mb_list.append(file)


def selection():
    selected_option = radio.get()
    gender_option = gender.get()
    ear_ring_path = "C:\Pycharm\MiniProject\EarRings\\"
    necklace_path = "C:\Pycharm\MiniProject\\Necklace\\"
    MN_path = "C:\Pycharm\MiniProject\MN\\"
    M_ER_path = "C:\Pycharm\MiniProject\MER\\"
    mb_path = "C:\Pycharm\MiniProject\MB\\"
    fb_path = "C:\Pycharm\MiniProject\FB\\"
    if selected_option == 1 and gender_option == 1:
        M_ER_path = M_ER_path + random.choice(M_ER_list)
        img = Image.open(M_ER_path)
        img = img.resize((500, 500))
        img.show()
    if selected_option == 2 and gender_option == 1:
        MN_path = MN_path + random.choice(MN_list)
        img = Image.open(MN_path)
        img = img.resize((500, 500))
        img.show()
    if selected_option == 1 and gender_option == 2:
        ear_ring_path = ear_ring_path + random.choice(ear_rings_list)
        img = Image.open(ear_ring_path)
        img = img.resize((500, 500))
        img.show()
    if selected_option == 2 and gender_option == 2:
        necklace_path = necklace_path + random.choice(necklace_list)
        img = Image.open(necklace_path)
        img = img.resize((500, 500))
        img.show()
    if selected_option == 1 and gender_option == 3:
        ear_ring_path = ear_ring_path + random.choice(ear_rings_list)
        img = Image.open(ear_ring_path)
        img = img.resize((500, 500))
        img.show()
    if selected_option == 2 and gender_option == 3:
        necklace_path = necklace_path + random.choice(necklace_list)
        img = Image.open(necklace_path)
        img = img.resize((500, 500))
        img.show()
    if selected_option == 3 and gender_option == 1:
        mb_path = mb_path + random.choice(mb_list)
        img = Image.open(mb_path)
        img = img.resize((500, 500))
        img.show()
    if selected_option == 3 and gender_option == 2:
        fb_path = fb_path + random.choice(fb_list)
        img = Image.open(fb_path)
        img = img.resize((500, 500))
        img.show()
    if selected_option == 3 and gender_option == 3:
        fb_path = fb_path + random.choice(fb_list)
        img = Image.open(fb_path)
        img = img.resize((500, 500))
        img.show()


win = Tk()
win.geometry("1000x1000")
win.resizable(0, 0)
bg_image = Image.open("D:\REquired\Mini Project CD\MiniProject\\bg.jpg")
bg_image = bg_image.resize((1000, 1000))
background_photo = ImageTk.PhotoImage(bg_image)
background_label = Label(win, image=background_photo)
background_label.place(x=0, y=0)
win.title("Fashion Accesory Recommendation System Accompanied With Augmented Reality")
Label(win, text="Upload Photo", fg="Purple", font="san-serif 18 bold").place(x=300, y=70)
open_button = Button(win, text="Upload Photo", font="san-serif 15 bold", command=open_photo)
open_button.place(x=500, y=70)

shape_label = Label(win, text="", fg="Black", font="san-serif 22 bold")
shape_label.place(x=430, y=600)

Label(win, text="Select Accesory", fg="Purple", font="san-serif 15 bold").place(x=420, y=340)
radio = IntVar()
R1 = Radiobutton(win, text="Ear Rings", variable=radio, font="san-serif 15 bold", value=1)
R1.place(x=430, y=370)
R2 = Radiobutton(win, text="Necklace", variable=radio, font="san-serif 15 bold", value=2)
R2.place(x=430, y=400)
R3 = Radiobutton(win, text="Bangles", variable=radio, font="san-serif 15 bold", value=3)
R3.place(x=430, y=430)
item_button = Button(win, text="Get Item", font="san-serif 15 bold", command=selection).place(x=420, y=480)
photo_label = Label(win).pack()

Label(win, text="Gender", fg="Purple", font="san-serif 15 bold").place(x=430, y=160)
gender = IntVar()
R3 = Radiobutton(win, text="Male", variable=gender, font="san-serif 15 bold", value=1)
R3.place(x=430, y=190)
R4 = Radiobutton(win, text="Female", variable=gender, font="san-serif 15 bold", value=2)
R4.place(x=430, y=220)
R5 = Radiobutton(win, text="Other", variable=gender, font="san-serif 15 bold", value=3)
R5.place(x=430, y=250)

win.mainloop()
