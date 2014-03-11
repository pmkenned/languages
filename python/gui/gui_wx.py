#!/usr/bin/env python

import wx
 
class test(wx.App):
    def __init__(self):
        wx.App.__init__(self, redirect=False)
 
    def OnInit(self):
        frame = wx.Frame(None, -1,
                         "Test",
                         pos=(50,50), size=(100,40),
                         style=wx.DEFAULT_FRAME_STYLE)
        button = wx.Button(frame, -1, "Hello World!", (20, 20))
        self.frame = frame
        self.frame.Show()
        return True
 
if __name__ == '__main__':
        app = test()
        app.MainLoop()
