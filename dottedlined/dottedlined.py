#!/usr/bin/python
# -*- coding: utf-8 -*-

# Explicitly import reportlab.pdfbase._fontdata_*
# Uncomment these lines if you are running PyInstaller on Windows
# Reference:
#     http://www.python-forum.org/pythonforum/viewtopic.php?f=15&t=21922
"""
from reportlab.pdfbase import _fontdata_widths_courier
from reportlab.pdfbase import _fontdata_widths_courierbold
from reportlab.pdfbase import _fontdata_widths_courieroblique
from reportlab.pdfbase import _fontdata_widths_courierboldoblique
from reportlab.pdfbase import _fontdata_widths_helvetica
from reportlab.pdfbase import _fontdata_widths_helveticabold
from reportlab.pdfbase import _fontdata_widths_helveticaoblique
from reportlab.pdfbase import _fontdata_widths_helveticaboldoblique
from reportlab.pdfbase import _fontdata_widths_timesroman
from reportlab.pdfbase import _fontdata_widths_timesbold
from reportlab.pdfbase import _fontdata_widths_timesitalic
from reportlab.pdfbase import _fontdata_widths_timesbolditalic
from reportlab.pdfbase import _fontdata_widths_symbol
from reportlab.pdfbase import _fontdata_widths_zapfdingbats
from reportlab.pdfbase import _fontdata_enc_winansi
from reportlab.pdfbase import _fontdata_enc_macroman
from reportlab.pdfbase import _fontdata_enc_standard
from reportlab.pdfbase import _fontdata_enc_symbol
from reportlab.pdfbase import _fontdata_enc_zapfdingbats
from reportlab.pdfbase import _fontdata_enc_pdfdoc
from reportlab.pdfbase import _fontdata_enc_macexpert
"""

import datetime
import generator
import os
import wx

