# @author: ALI GHANBARI 
# @email: alighanbari446@gmail.com

from pynput import keyboard
import time
# import curses
# import scriptcontext
import msvcrt
import sys
# i = 0
# t = 0
#
# def on_release(key):
#     global i, t
#     if key == keyboard.Key.space:
#         while True:
#             i += 1
#             print(i)
#             if t == 1:
#                 break
#         return True
#
# def on_press(key):
#     global t
#     if key == keyboard.Key.esc:
#         t = 1
#         return False
#
# lis = keyboard.Listener(on_press=on_press, on_release=on_release)
# lis.start() # start to listen on a separate thread
# lis.join() # no this if main thread is polling self.keys


# def _start():
#     print("HelloWorld")
#     return True
#
# def on_press(key):
#     if key == keyboard.Key.esc:
#         # Stop listener
#         return False
#     else:
#         _start()
#
#
# # Collect events until released
# with keyboard.Listener(
#         on_press=on_press) as listener:
#     listener.join()

# stdscr = curses.initscr()
# while True:
#     key = stdscr.getch()
#     if key == 27: # This is the escape key code
#          curses.endwin()
#          break
# while True:
#     pressedKey = msvcrt.getch()
#     if pressedKey == 'q':
#        print("Q was pressed")
#     elif pressedKey == 'x':
#        sys.exit()
#     else:
#        print("Key Pressed:" + str(pressedKey))
while 1:
    print('Testing..')
    # body of the loop ...
    if msvcrt.kbhit() and msvcrt.getch()[0] == 28:
        break
