# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

###########################################################################
## Class Sheetaholics_DottedLined
###########################################################################

class Sheetaholics_DottedLined ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Sheetaholics: Dotted Lined Sheet", pos = wx.DefaultPosition, size = wx.Size( 300,550 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer = wx.BoxSizer( wx.VERTICAL )
		
		gbSizer = wx.GridBagSizer( 5, 5 )
		gbSizer.SetFlexibleDirection( wx.BOTH )
		gbSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.txt_dotnline = wx.StaticText( self, wx.ID_ANY, u"Dot and Line", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_dotnline.Wrap( -1 )
		gbSizer.Add( self.txt_dotnline, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 3 ), wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.txt_gridsize = wx.StaticText( self, wx.ID_ANY, u"Grid Size:", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_gridsize.Wrap( -1 )
		gbSizer.Add( self.txt_gridsize, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.txt_mm_0 = wx.StaticText( self, wx.ID_ANY, u"mm", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_mm_0.Wrap( -1 )
		gbSizer.Add( self.txt_mm_0, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.txt_dotcolor = wx.StaticText( self, wx.ID_ANY, u"Dot Color:", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_dotcolor.Wrap( -1 )
		gbSizer.Add( self.txt_dotcolor, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.clrpk_dotcolor = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		gbSizer.Add( self.clrpk_dotcolor, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 2 ), wx.EXPAND, 5 )
		
		self.tc_gridsize = wx.TextCtrl( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer.Add( self.tc_gridsize, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		self.txt_dotdiameter = wx.StaticText( self, wx.ID_ANY, u"Dot Diameter:", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_dotdiameter.Wrap( -1 )
		gbSizer.Add( self.txt_dotdiameter, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.tc_dotdiameter = wx.TextCtrl( self, wx.ID_ANY, u"0.4", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer.Add( self.tc_dotdiameter, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), 0, 5 )
		
		self.txt_mm_1 = wx.StaticText( self, wx.ID_ANY, u"mm", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_mm_1.Wrap( -1 )
		gbSizer.Add( self.txt_mm_1, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.txt_linecolor = wx.StaticText( self, wx.ID_ANY, u"Line Color:", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_linecolor.Wrap( -1 )
		gbSizer.Add( self.txt_linecolor, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.clrpk_linecolor = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		gbSizer.Add( self.clrpk_linecolor, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 2 ), wx.EXPAND, 5 )
		
		self.txt_linewidth = wx.StaticText( self, wx.ID_ANY, u"Line Width:", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_linewidth.Wrap( -1 )
		gbSizer.Add( self.txt_linewidth, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.tc_linewidth = wx.TextCtrl( self, wx.ID_ANY, u"0.2", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer.Add( self.tc_linewidth, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		self.txt_mm_2 = wx.StaticText( self, wx.ID_ANY, u"mm", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_mm_2.Wrap( -1 )
		gbSizer.Add( self.txt_mm_2, wx.GBPosition( 5, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.txt_margin = wx.StaticText( self, wx.ID_ANY, u"Margin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_margin.Wrap( -1 )
		gbSizer.Add( self.txt_margin, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.txt_innermargin = wx.StaticText( self, wx.ID_ANY, u"Inner Margin:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_innermargin.Wrap( -1 )
		gbSizer.Add( self.txt_innermargin, wx.GBPosition( 7, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.tc_innermargin = wx.TextCtrl( self, wx.ID_ANY, u"20", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer.Add( self.tc_innermargin, wx.GBPosition( 7, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		self.txt_mm_3 = wx.StaticText( self, wx.ID_ANY, u"mm", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_mm_3.Wrap( -1 )
		gbSizer.Add( self.txt_mm_3, wx.GBPosition( 7, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.txt_outermargin = wx.StaticText( self, wx.ID_ANY, u"Outer Margin:", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_outermargin.Wrap( -1 )
		gbSizer.Add( self.txt_outermargin, wx.GBPosition( 8, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.tc_outermargin = wx.TextCtrl( self, wx.ID_ANY, u"15", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer.Add( self.tc_outermargin, wx.GBPosition( 8, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		self.txt_mm_4 = wx.StaticText( self, wx.ID_ANY, u"mm", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_mm_4.Wrap( -1 )
		gbSizer.Add( self.txt_mm_4, wx.GBPosition( 8, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.txt_topmargin = wx.StaticText( self, wx.ID_ANY, u"Top Margin:", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_topmargin.Wrap( -1 )
		gbSizer.Add( self.txt_topmargin, wx.GBPosition( 9, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.tc_topmargin = wx.TextCtrl( self, wx.ID_ANY, u"20", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer.Add( self.tc_topmargin, wx.GBPosition( 9, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		self.txt_mm_5 = wx.StaticText( self, wx.ID_ANY, u"mm", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_mm_5.Wrap( -1 )
		gbSizer.Add( self.txt_mm_5, wx.GBPosition( 9, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.txt_bottommargin = wx.StaticText( self, wx.ID_ANY, u"Bottom Margin:", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_bottommargin.Wrap( -1 )
		gbSizer.Add( self.txt_bottommargin, wx.GBPosition( 10, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.tc_bottommargin = wx.TextCtrl( self, wx.ID_ANY, u"20", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer.Add( self.tc_bottommargin, wx.GBPosition( 10, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		self.txt_mm_6 = wx.StaticText( self, wx.ID_ANY, u"mm", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_mm_6.Wrap( -1 )
		gbSizer.Add( self.txt_mm_6, wx.GBPosition( 10, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.txt_papersize = wx.StaticText( self, wx.ID_ANY, u"Paper Size", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_papersize.Wrap( -1 )
		gbSizer.Add( self.txt_papersize, wx.GBPosition( 11, 0 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.txt_pagewidth = wx.StaticText( self, wx.ID_ANY, u"Page Width:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_pagewidth.Wrap( -1 )
		gbSizer.Add( self.txt_pagewidth, wx.GBPosition( 12, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.tc_pagewidth = wx.TextCtrl( self, wx.ID_ANY, u"210", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer.Add( self.tc_pagewidth, wx.GBPosition( 12, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		self.txt_mm_7 = wx.StaticText( self, wx.ID_ANY, u"mm", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_mm_7.Wrap( -1 )
		gbSizer.Add( self.txt_mm_7, wx.GBPosition( 12, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.txt_pageheight = wx.StaticText( self, wx.ID_ANY, u"Page Height:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_pageheight.Wrap( -1 )
		gbSizer.Add( self.txt_pageheight, wx.GBPosition( 13, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.tc_pageheight = wx.TextCtrl( self, wx.ID_ANY, u"297", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer.Add( self.tc_pageheight, wx.GBPosition( 13, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		self.txt_mm_8 = wx.StaticText( self, wx.ID_ANY, u"mm", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_mm_8.Wrap( -1 )
		gbSizer.Add( self.txt_mm_8, wx.GBPosition( 13, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.txt_numpages = wx.StaticText( self, wx.ID_ANY, u"Number of Pages", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_numpages.Wrap( -1 )
		gbSizer.Add( self.txt_numpages, wx.GBPosition( 14, 0 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.txt_numberofpages = wx.StaticText( self, wx.ID_ANY, u"Number of Pages:", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_numberofpages.Wrap( -1 )
		gbSizer.Add( self.txt_numberofpages, wx.GBPosition( 15, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.tc_pagecount = wx.TextCtrl( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer.Add( self.tc_pagecount, wx.GBPosition( 15, 1 ), wx.GBSpan( 1, 2 ), wx.EXPAND, 5 )
		
		self.btn_genpdf = wx.Button( self, wx.ID_ANY, u"Generate PDF", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer.Add( self.btn_genpdf, wx.GBPosition( 16, 0 ), wx.GBSpan( 1, 3 ), wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 5 )
		
		bSizer.Add( gbSizer, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.SetSizer( bSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btn_genpdf.Bind( wx.EVT_BUTTON, self.btn_genpdfOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btn_genpdfOnButtonClick( self, event ):
		event.Skip()
	

