#-*- encoding: UTF-8 -*-

import wx
import os
import pylast
import time
from sys import exit
from window import Window
from scrobble import Scrobblewindow
class Mainmenu(Window):
    name = "Aligascrobbler login"

    def __init__(self):
        Window.__init__(self, None)
        self.username= self._edit("Digite seu nome de usuário")
        self.password_shown= False
        self.text_password= self._edit("Digite sua senha", tpassword=True)
        if os.path.isfile("login.cfg"):
            with open("login.cfg", 'r') as arq:
                try:
                    line=arq.readline().split()
                    self.username.SetValue(line[0])
                    self.text_password.SetValue(line[1])
                except:
                    pass
        self.text_no_password=self._edit("Digite sua senha")
        self.text_no_password.Hide()
        self.checkbox= self._checkbox("Mostrar senha")
        self.checkbox.Bind(wx.EVT_CHECKBOX,self.OnCheckbox)
        self.login=self._button("&Login", self._login)
        self._button("&Fechar", self.OnExit)

    def OnCheckbox(self,event):
        self.text_password.Show(self.password_shown)
        self.text_no_password.Show(not self.password_shown)
        if not self.password_shown:
            self.text_no_password.SetValue(self.text_password.GetValue())
        else:
            self.text_password.SetValue(self.text_no_password.GetValue())
        self.password_shown= not self.password_shown

    def _login(self, event):
        API_KEY = "807622a0671955af069162490915e5f3"
        API_SECRET ="a2ac4c1f40bd04c1062ce367787b3b93"
        if self.text_no_password.GetValue():
            self.text_password.SetValue(self.text_no_password.GetValue())
        if not self.username.GetValue() or not self.text_password.GetValue():
            d= self._dialog('Aligascrobbler', '''Campos de usuário ou senha
estão em branco. Aligascrobbler fica bravo e é claro que fecha.''')
            exit(1)
        try:
            network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET, username = self.username.GetValue(), password_hash = pylast.md5(self.text_password.GetValue()
))
            self._go_to_window(Scrobblewindow(self, network=network))
        except pylast.WSError:
            w = self._dialog('Aligascrobbler', 'Usuário ou senha incorreta, Tente novamente.')

if __name__ == "__main__":
    import __builtin__
    a = wx.App(False)
    __builtin__.application = a
    w = Mainmenu()
w.Show(True)
a.MainLoop()
