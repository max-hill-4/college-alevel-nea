import pygame as py

py.init()

# Window size.
width, height = 640, 480

socket_object = None

# Pygame creates  hidden surface ready to be shown on screen.
button_login_image = py.image.load("resources/button_login_image.png")

button_create_image = py.image.load("resources/button_create_image.png")
button_quit_image = py.image.load("resources/button_quit_image.png")
button_back_image = py.image.load("resources/button_back_image.png")
button_confirm_image = py.image.load("resources/button_confirm_image.png")

text_box_image = py.image.load("resources/text_box_image.png")
text_box_image_selected = py.image.load("resources/text_box_image_outline.png")

background_title = py.image.load("resources/background_title.png")
background_login = py.image.load("resources/background_login.png")
background_lobby = py.image.load("resources/background_lobby.png")
background_wait = py.image.load("resources/background_wait.png")
background_gameplay = py.image.load("resources/background_gameplay.png")
# Button size.
caption = "Noughts and Crosses"
font = py.font.Font(None, 32)