class DottedLinedForm(wx.Frame):
    def __init__(self, parent, title):
        super(DottedLinedForm, self).__init__(parent, title=title, size=(300, 550))
        
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
        sizer.Add(self.tc_gridsize, pos=(dot_line_row, dot_line_col + 1), flag=wx.EXPAND|wx.LEFT, border=spacing)
        sizer.Add(wx.StaticText(panel, label="mm"), pos=(dot_line_row, dot_line_col + 2), flag=wx.ALIGN_RIGHT|wx.TOP|wx.RIGHT, border=spacing)
        dot_line_row += 1
        
        self.btn_dotcolor = wx.Button(panel, label="Select Color")
        self.btn_dotcolor.Bind(wx.EVT_BUTTON, self.on_btn_dotcolor)
        txt_dotcolor = wx.StaticText(panel, label="Dot Color:")
        sizer.Add(txt_dotcolor, pos=(dot_line_row, dot_line_col + 0), flag=wx.ALIGN_RIGHT|wx.TOP|wx.LEFT, border=spacing)
        sizer.Add(self.btn_dotcolor, pos=(dot_line_row, dot_line_col + 1), span=(1, 2), flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=spacing)
        dot_line_row += 1
        
        txt_dotdiameter = wx.StaticText(panel, label="Dot Diameter:")
        self.tc_dotdiameter = wx.TextCtrl(panel, value="0.4")
        sizer.Add(txt_dotdiameter, pos=(dot_line_row, dot_line_col + 0), flag=wx.ALIGN_RIGHT|wx.TOP|wx.LEFT, border=spacing)
        sizer.Add(self.tc_dotdiameter, pos=(dot_line_row, dot_line_col + 1), flag=wx.EXPAND|wx.LEFT, border=spacing)
        sizer.Add(wx.StaticText(panel, label="mm"), pos=(dot_line_row, dot_line_col + 2), flag=wx.ALIGN_RIGHT|wx.TOP|wx.RIGHT, border=spacing)
        dot_line_row += 1
        
        self.btn_linecolor = wx.Button(panel, label="Select Color")
        self.btn_linecolor.Bind(wx.EVT_BUTTON, self.on_btn_linecolor)
        txt_linecolor = wx.StaticText(panel, label="Line Color:")
        sizer.Add(txt_linecolor, pos=(dot_line_row, dot_line_col + 0), flag=wx.ALIGN_RIGHT|wx.TOP|wx.LEFT, border=spacing)
        sizer.Add(self.btn_linecolor, pos=(dot_line_row, dot_line_col + 1), span=(1, 2), flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=spacing)
        dot_line_row += 1
        
        txt_linewidth = wx.StaticText(panel, label="Line Width:")
        self.tc_linewidth = wx.TextCtrl(panel, value="0.2")
        sizer.Add(txt_linewidth, pos=(dot_line_row, dot_line_col + 0), flag=wx.ALIGN_RIGHT|wx.TOP|wx.LEFT, border=spacing)
        sizer.Add(self.tc_linewidth, pos=(dot_line_row, dot_line_col + 1), flag=wx.EXPAND|wx.LEFT, border=spacing)
        sizer.Add(wx.StaticText(panel, label="mm"), pos=(dot_line_row, dot_line_col + 2), flag=wx.ALIGN_RIGHT|wx.TOP|wx.RIGHT, border=spacing)
        dot_line_row += 1
        
        margin_row = dot_line_row
        margin_col = 0
        
        txt_margin = wx.StaticText(panel, label="Margin")
        sizer.Add(txt_margin, pos=(margin_row, margin_col + 0), span=(1, 3), flag=wx.ALIGN_CENTER|wx.TOP|wx.LEFT, border=spacing)
        margin_row += 1
        
        txt_innermargin = wx.StaticText(panel, label="Inner Margin:")
        self.tc_innermargin = wx.TextCtrl(panel, value="20")
        sizer.Add(txt_innermargin, pos=(margin_row, margin_col + 0), flag=wx.ALIGN_RIGHT|wx.TOP|wx.LEFT, border=spacing)
        sizer.Add(self.tc_innermargin, pos=(margin_row, margin_col + 1), flag=wx.EXPAND|wx.LEFT, border=spacing)
        sizer.Add(wx.StaticText(panel, label="mm"), pos=(margin_row, margin_col + 2), flag=wx.ALIGN_RIGHT|wx.TOP|wx.RIGHT, border=spacing)
        margin_row += 1
        
        txt_outermargin = wx.StaticText(panel, label="Outer Margin:")
        self.tc_outermargin = wx.TextCtrl(panel, value="15")
        sizer.Add(txt_outermargin, pos=(margin_row, margin_col + 0), flag=wx.ALIGN_RIGHT|wx.TOP|wx.LEFT, border=spacing)
        sizer.Add(self.tc_outermargin, pos=(margin_row, margin_col + 1), flag=wx.EXPAND|wx.LEFT, border=spacing)
        sizer.Add(wx.StaticText(panel, label="mm"), pos=(margin_row, margin_col + 2), flag=wx.ALIGN_RIGHT|wx.TOP|wx.RIGHT, border=spacing)
        margin_row += 1
        
        txt_topmargin = wx.StaticText(panel, label="Top Margin:")
        self.tc_topmargin = wx.TextCtrl(panel, value="15")
        sizer.Add(txt_topmargin, pos=(margin_row, margin_col + 0), flag=wx.ALIGN_RIGHT|wx.TOP|wx.LEFT, border=spacing)
        sizer.Add(self.tc_topmargin, pos=(margin_row, margin_col + 1), flag=wx.EXPAND|wx.LEFT, border=spacing)
        sizer.Add(wx.StaticText(panel, label="mm"), pos=(margin_row, margin_col + 2), flag=wx.ALIGN_RIGHT|wx.TOP|wx.RIGHT, border=spacing)
        margin_row += 1
        
        txt_bottommargin = wx.StaticText(panel, label="Bottom  Margin:")
        self.tc_bottommargin = wx.TextCtrl(panel, value="15")
        sizer.Add(txt_bottommargin, pos=(margin_row, margin_col + 0), flag=wx.ALIGN_RIGHT|wx.TOP|wx.LEFT, border=spacing)
        sizer.Add(self.tc_bottommargin, pos=(margin_row, margin_col + 1), flag=wx.EXPAND|wx.LEFT, border=spacing)
        sizer.Add(wx.StaticText(panel, label="mm"), pos=(margin_row, margin_col + 2), flag=wx.ALIGN_RIGHT|wx.TOP|wx.RIGHT, border=spacing)
        margin_row += 1
        
        papersize_row = margin_row
        papersize_col = margin_col
        
        txt_papersize = wx.StaticText(panel, label="Paper Size")
        sizer.Add(txt_papersize, pos=(papersize_row, papersize_col + 0), span=(1, 3), flag=wx.ALIGN_CENTER|wx.TOP|wx.LEFT, border=spacing)
        papersize_row += 1
        
        txt_pagewidth = wx.StaticText(panel, label="Page Width:")
        self.tc_pagewidth = wx.TextCtrl(panel, value="210")
        sizer.Add(txt_pagewidth, pos=(papersize_row, papersize_col + 0), flag=wx.ALIGN_RIGHT|wx.TOP|wx.LEFT, border=spacing)
        sizer.Add(self.tc_pagewidth, pos=(papersize_row, papersize_col + 1), flag=wx.EXPAND|wx.LEFT, border=spacing)
        sizer.Add(wx.StaticText(panel, label="mm"), pos=(papersize_row, papersize_col + 2), flag=wx.ALIGN_RIGHT|wx.RIGHT, border=spacing)
        papersize_row += 1
        
        txt_pageheight = wx.StaticText(panel, label="Page Height:")
        self.tc_pageheight = wx.TextCtrl(panel, value="297")
        sizer.Add(txt_pageheight, pos=(papersize_row, papersize_col + 0), flag=wx.ALIGN_RIGHT|wx.TOP|wx.LEFT, border=spacing)
        sizer.Add(self.tc_pageheight, pos=(papersize_row, papersize_col + 1), flag=wx.EXPAND|wx.LEFT, border=spacing)
        sizer.Add(wx.StaticText(panel, label="mm"), pos=(papersize_row, papersize_col + 2), flag=wx.ALIGN_RIGHT|wx.RIGHT, border=spacing)
        papersize_row += 1
        
        pagecount_row = papersize_row
        pagecount_col = dot_line_col
        
        txt_pagecount_title = wx.StaticText(panel, label="Number of Pages")
        sizer.Add(txt_pagecount_title, pos=(pagecount_row, pagecount_col + 0), span=(1, 3), flag=wx.ALIGN_CENTER|wx.TOP|wx.LEFT, border=spacing)
        pagecount_row += 1
        
        txt_pagecount = wx.StaticText(panel, label="Number of Pages:")
        self.tc_pagecount = wx.TextCtrl(panel, value="2")
        sizer.Add(txt_pagecount, pos=(pagecount_row, pagecount_col + 0), flag=wx.ALIGN_RIGHT|wx.TOP|wx.LEFT, border=spacing)
        sizer.Add(self.tc_pagecount, pos=(pagecount_row, pagecount_col + 1), span=(1,2), flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=spacing)
        pagecount_row += 1
        
        btn_genpdf = wx.Button(panel, label="Generate PDF")
        sizer.Add(btn_genpdf, pos=(pagecount_row, pagecount_col + 0), span=(1, 3), flag=wx.ALIGN_CENTER|wx.TOP|wx.LEFT|wx.RIGHT|wx.BOTTOM, border=spacing)
        btn_genpdf.Bind(wx.EVT_BUTTON, self.GeneratePDF)
        pagecount_row += 1
        
        sizer.AddGrowableCol(1)
        sizer.AddGrowableCol(5)
        panel.SetSizerAndFit(sizer)
    
    def on_btn_linecolor(self, event):
        dialog = wx.ColourDialog(None)
        dialog.GetColourData().SetChooseFull(True)
        if dialog.ShowModal() == wx.ID_OK:
            data = dialog.GetColourData()
            self.btn_linecolor.SetForegroundColour(data.GetColour())
        dialog.Destroy()
    
    def on_btn_dotcolor(self, event):
        dialog = wx.ColourDialog(None)
        dialog.GetColourData().SetChooseFull(True)
        if dialog.ShowModal() == wx.ID_OK:
            data = dialog.GetColourData()
            self.btn_dotcolor.SetForegroundColour(data.GetColour())
        dialog.Destroy()
    
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
        config['dotColor'] =        self.btn_dotcolor.GetForegroundColour()
        config['lineWidth'] =       float(self.tc_linewidth.GetValue())
        config['lineColor'] =       self.btn_linecolor.GetForegroundColour()
        config['pageCount'] =       float(self.tc_pagecount.GetValue())
        
        dialog = wx.DirDialog(None, "Choose a directory to store the PDF file:", style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            pdf_filename = "dottedlinedsheets_%s.pdf" % datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
            pdf_filename = os.path.join(dialog.GetPath(), pdf_filename)
            generator.genpdf(pdf_filename, config)
            os.system(pdf_filename)
        dialog.Destroy()

if __name__ == '__main__':
    app = wx.App()
    DottedLinedForm(None, title='Dotted Lined Sheet Generator')
    app.MainLoop()

