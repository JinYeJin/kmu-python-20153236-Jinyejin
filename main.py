# -*- coidng: utf-8 -*-

import window
from tkinter import *

main_win = Tk()
main_win.title ("Project")

window.gen_entry(main_win)
window.gen_button(main_win)
window.gen_range_button(main_win)
window.gen_display(main_win)