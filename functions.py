import wx
a=wx.App()

def alert(title, text):
 wx.MessageBox(title, text)
def input_box(title, message):
  dlg=wx.TextEntryDialog(None, message, title)
  result=dlg.GetValue()
  dlg.Destroy()
  return result
