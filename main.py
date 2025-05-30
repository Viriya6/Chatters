import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle

def main(stdscr):
    stdscr.clear()
    stdscr.addstr("Hello, World!")

    stdscr.refresh()
    stdscr.getch()

wrapper(main)
