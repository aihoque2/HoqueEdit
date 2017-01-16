import wx
import wx.lib
import wx.stc as stc
import os

faces={'times':'Times New Roman',
       'mono':'Courier New',
       'helv':'Arial',
       'other':'Comic Sans MS',
       'size':12,
       'size2':0,}

class MainWindow(wx.Frame):
    def __init__(self,parent,title):
        self.leftMarginWidth=30
        self.dirname= ''
        self.dilename= ''
        self.leftMarginWidth=25
        self.lineNumbersEnabled=True

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

        #part 3 here
        self.Bind(wx.EVT_MENU, self.OnNew, menuNew)
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnSave, menuSave)
        self.Bind(wx.EVT_MENU, self.OnSaveAs, menuSaveAs)
        self.Bind(wx.EVT_MENU, self.OnClose, menuClose)

        self.Bind(wx.EVT_MENU, self.OnUndo, menuUndo)
        self.Bind(wx.EVT_MENU, self.OnRedo, menuRedo)
        self.Bind(wx.EVT_MENU, self.OnSelectAll, menuSelectAll)
        self.Bind(wx.EVT_MENU, self.OnCopy, menuCopy)
        self.Bind(wx.EVT_MENU, self.OnCut, menuCut)
        self.Bind(wx.EVT_MENU, self.OnPaste, menuPaste)

        self.Bind(wx.EVT_MENU, self.OnTOggleLineNumbers, menuLineNumbers)

        self.Bind(wx.EVT_MENU, self.OnHowTo, menuHowTo)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)

        self.Show()

    def OnNew(self, e):
        self.filename=''
        self.control.SetValue("")

    def OnOpen(self,e):
        try:
            dlg=wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.FD_OPEN)
            if(dlg.ShowModal()==wx.ID_OK):
                self.filename=dlg.GetFilename()
                self.dirname=dlg.GetDirectory()
                f=open(os.path.join(self.dirname, self.filename), 'r')
                self.control.setValue(f.read())
                f.close()
            dlg.Destroy()
        except:
            dlg=wx.MessageDialog(self, "Couldn't open file","Error",wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
    def OnSave(self, e):
        try:
            f=open(os.path.join(self.dirname, self.filename), 'w')
            f.write(self.control.GEtValue())
            f.close()
        except:
            try:
                dlg= wx.FIleDialog(self,"Save file as", self.dirname, "Untitled", "*.*", wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
                if (dlg.ShowModal()==wx.ID_OK):
                    self.filename=dlg.GetFilename()
                    self.dirname=dlg.getDirectory()
                    f=open(os.path.join(self.dirname,self.filename), 'w')
                    f.write(self.control.GetValue())
                    f.close()
                dlg.Destroy()
            except:
                pass
    def OnSaveAs(selfself, e):
        try:
            f=open(os.path.join(self.dirname, self.filename), 'w')
            f.write(self.control.GEtValue())
            f.close()
        except:
            try:
                dlg= wx.FIleDialog(self,"Save file as", self.dirname, "Untitled", "*.*", wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
                if (dlg.ShowModal()==wx.ID_OK):
                    self.filename=dlg.GetFilename()
                    self.dirname=dlg.getDirectory()
                    f=open(os.path.join(self.dirname,self.filename), 'w')
                    f.write(self.control.GetValue())
                    f.close()
                dlg.Destroy()
            except:
                pass
    def OnClose(self, e):
        self.Close(True)

    def OnUndo(self, e):
        self.control.Undo()

    def OnRedo(self, e):
        self.control.Redo()

    def OnSelectAll(self, e):
        self.control.SelectAll()
    def OnCopy(self,e):
        self.control.Copy()
    def OnCut(self, e):
        self.control.cut()
    def OnPaste(self, e):
        self.control.Paste()
    def OnTOggleLineNumbers(self, e):
        if (self.lineNumbersEnabled):
            self.control.SetMarginWidth(1, 0)
            self.linenumbersEnabled= False
        else:
            self.control.SetMarginWidth(1, self.leftMarginWidth)
            self.lineNumbersEnabled=True

    def OnHowto(self, e):
        dlg=wx.lib.dialogs.ScrolledMessageDialong(self, "THis is how to.",size=(400,400))
        dlg.ShowModal()
        dlg.Destroy()

    def OnAbout(self, e):
        dlg=wx.MessageDialog(self, "My advanced text editor I made with python and wx",wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

app=wx.App()
frame= MainWindow(None, "HoqueEdit: Advanced Edition")
app.MainLoop()