import wx
import wx.lib.dialogs
import wx.stc as stc

faces={'times':'Times New Roman',
       'mono':'Courier New',
       'helv':'Arial',
       'other':'Comic Sans MS',
       'size':12,
       'size2':0,}

class MainWindow(wx.Frame):
    def __init__(self,parent,title):
        self.leftMarginWidth=30

        wx.Frame.__init__(self,parent,title=title, size=(800,600))
        self.control=stc.StyledTextCtrl(self,style=wx.TE_MULTILINE | wx.TE_WORDWRAP)
        self.control.CmdKeyAssign(ord('='), stc.STC_SCMOD_CTRL, stc.STC_CMD_ZOOMIN)
        self.control.CmdKeyAssign(ord('-'), stc.STC_SCMOD_CTRL, stc.STC_CMD_ZOOMOUT)
        self.control.CmdKeyAssign(ord('c'), stc.STC_SCMOD_CTRL, stc.STC_CMD_COPY)
        self.control.CmdKeyAssign(ord('v'), stc.STC_SCMOD_CTRL, stc.STC_CMD_PASTE)
        self.control.CmdKeyAssign(ord('z'), stc.STC_SCMOD_CTRL, stc.STC_CMD_UNDO)

        self.control.SetViewWhiteSpace(False)
        self.control.SetMargins(5,0)
        self.control.SetMarginType(1, stc.STC_MARGIN_NUMBER)
        self.control.SetMarginWidth(1,self.leftMarginWidth)

        self.CreateStatusBar()
        self.StatusBar.SetBackgroundColour((220,220,220))

        filemenu=wx.Menu()
        menuNew=filemenu.Append(wx.ID_NEW, "&New", "Create a new document")
        menuOpen=filemenu.Append(wx.ID_OPEN, "&Open", "Open an existing document")
        menuSave=filemenu.Append(wx.ID_SAVE,"&Save", "Save the current version")
        menuSaveAs=filemenu.Append(wx.ID_SAVEAS,"Save &As", "Save a new document")
        filemenu.AppendSeparator()
        menuClose=filemenu.Append(wx.ID_EXIT, "&Close", "Close the Application")

        editmenu=wx.Menu()
        menuUndo=editmenu.Append(wx.ID_UNDO, "&Undo", "Undo last action")
        menuRedo=editmenu.Append(wx.ID_REDO,"&Redo", "Redo last action")
        editmenu.AppendSeparator()
        menuSelectAll=editmenu.Append(wx.ID_SELECTALL, "&Select All", "Select the entire dcument")
        menuCopy=editmenu.Append(wx.ID_COPY, "&Copy", "Copy selected text")
        menuCut=editmenu.Append(wx.ID_CUT, "&Cut", "Cut selected text")
        menuPaste=editmenu.Append(wx.ID_PASTE, "&Paste", "Paste text from the clipboard")

        prefmenu=wx.Menu()
        menuLineNumbers=prefmenu.Append(wx.ID_ANY, "Toggle &Line Numbers", "Show/Hide line numbers column")

        helpmenu=wx.Menu()
        menuHowTo=helpmenu.Append(wx.ID_ANY, "&How To...", "Get help with the editor")
        helpmenu.AppendSeparator()
        menuAbout=helpmenu.Append(wx.ID_ABOUT, "&About the editor and it's creator")

        menuBar=wx.MenuBar()
        menuBar.Append(filemenu, "&File")
        menuBar.Append(editmenu, "&Edit")
        menuBar.Append(prefmenu, "&Preferences")
        menuBar.Append(helpmenu, "&Help")
        self.SetMenuBar(menuBar)

        self.Show()

app=wx.App()
frame= MainWindow(None, "HoqueEdit: Advanced Edition")
app.MainLoop()