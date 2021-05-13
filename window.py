import wx
class Window(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, wx.ID_ANY, self.name, size = (200, 100))
        self.CreateStatusBar()
        self.panel = wx.Panel(self)

    def _go_to_window(self, window):
        self.Show(False)
        window.Show(True)

    def _dialog(self, title, message):
        dlg = wx.MessageDialog(self, message, title, wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
        return dlg
    def _edit(self, name, multiline=False, tpassword=False):
        wx.StaticText(self.panel, label=name)
        if multiline:
            return wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)
        elif tpassword:
            return wx.TextCtrl(self.panel, style=wx.TE_PASSWORD)
        else:
            return wx.TextCtrl(self.panel)

    def _checkbox(self, name):
        return wx.CheckBox(self.panel, -1, name)

    def OnExit(self, event):
        self.Close(True)
        if self.Parent:
            self.Parent.Show(True)
    def _button(self, name, function):
        b = wx.Button(self.panel, wx.ID_ANY, name)
        self.Bind(wx.EVT_BUTTON, function, b)
        return b

    def _radiobox(self, name, choices, function=None):
        c = wx.RadioBox(self.panel, wx.ID_ANY, label=name, choices=choices)
        if function:
            self.Bind(wx.EVT_RADIOBOX, function, c)
        return c

    def _combobox(self, name, choices, function=None):
        wx.StaticText(self.panel, wx.ID_ANY, label=name)
        c = wx.ComboBox(self.panel, wx.ID_ANY, choices=choices,
        value=choices[0], style=wx.CB_READONLY)
        if function:
            self.Bind(wx.EVT_COMBOBOX, function, c)
        return c

    def _name_and_value(self, name, value):
        l = wx.StaticText(self.panel, wx.ID_ANY, label=name)
        e = wx.TextCtrl(self.panel, wx.ID_ANY, value=value, style=wx.TE_READONLY)
        return (l, e)

    def _listbox(self, name, choices):
        l = wx.StaticText(self.panel, wx.ID_ANY, label=name)
        lst = wx.ListBox(self.panel, wx.ID_ANY, choices=choices)
        return (l, lst)
