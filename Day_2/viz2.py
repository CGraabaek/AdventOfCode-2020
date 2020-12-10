import curses
from curses.textpad import Textbox, rectangle
import re
import time

regex_pattern = r"([0-9]+)-([0-9]+) ([a-z]+): ([a-z]+)"



JMP, NOP, ACC = "JMP", "NOP", "ACC"
OP_COLOR = {}
OP_HIGHLIGHT = {}
OP_WINDOW_WIDTH = 30
INDEX_ACC_WINDOW_WIDTH = 27
VISITED_WINDOW_WIDTH = 5
DELAY = .05
CELL = " * "

with open("input.txt") as f:
    DATA = f.read()
DATA = [(password, int(max_limit)) for min_limit,max_limit,letter,password in re.findall(r"([0-9]+)-([0-9]+) ([a-z]+): ([a-z]+)", DATA)]

def compute():
    index = acc = 0
    seen = set()
    while True:
        password,max_limit = DATA[index]
        yield password,max_limit

        if index in seen or index == len(DATA) - 1:
            break
        seen.add(index)

        index += 1


def delayed(iter, delay=DELAY):
    for item in iter:
        yield item
        time.sleep(delay)

def init_scr(screen):
    screen.clear()
    screen.keypad(True)
    curses.cbreak()
    curses.noecho()
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_YELLOW, curses.COLOR_WHITE)
    curses.init_pair(8, curses.COLOR_CYAN, curses.COLOR_WHITE)
    curses.init_pair(9, curses.COLOR_RED, curses.COLOR_WHITE)
    screen.attron(curses.color_pair(1))
    OP_COLOR.update(JMP=curses.color_pair(4), NOP=curses.color_pair(6), ACC=curses.color_pair(5))
    OP_HIGHLIGHT.update(JMP=curses.color_pair(7), NOP=curses.color_pair(9), ACC=curses.color_pair(8))

def end_curses(screen):
    curses.nocbreak()
    screen.keypad(False)
    curses.echo()
    curses.flushinp()
    curses.endwin()


def setup_windows(screen):
    height, width = screen.getmaxyx()
    width -= 1

    # Message window
    rectangle(screen, 0, 0, 2, width - INDEX_ACC_WINDOW_WIDTH - 2 - 1)
    messages = curses.newwin(1, width - INDEX_ACC_WINDOW_WIDTH - 2 - 2, 1, 1)


    # Valid Password Counter and accumulator window
    rectangle(screen, 0, width - INDEX_ACC_WINDOW_WIDTH - 2, 2, width)
    screen.addstr(1, width - INDEX_ACC_WINDOW_WIDTH - 1, "ADDRESS:      | ACC:")
    addr = curses.newwin(1, 5, 1, width - INDEX_ACC_WINDOW_WIDTH - 1 + 9)
    addr.attron(curses.color_pair(3))
    acc = curses.newwin(1, 7, 1, width - INDEX_ACC_WINDOW_WIDTH - 1 + 9 + 4 + 8)
    acc.attron(curses.color_pair(2))

    # Op history window - LEFT WINDOW
    rectangle(screen, 3, 0, height - 3, OP_WINDOW_WIDTH + 2)
    op_out = curses.newwin(height - 3 - 2 - 2, OP_WINDOW_WIDTH, 4, 1)
    op_out.scrollok(True)


    # Visited window - RIGHT WINDONW
    rectangle(screen, 3, width - VISITED_WINDOW_WIDTH - 2, height - 3, width)
    visited = curses.newwin(height - 3 - 2 - 2, VISITED_WINDOW_WIDTH, 4, width - VISITED_WINDOW_WIDTH - 1)
    visited.attron(curses.color_pair(9))
    visited.scrollok(True)

    screen.refresh()
    

    return messages,addr,acc,op_out,visited


@curses.wrapper
def main(screen):
    init_scr(screen)
    message_win,addr_win, acc_win, op_out_win, visited_win = setup_windows(screen)

    def print_message(message, delay=DELAY, with_dots=False):
        """Print single-line messages to the message window"""
        message_win.clear()
        for i, letter in delayed(enumerate(message), delay):
            message_win.addstr(0, i, letter)
            message_win.refresh()

        if with_dots:
            return dots(len(message))
    
    def dots(offset):
        """Generator that animates the "..." in the message window."""
        while True:
            n = -round(2 * time.time()) % 4
            message_win.addstr(0, offset, "...   "[n: n + 3])
            message_win.noutrefresh()
            yield

    def update_ops(op, val):
        op_out_win.scroll()
        y, _ = op_out_win.getmaxyx()
        op_out_win.addstr(y - 1, 0, f"{op} {val:>10}")
        # op_out_win.chgat(y - 1, 0, 3, OP_COLOR[op])
        op_out_win.chgat(y - 1, 0, 3, curses.color_pair(4))
        op_out_win.noutrefresh()

    def update_visited(ind):
        visited_win.scroll()
        y, _ = visited_win.getmaxyx()
        visited_win.addstr(y - 1, 0, f"{ind:4}")
        visited_win.noutrefresh()

    def update_ind_acc(ind, acc):
        addr_win.addstr(0, 0, f"{ind:04}")
        addr_win.noutrefresh()
        acc_win.addstr(0, 0, f"{acc:06}")
        acc_win.noutrefresh()


    def visualize_computation(delay=DELAY):
        for password,max_limit in delayed(compute(), delay):
            update_ops(password, max_limit)
            update_ind_acc(12,max_limit)
            next(dotter)

            curses.doupdate()
        return ind
    
    # Start of program
    # highlighter = highlight(); next(highlighter)
    dotter = print_message("Processing Passwords", with_dots=True)
    ind = visualize_computation(.2)
