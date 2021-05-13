# -*- encoding: UTF-8 -*-
import calendar, datetime, time
import wx
import pylast
from window import Window
class Scrobblewindow(Window):
    name = "Aligascrobbler"

    def __init__(self, parent, network):
        Window.__init__(self, None)
        self.network=network
        self.artist= self._edit("Digite o artista")
        self.title= self._edit("Digite o nome da música")
        self.album= self._edit("Digite o álbum(opcional)")
        self.tmlist= self._combobox("", timescrobble)
        self.tmlist.Bind(wx.EVT_COMBOBOX, self.OnCombobox)
        self.tmlist.SetSelection(1)
        self.day=self._edit("Dia")
        self.day.Hide()
        self.hour=self._edit("Hora")
        self.hour.Hide()
        self.minute=self._edit("Minuto")
        self.minute.Hide()
        self._button("&Scrobble", self._do_scrobble)
        self._button("&Fechar", exit)

    def OnCombobox(self, event):
        if self.tmlist.GetSelection()==0:
            self.day.Show(True)
            self.hour.Show(True)
            self.minute.Show(True)
        else:
            self.day.Show(False)
            self.hour.Show(False)
            self.minute.Show(False)

    def _do_scrobble(self, event):
        now=datetime.datetime.now()
        if self.minute.GetValue() or self.hour.GetValue() or self.minute.GetValue():
            date= datetime.datetime(day=int(self.day.GetValue()), month=now.month, year=now.year, hour=int(self.hour.GetValue())+3, minute=int(self.minute.GetValue()),
second=20)
            tmscrobble=int( calendar.timegm(date.timetuple()))
        else:
            tmscrobble=int(time.time()-(self.tmlist.GetSelection()*60-60))

        if not self.artist.GetValue() or not self.title.GetValue():
            d = self._dialog('Aligascrobbler', 'Campos Artista e Nome da música precisam ser preenchidos.')
            return False
        try:
            self.network.scrobble(artist = self.artist.GetValue(), album = self.album.GetValue(), title = self.title.GetValue(), timestamp= tmscrobble)
            d = self._dialog('Aligascrobbler', 'Scrobble efetuado!')
        except pylast.ScrobbleError:
            d = self._dialog('Aligascrobbler', 'Scrobble falhou, tente novamente.')

timescrobble=[]
for i in range(0,301):
    if i==0:
        timescrobble.append("Agora mesmo")
    elif i ==1:
        timescrobble.append("%d minuto atrás" %i)
    elif i < 60:
        timescrobble.append("%d minutos atrás" %i)
    elif i >= 60:
        horas=i/60
        minutos= i % 60
        if minutos==0:
            if horas==1:
                timescrobble.append("%d hora atrás" %horas)
            else:
                timescrobble.append("%d horas atrás" %horas)
        elif minutos==1:
            if horas==1:
                timescrobble.append("%d hora e %d minuto atrás" %(horas, minutos))
            else:
                timescrobble.append("%d horas e %d minuto atrás" %(horas, minutos))
        elif horas==1 and minutos<60:
            timescrobble.append("%d hora e %d minutos atrás" %(horas, minutos))
        else:
            timescrobble.append("%d horas e %d minutos atrás" %(horas, minutos))
timescrobble.insert(0, "Data personalizada")
