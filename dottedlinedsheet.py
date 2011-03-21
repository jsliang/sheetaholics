#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import generator
import os
import wx

class DottedLinedForm(wx.Frame):
    def __init__(self, parent, title):
        super(DottedLinedForm, self).__init__(parent, title=title, size=(512, 350))
        
        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        spacing = 5
        
        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(spacing, spacing)
        
        dot_line_row = 0
        dot_line_col = 0
        
        txt_dotline = wx.StaticText(panel, label="Dot and Line")
        sizer.Add(txt_dotline, pos=(dot_line_row, dot_line_col + 0), span=(1, 3), flag=wx.ALIGN_CENTER|wx.TOP|wx.LEFT, border=spacing)
        dot_line_row += 1
        
        txt_gridsize = wx.StaticText(panel, label="Grid Size:")
        self.tc_gridsize = wx.TextCtrl(panel, value="8")
        sizer.Add(txt_gridsize, pos=(dot_line_row, dot_line_col + 0), flag=wx.ALIGN_RIGHT|wx.TOP|wx.LEFT, border=spacing)
        sizer.Add(self.tc_gridsize, pos=(dot_line_row, dot_line_col + 1), flag=wx.EXPAND|wx.TOP|wx.LEFT, border=spacing)
        sizer.Add(wx.StaticText(panel, label="mm"), pos=(dot_line_row, dot_line_col + 2), flag=wx.ALIGN_RIGHT|wx.TOP|wx.LEFT|wx.BOTTOM, border=spacing)
        dot_line_row += 1
        
        txt_dotcolor = wx.StaticText(panel, label="Dot Color:")
        self.tc_dotcolor = wx.TextCtrl(panel, value="#000000")
        sizer.Add(txt_dotcolor, pos=(dot_line_row, dot_line_col + 0), flag=wx.ALIGN_RIGHT|wx.TOP|wx.LEFT, border=spacing)
        sizer.Add(self.tc_dotcolor, pos=(dot_line_row, dot_line_col + 1), span=(1, 2), flag=wx.EXPAND|wx.TOP|wx.LEFT, border=spacing)
        dot_line_row += 1
        
        txt_dotdiameter = wx.StaticText(panel, label="Dot Diameter:")
        self.tc_dotdiameter = wx.TextCtrl(panel, value="0.4")
        sizer.Add(txt_dotdiameter, pos=(dot_line_row, dot_line_col + 0), flag=wx.ALIGN_RIGHT|wx.TOP|wx.LEFT, border=spacing)
        sizer.Add(self.tc_dotdiameter, pos=(dot_line_row, dot_line_col + 1), flag=wx.EXPAND|wx.TOP|wx.LEFT, border=spacing)
        sizer.Add(wx.StaticText(panel, label="mm"), pos=(dot_line_row, dot_line_col + 2), flag=wx.ALIGN_RIGHT|wx.TOP|wx.LEFT, border=spacing)
        dot_line_row += 1
        
        txt_linecolor = wx.StaticText(panel, label="Line Color:")
        self.tc_linecolor = wx.TextCtrl(panel, value="#000000")
        sizer.Add(txt_linecolor, pos=(dot_line_row, dot_line_col + 0), flag=wx.ALIGN_RIGHT|wx.TOP|wx.LEFT, border=spacing)
        sizer.Add(self.tc_linecolor, pos=(dot_line_row, dot_line_col + 1), span=(1, 2), flag=wx.EXPAND|wx.TOP|wx.LEFT, border=spacing)
        dot_line_row += 1
        
        txt_linewidth = wx.StaticText(panel, label="Line Width:")
        self.tc_linewidth = wx.TextCtrl(panel, value="0.2")
        sizer.Add(txt_linewidth, pos=(dot_line_row, dot_line_col + 0), flag=wx.ALIGN_RIGHT|wx.TOP|wx.LEFT, border=spacing)
        sizer.Add(self.tc_linewidth, pos=(dot_line_row, dot_line_col + 1), flag=wx.EXPAND|wx.TOP|wx.LEFT, border=spacing)
        sizer.Add(wx.StaticText(panel, label="mm"), pos=(dot_line_row, dot_line_col + 2), flag=wx.ALIGN_RIGHT|wx.TOP|wx.LEFT, border=spacing)
        dot_line_row += 1
        
        margin_row = 0
        margin_col = 4
        
        txt_margin = wx.StaticText(panel, label="Margin")
        sizer.Add(txt_margin, pos=(margin_row, margin_col + 0), span=(1, 3), flag=wx.ALIGN_CENTER|wx.TOP|wx.LEFT, border=spacing)
        margin_row += 1
        
        txt_innermargin = wx.StaticText(panel, label="Inner Margin:")
        self.tc_innermargin = wx.TextCtrl(panel, value="20")
        sizer.Add(txt_innermargin, pos=(margin_row, margin_col + 0), flag=wx.ALIGN_RIGHT|wx.TOP|wx.LEFT, border=spacing)
        sizer.Add(self.tc_innermargin, pos=(margin_row, margin_col + 1), flag=wx.EXPAND|wx.TOP|wx.LEFT, border=spacing)
        sizer.Add(wx.StaticText(panel, label="mm"), pos=(margin_row, margin_col + 2), flag=wx.ALIGN_RIGHT|wx.TOP|wx.RIGHT|wx.BOTTOM, border=spacing)
        margin_row += 1
        
        txt_outermargin = wx.StaticText(panel, label="Outer Margin:")
        self.tc_outermargin = wx.TextCtrl(panel, value="15")
        sizer.Add(txt_outermargin, pos=(margin_row, margin_col + 0), flag=wx.ALIGN_RIGHT|wx.TOP|wx.LEFT, border=spacing)
        sizer.Add(self.tc_outermargin, pos=(margin_row, margin_col + 1), flag=wx.EXPAND|wx.TOP|wx.LEFT, border=spacing)
        sizer.Add(wx.StaticText(panel, label="mm"), pos=(margin_row, margin_col + 2), flag=wx.ALIGN_RIGHT|wx.TOP|wx.RIGHT|wx.BOTTOM, border=spacing)
        margin_row += 1
        
        txt_topmargin = wx.StaticText(panel, label="Top Margin:")
        self.tc_topmargin = wx.TextCtrl(panel, value="15")
        sizer.Add(txt_topmargin, pos=(margin_row, margin_col + 0), flag=wx.ALIGN_RIGHT|wx.TOP|wx.LEFT, border=spacing)
        sizer.Add(self.tc_topmargin, pos=(margin_row, margin_col + 1), flag=wx.EXPAND|wx.TOP|wx.LEFT, border=spacing)
        sizer.Add(wx.StaticText(panel, label="mm"), pos=(margin_row, margin_col + 2), flag=wx.ALIGN_RIGHT|wx.TOP|wx.RIGHT|wx.BOTTOM, border=spacing)
        margin_row += 1
        
        txt_bottommargin = wx.StaticText(panel, label="Bottom  Margin:")
        self.tc_bottommargin = wx.TextCtrl(panel, value="15")
        sizer.Add(txt_bottommargin, pos=(margin_row, margin_col + 0), flag=wx.ALIGN_RIGHT|wx.TOP|wx.LEFT, border=spacing)
        sizer.Add(self.tc_bottommargin, pos=(margin_row, margin_col + 1), flag=wx.EXPAND|wx.TOP|wx.LEFT, border=spacing)
        sizer.Add(wx.StaticText(panel, label="mm"), pos=(margin_row, margin_col + 2), flag=wx.ALIGN_RIGHT|wx.TOP|wx.RIGHT|wx.BOTTOM, border=spacing)
        margin_row += 1
        
        papersize_row = margin_row
        papersize_col = margin_col
        
        txt_papersize = wx.StaticText(panel, label="Paper Size")
        sizer.Add(txt_papersize, pos=(papersize_row, papersize_col + 0), span=(1, 3), flag=wx.ALIGN_CENTER|wx.TOP|wx.LEFT, border=spacing)
        papersize_row += 1
        
        txt_pagewidth = wx.StaticText(panel, label="Page Width:")
        self.tc_pagewidth = wx.TextCtrl(panel, value="210")
        sizer.Add(txt_pagewidth, pos=(papersize_row, papersize_col + 0), flag=wx.ALIGN_RIGHT|wx.TOP|wx.LEFT, border=spacing)
        sizer.Add(self.tc_pagewidth, pos=(papersize_row, papersize_col + 1), flag=wx.EXPAND|wx.TOP|wx.LEFT, border=spacing)
        sizer.Add(wx.StaticText(panel, label="mm"), pos=(papersize_row, papersize_col + 2), flag=wx.ALIGN_RIGHT|wx.TOP|wx.RIGHT|wx.BOTTOM, border=spacing)
        papersize_row += 1
        
        txt_pageheight = wx.StaticText(panel, label="Page Height:")
        self.tc_pageheight = wx.TextCtrl(panel, value="297")
        sizer.Add(txt_pageheight, pos=(papersize_row, papersize_col + 0), flag=wx.ALIGN_RIGHT|wx.TOP|wx.LEFT, border=spacing)
        sizer.Add(self.tc_pageheight, pos=(papersize_row, papersize_col + 1), flag=wx.EXPAND|wx.TOP|wx.LEFT, border=spacing)
        sizer.Add(wx.StaticText(panel, label="mm"), pos=(papersize_row, papersize_col + 2), flag=wx.ALIGN_RIGHT|wx.TOP|wx.RIGHT|wx.BOTTOM, border=spacing)
        papersize_row += 1
        
        pagecount_row = dot_line_row
        pagecount_col = dot_line_col
        
        txt_pagecount_title = wx.StaticText(panel, label="Number of Pages")
        sizer.Add(txt_pagecount_title, pos=(pagecount_row, pagecount_col + 0), span=(1, 3), flag=wx.ALIGN_CENTER|wx.TOP|wx.LEFT, border=spacing)
        pagecount_row += 1
        
        txt_pagecount = wx.StaticText(panel, label="Number of Pages:")
        self.tc_pagecount = wx.TextCtrl(panel, value="2")
        sizer.Add(txt_pagecount, pos=(pagecount_row, pagecount_col + 0), flag=wx.ALIGN_RIGHT|wx.TOP|wx.LEFT, border=spacing)
        sizer.Add(self.tc_pagecount, pos=(pagecount_row, pagecount_col + 1), flag=wx.EXPAND|wx.TOP|wx.LEFT, border=spacing)
        sizer.Add(wx.StaticText(panel, label="mm"), pos=(pagecount_row, pagecount_col + 2), flag=wx.ALIGN_RIGHT|wx.TOP|wx.RIGHT|wx.BOTTOM, border=spacing)
        pagecount_row += 1
        
        btn_genpdf = wx.Button(panel, label="Generate PDF")
        sizer.Add(btn_genpdf, pos=(pagecount_row, 2), span=(1, 3), flag=wx.ALIGN_CENTER, border=spacing)
        btn_genpdf.Bind(wx.EVT_BUTTON, self.GeneratePDF)
        pagecount_row += 1
        
        sizer.AddGrowableCol(1)
        sizer.AddGrowableCol(5)
        panel.SetSizerAndFit(sizer)

    def GeneratePDF(self, event):
        config = {}
        config['gridSize'] =        float(self.tc_gridsize.GetValue())
        config['pageWidth'] =       float(self.tc_pagewidth.GetValue())
        config['pageHeight'] =      float(self.tc_pageheight.GetValue())
        config['marginInner'] =     float(self.tc_innermargin.GetValue())
        config['marginOuter'] =     float(self.tc_outermargin.GetValue())
        config['marginTop'] =       float(self.tc_topmargin.GetValue())
        config['marginBottom'] =    float(self.tc_bottommargin.GetValue())
        config['dotDiameter'] =     float(self.tc_dotdiameter.GetValue())
        config['dotColor'] =        self.tc_dotcolor.GetValue()
        config['lineWidth'] =       float(self.tc_linewidth.GetValue())
        config['lineColor'] =       self.tc_linecolor.GetValue()
        config['pageCount'] =       float(self.tc_pagecount.GetValue())
        
        dialog = wx.DirDialog(None, "Choose a directory to store the PDF file:", style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            pdf_filename = "dottedlinedsheets_%s.pdf" % datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
            pdf_filename = os.path.join(dialog.GetPath(), pdf_filename)
            f = open(pdf_filename, 'w')
            f.write(generator.get_pdf_content(config))
            f.close()
            os.system(pdf_filename)
        dialog.Destroy()

if __name__ == '__main__':
    app = wx.App()
    DottedLinedForm(None, title='Dotted Lined Sheet Generator')
    app.MainLoop()

