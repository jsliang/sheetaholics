#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import generator
import gui
import os
import wx

# Implementing Sheetaholics_Finished_Dialog
class Sheetaholics_Finished_Dialog( gui.Sheetaholics_Finished_Dialog ):
    def __init__( self, parent ):
        gui.Sheetaholics_Finished_Dialog.__init__( self, parent )

    # Handlers for Sheetaholics_Finished_Dialog events.
    def btn_okOnButtonClick( self, event ):
        self.Destroy()

# Implementing Sheetaholics_Main
class Sheetaholics_Main( gui.Sheetaholics_Main ):
    def __init__( self, parent ):
        gui.Sheetaholics_Main.__init__( self, parent )
        
        self.dp_output.SetPath(os.path.abspath(os.path.dirname(__file__)))
        
        self.tc_dotdiameter.Enable( self.cb_drawdots.GetValue() )
        self.clrpk_dotcolor.Enable( self.cb_drawdots.GetValue() )
        
        self.tc_linewidth.Enable( self.cb_drawlines.GetValue() )
        self.clrpk_linecolor.Enable( self.cb_drawlines.GetValue() )
        
        self.tc_pronheight.Enable( self.cb_drawpron.GetValue() )
    
    # Handlers for Sheetaholics_Main events.
    def cb_drawdotsOnCheckBox( self, event ):
        self.tc_dotdiameter.Enable( self.cb_drawdots.GetValue() )
        self.clrpk_dotcolor.Enable( self.cb_drawdots.GetValue() )
    
    def cb_drawlinesOnCheckBox( self, event ):
        self.tc_linewidth.Enable( self.cb_drawlines.GetValue() )
        self.clrpk_linecolor.Enable( self.cb_drawlines.GetValue() )
    
    def cb_drawpronOnCheckBox( self, event ):
        self.tc_pronheight.Enable( self.cb_drawpron.GetValue() )
    
    def btn_dottedlined_genpdfOnButtonClick( self, event ):
        config = {}
        config['gridSize'] =        float(self.tc_gridsize.GetValue())
        config['drawPron'] =        self.cb_drawpron.GetValue()
        config['pronHeight'] =      float(self.tc_pronheight.GetValue())
        config['pageWidth'] =       float(self.tc_pagewidth.GetValue())
        config['pageHeight'] =      float(self.tc_pageheight.GetValue())
        config['marginInner'] =     float(self.tc_innermargin.GetValue())
        config['marginOuter'] =     float(self.tc_outermargin.GetValue())
        config['marginTop'] =       float(self.tc_topmargin.GetValue())
        config['marginBottom'] =    float(self.tc_bottommargin.GetValue())
        config['drawdots'] =        self.cb_drawdots.GetValue()
        config['dotDiameter'] =     float(self.tc_dotdiameter.GetValue())
        config['dotColor'] =        self.clrpk_dotcolor.GetColour()
        config['drawlines'] =       self.cb_drawlines.GetValue()
        config['lineWidth'] =       float(self.tc_linewidth.GetValue())
        config['lineColor'] =       self.clrpk_linecolor.GetColour()
        config['pageCount'] =       float(self.sc_pagecount.GetValue())
        
        pdf_filename = "dottedlinedsheets_%s.pdf" % datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
        pdf_filename = os.path.join(self.dp_output.GetPath(), pdf_filename)
        generator.genpdf(pdf_filename, config)
        
        self.dialog = Sheetaholics_Finished_Dialog(self)
        self.dialog.tc_pdfpath.SetValue(pdf_filename)
        self.dialog.Show()

class SheetaholicsMain(wx.App):
    def OnInit(self):
        self.m_frame = Sheetaholics_Main(None)
        self.m_frame.Show()
        return True

app = SheetaholicsMain(0)
app.MainLoop()
