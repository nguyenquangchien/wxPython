#!/usr/bin/env python

import wx

class MenuEventFrame(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Menus', 
                         size=(300,200))
        menuBar = wx.MenuBar()
        menu1 = wx.Menu()
        menuItem = menu1.Append(-1, "&Exit...")
        menuBar.Append(menu1, "&File")
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.OnCloseMe, menuItem)

    def OnCloseMe(self, event):
        self.Close(True)

class App(wx.App):

    def __init__(self):
        wx.App.__init__(self)

    def OnInit(self):
        self.frame = MenuEventFrame(parent=None, id=-1)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True
    
    def OnExit(self):
        return
    

if __name__ == '__main__':
    app = App()
    app.MainLoop()