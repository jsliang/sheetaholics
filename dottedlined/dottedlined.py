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
import gui
import os
import wx


# Implementing Sheetaholics_DottedLined
class SheetaholicsDottedLined( gui.Sheetaholics_DottedLined ):
    def __init__( self, parent ):
        gui.Sheetaholics_DottedLined.__init__( self, parent )

    # Handlers for Sheetaholics_DottedLined events.
    def btn_genpdfOnButtonClick( self, event ):
        config = {}
        config['gridSize'] =        float(self.tc_gridsize.GetValue())
        config['pageWidth'] =       float(self.tc_pagewidth.GetValue())
        config['pageHeight'] =      float(self.tc_pageheight.GetValue())
        config['marginInner'] =     float(self.tc_innermargin.GetValue())
        config['marginOuter'] =     float(self.tc_outermargin.GetValue())
        config['marginTop'] =       float(self.tc_topmargin.GetValue())
        config['marginBottom'] =    float(self.tc_bottommargin.GetValue())
        config['dotDiameter'] =     float(self.tc_dotdiameter.GetValue())
        config['dotColor'] =        self.clrpk_dotcolor.GetForegroundColour()
        config['lineWidth'] =       float(self.tc_linewidth.GetValue())
        config['lineColor'] =       self.clrpk_linecolor.GetForegroundColour()
        config['pageCount'] =       float(self.tc_pagecount.GetValue())
        
        dialog = wx.DirDialog(None, "Choose a directory to store the PDF file:", style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            pdf_filename = "dottedlinedsheets_%s.pdf" % datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
            pdf_filename = os.path.join(dialog.GetPath(), pdf_filename)
            generator.genpdf(pdf_filename, config)
            os.system(pdf_filename)
        dialog.Destroy()

class SheetaholicsMain(wx.App):
    def OnInit(self):
        self.m_frame = SheetaholicsDottedLined(None)
        self.m_frame.Show()
        return True

app = SheetaholicsMain(0)
app.MainLoop()
