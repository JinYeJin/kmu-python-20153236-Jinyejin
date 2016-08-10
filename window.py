from tkinter import *


def gen_entry(main_win):

    name_index = 0;
    entry_group = ["이름: ", "점수: ", "번호: ", "파일이름: ", "파일이름: "]
    bgcolor = "light green"

    # generate entry frame
    entry_frame = Frame(main_win).grid(row = 0, column = 0, columnspan = 10, sticky = W)

    for i in range(0, len(entry_group) * 2, 2):
        Label(entry_frame, text=entry_group[name_index]).grid(row= i, column = 2, sticky=W)
        entry = Entry(entry_frame, width=20, bg = bgcolor).grid(row=i, column = 3, sticky=W)
        name_index += 1


def gen_button(main_win):

    button_group = ["추가", "삭제", "저장", "열기"]

    #generate button frame
    button_frame = Frame(main_win).grid(row = 0, column = 0, columnspan = 10, sticky = W)

    for i in range(len(button_group)):
        button = Button(button_frame, text = button_group[i], width = 5).grid(row = i, column = 6)

def gen_range_button(main_win):

    button_group = ["번호순", "이름순", "점수내림차순", "점수오름차순"]

    #generate range button frame
    range_button_frame = Frame(main_win).grid(row = 0, column = 0, columnspan = 10, sticky = N)

    for i in range(len(button_group)):
        buton = Button(range_button_frame, text = button_group[i], width = 10).grid(row = 9, column = i)

def gen_display(main_win):

    #generate display frame
    display_frame = Frame(main_win).grid(row = 0, column = 0, columnspan = 12, sticky = N)
    list_display = Text(display_frame, width = 45, height = 20, bg = "pink").grid(row = 10, column = 0)