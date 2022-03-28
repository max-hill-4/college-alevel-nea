import pygame as py
import tools as tl
import config as cfg
import network as nt


class Wait:
    def __init__(self):
        self.done = False
        self.next_state = None
        self.button_back = tl.Button(cfg.button_back_image, 0, 0)

    def get_event(self, event):
        if event.type == py.QUIT:
            nt.del_lobby(cfg.lobby_id)
            cfg.lobby_created = None
            self.done = True

        if not cfg.lobby_id:
            print('creating game lobby')
            cfg.lobby_id = nt.lobby_code()
            nt.add_lobby(cfg.lobby_id)

        if nt.get_data(cfg.lobby_id)[0]:
            cfg.move = True
            self.next_state = "GAMEPLAY"

        if self.button_back.pressed(event):
            nt.del_lobby(cfg.lobby_id)
            cfg.lobby_created = None
            self.next_state = "LOBBY"

    def draw(self, window):

        window.blit(cfg.background_wait, (0, 0))
        self.button_back.draw(window)