# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Nov 17 2010)
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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Sheetaholics: 點線筆記頁產生器 V1.1", pos = wx.DefaultPosition, size = wx.Size( 500,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer = wx.FlexGridSizer( 3, 1, 5, 5 )
		fgSizer.AddGrowableCol( 0 )
		fgSizer.AddGrowableRow( 0 )
		fgSizer.AddGrowableRow( 2 )
		fgSizer.SetFlexibleDirection( wx.BOTH )
		fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		gbSizer_settings = wx.GridBagSizer( 0, 0 )
		gbSizer_settings.AddGrowableCol( 0 )
		gbSizer_settings.AddGrowableCol( 1 )
		gbSizer_settings.AddGrowableRow( 0 )
		gbSizer_settings.AddGrowableRow( 1 )
		gbSizer_settings.AddGrowableRow( 2 )
		gbSizer_settings.SetFlexibleDirection( wx.BOTH )
		gbSizer_settings.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		sbSizer_dotnline = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"點線設定" ), wx.VERTICAL )
		
		fgSizer_dotnline = wx.FlexGridSizer( 5, 3, 5, 5 )
		fgSizer_dotnline.AddGrowableRow( 0 )
		fgSizer_dotnline.AddGrowableRow( 1 )
		fgSizer_dotnline.AddGrowableRow( 2 )
		fgSizer_dotnline.AddGrowableRow( 3 )
		fgSizer_dotnline.AddGrowableRow( 4 )
		fgSizer_dotnline.SetFlexibleDirection( wx.BOTH )
		fgSizer_dotnline.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.txt_gridsize = wx.StaticText( self, wx.ID_ANY, u"方眼大小：", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_gridsize.Wrap( -1 )
		fgSizer_dotnline.Add( self.txt_gridsize, 0, wx.ALIGN_RIGHT|wx.BOTTOM|wx.TOP|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.tc_gridsize = wx.TextCtrl( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_dotnline.Add( self.tc_gridsize, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt_mm_0 = wx.StaticText( self, wx.ID_ANY, u"mm", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_mm_0.Wrap( -1 )
		fgSizer_dotnline.Add( self.txt_mm_0, 0, wx.BOTTOM|wx.TOP|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt_dotcolor = wx.StaticText( self, wx.ID_ANY, u"圓點顏色：", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_dotcolor.Wrap( -1 )
		fgSizer_dotnline.Add( self.txt_dotcolor, 0, wx.ALIGN_RIGHT|wx.BOTTOM|wx.TOP|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.clrpk_dotcolor = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		fgSizer_dotnline.Add( self.clrpk_dotcolor, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer_dotnline.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.txt_dotdiameter = wx.StaticText( self, wx.ID_ANY, u"圓點直徑：", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_dotdiameter.Wrap( -1 )
		fgSizer_dotnline.Add( self.txt_dotdiameter, 0, wx.ALIGN_RIGHT|wx.BOTTOM|wx.TOP|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.tc_dotdiameter = wx.TextCtrl( self, wx.ID_ANY, u"0.4", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_dotnline.Add( self.tc_dotdiameter, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt_mm_1 = wx.StaticText( self, wx.ID_ANY, u"mm", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_mm_1.Wrap( -1 )
		fgSizer_dotnline.Add( self.txt_mm_1, 0, wx.BOTTOM|wx.TOP|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt_linecolor = wx.StaticText( self, wx.ID_ANY, u"橫線顏色：", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_linecolor.Wrap( -1 )
		fgSizer_dotnline.Add( self.txt_linecolor, 0, wx.ALIGN_RIGHT|wx.BOTTOM|wx.TOP|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.clrpk_linecolor = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		fgSizer_dotnline.Add( self.clrpk_linecolor, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer_dotnline.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.txt_linewidth = wx.StaticText( self, wx.ID_ANY, u"橫線線寬：", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_linewidth.Wrap( -1 )
		fgSizer_dotnline.Add( self.txt_linewidth, 0, wx.ALIGN_RIGHT|wx.BOTTOM|wx.TOP|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.tc_linewidth = wx.TextCtrl( self, wx.ID_ANY, u"0.2", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_dotnline.Add( self.tc_linewidth, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt_mm_2 = wx.StaticText( self, wx.ID_ANY, u"mm", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_mm_2.Wrap( -1 )
		fgSizer_dotnline.Add( self.txt_mm_2, 0, wx.BOTTOM|wx.TOP|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sbSizer_dotnline.Add( fgSizer_dotnline, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gbSizer_settings.Add( sbSizer_dotnline, wx.GBPosition( 0, 0 ), wx.GBSpan( 2, 1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
		
		sbSizer_margin = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"頁面邊界" ), wx.VERTICAL )
		
		fgSizer_margin = wx.FlexGridSizer( 4, 3, 5, 5 )
		fgSizer_margin.AddGrowableRow( 0 )
		fgSizer_margin.AddGrowableRow( 1 )
		fgSizer_margin.AddGrowableRow( 2 )
		fgSizer_margin.AddGrowableRow( 3 )
		fgSizer_margin.SetFlexibleDirection( wx.BOTH )
		fgSizer_margin.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.txt_innermargin = wx.StaticText( self, wx.ID_ANY, u"內側邊界：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_innermargin.Wrap( -1 )
		fgSizer_margin.Add( self.txt_innermargin, 0, wx.ALIGN_RIGHT|wx.BOTTOM|wx.TOP, 5 )
		
		self.tc_innermargin = wx.TextCtrl( self, wx.ID_ANY, u"20", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_margin.Add( self.tc_innermargin, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.txt_mm_3 = wx.StaticText( self, wx.ID_ANY, u"mm", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_mm_3.Wrap( -1 )
		fgSizer_margin.Add( self.txt_mm_3, 0, wx.BOTTOM|wx.TOP, 5 )
		
		self.txt_outermargin = wx.StaticText( self, wx.ID_ANY, u"外側邊界：", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_outermargin.Wrap( -1 )
		fgSizer_margin.Add( self.txt_outermargin, 0, wx.ALIGN_RIGHT|wx.BOTTOM|wx.TOP, 5 )
		
		self.tc_outermargin = wx.TextCtrl( self, wx.ID_ANY, u"15", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_margin.Add( self.tc_outermargin, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.txt_mm_4 = wx.StaticText( self, wx.ID_ANY, u"mm", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_mm_4.Wrap( -1 )
		fgSizer_margin.Add( self.txt_mm_4, 0, wx.BOTTOM|wx.TOP, 5 )
		
		self.txt_topmargin = wx.StaticText( self, wx.ID_ANY, u"上方邊界：", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_topmargin.Wrap( -1 )
		fgSizer_margin.Add( self.txt_topmargin, 0, wx.ALIGN_RIGHT|wx.BOTTOM|wx.TOP, 5 )
		
		self.tc_topmargin = wx.TextCtrl( self, wx.ID_ANY, u"20", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_margin.Add( self.tc_topmargin, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.txt_mm_5 = wx.StaticText( self, wx.ID_ANY, u"mm", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_mm_5.Wrap( -1 )
		fgSizer_margin.Add( self.txt_mm_5, 0, wx.BOTTOM|wx.TOP, 5 )
		
		self.txt_bottommargin = wx.StaticText( self, wx.ID_ANY, u"下方邊界：", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_bottommargin.Wrap( -1 )
		fgSizer_margin.Add( self.txt_bottommargin, 0, wx.ALIGN_RIGHT|wx.BOTTOM|wx.TOP, 5 )
		
		self.tc_bottommargin = wx.TextCtrl( self, wx.ID_ANY, u"20", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_margin.Add( self.tc_bottommargin, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.txt_mm_6 = wx.StaticText( self, wx.ID_ANY, u"mm", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_mm_6.Wrap( -1 )
		fgSizer_margin.Add( self.txt_mm_6, 0, wx.BOTTOM|wx.TOP, 5 )
		
		sbSizer_margin.Add( fgSizer_margin, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		gbSizer_settings.Add( sbSizer_margin, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
		
		sbSizer_pagecount = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"輸出頁數" ), wx.VERTICAL )
		
		fgSizer_pagecount = wx.FlexGridSizer( 1, 2, 5, 5 )
		fgSizer_pagecount.AddGrowableRow( 0 )
		fgSizer_pagecount.SetFlexibleDirection( wx.BOTH )
		fgSizer_pagecount.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.txt_numberofpages = wx.StaticText( self, wx.ID_ANY, u"輸出頁數：", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_numberofpages.Wrap( -1 )
		fgSizer_pagecount.Add( self.txt_numberofpages, 0, wx.BOTTOM|wx.TOP|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.sc_pagecount = wx.SpinCtrl( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 1000, 2 )
		fgSizer_pagecount.Add( self.sc_pagecount, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sbSizer_pagecount.Add( fgSizer_pagecount, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		gbSizer_settings.Add( sbSizer_pagecount, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
		
		sbSizer_papersize = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"紙張尺寸" ), wx.VERTICAL )
		
		fgSizer_papersize = wx.FlexGridSizer( 2, 3, 5, 5 )
		fgSizer_papersize.AddGrowableRow( 0 )
		fgSizer_papersize.AddGrowableRow( 1 )
		fgSizer_papersize.SetFlexibleDirection( wx.BOTH )
		fgSizer_papersize.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.txt_pagewidth = wx.StaticText( self, wx.ID_ANY, u"頁面寬度：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_pagewidth.Wrap( -1 )
		fgSizer_papersize.Add( self.txt_pagewidth, 0, wx.ALIGN_RIGHT|wx.BOTTOM|wx.TOP|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.tc_pagewidth = wx.TextCtrl( self, wx.ID_ANY, u"210", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_papersize.Add( self.tc_pagewidth, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt_mm_7 = wx.StaticText( self, wx.ID_ANY, u"mm", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_mm_7.Wrap( -1 )
		fgSizer_papersize.Add( self.txt_mm_7, 0, wx.BOTTOM|wx.TOP|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt_pageheight = wx.StaticText( self, wx.ID_ANY, u"頁面高度：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_pageheight.Wrap( -1 )
		fgSizer_papersize.Add( self.txt_pageheight, 0, wx.ALIGN_RIGHT|wx.BOTTOM|wx.TOP|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.tc_pageheight = wx.TextCtrl( self, wx.ID_ANY, u"297", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_papersize.Add( self.tc_pageheight, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt_mm_8 = wx.StaticText( self, wx.ID_ANY, u"mm", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_mm_8.Wrap( -1 )
		fgSizer_papersize.Add( self.txt_mm_8, 0, wx.BOTTOM|wx.TOP|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sbSizer_papersize.Add( fgSizer_papersize, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		gbSizer_settings.Add( sbSizer_papersize, wx.GBPosition( 1, 1 ), wx.GBSpan( 2, 1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
		
		fgSizer.Add( gbSizer_settings, 1, wx.EXPAND, 5 )
		
		fgSizer_outputdir = wx.FlexGridSizer( 1, 2, 0, 0 )
		fgSizer_outputdir.AddGrowableCol( 1 )
		fgSizer_outputdir.SetFlexibleDirection( wx.BOTH )
		fgSizer_outputdir.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.txt_outputdir = wx.StaticText( self, wx.ID_ANY, u"PDF檔輸出目錄：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_outputdir.Wrap( -1 )
		fgSizer_outputdir.Add( self.txt_outputdir, 0, wx.BOTTOM|wx.LEFT|wx.TOP|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.dp_output = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"請選擇PDF檔案的輸出目錄", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		fgSizer_outputdir.Add( self.dp_output, 0, wx.EXPAND|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		fgSizer.Add( fgSizer_outputdir, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
		
		gSizer_footer = wx.GridSizer( 1, 2, 0, 0 )
		
		fgSizer_footer = wx.FlexGridSizer( 2, 2, 5, 5 )
		fgSizer_footer.SetFlexibleDirection( wx.BOTH )
		fgSizer_footer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText_author = wx.StaticText( self, wx.ID_ANY, u"作者:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_author.Wrap( -1 )
		fgSizer_footer.Add( self.m_staticText_author, 0, wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT, 5 )
		
		self.m_staticText57 = wx.StaticText( self, wx.ID_ANY, u"jsliang (jsliang.tw@gmail.com)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText57.Wrap( -1 )
		fgSizer_footer.Add( self.m_staticText57, 0, 0, 5 )
		
		self.m_staticText_github = wx.StaticText( self, wx.ID_ANY, u"GitHub:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_github.Wrap( -1 )
		fgSizer_footer.Add( self.m_staticText_github, 0, wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT, 5 )
		
		self.m_hyperlink_github = wx.HyperlinkCtrl( self, wx.ID_ANY, u"jsliang/sheetaholics ", u"https://github.com/jsliang/sheetaholics", wx.DefaultPosition, wx.DefaultSize, wx.HL_DEFAULT_STYLE )
		fgSizer_footer.Add( self.m_hyperlink_github, 0, wx.ALIGN_BOTTOM, 5 )
		
		gSizer_footer.Add( fgSizer_footer, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btn_genpdf = wx.Button( self, wx.ID_ANY, u"產生PDF檔", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer_footer.Add( self.btn_genpdf, 0, wx.ALIGN_RIGHT|wx.EXPAND|wx.LEFT, 5 )
		
		fgSizer.Add( gSizer_footer, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer.Add( fgSizer, 1, wx.ALL|wx.EXPAND, 5 )
		
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
	

###########################################################################
## Class Sheetaholics_DottedLined_Finished
###########################################################################

class Sheetaholics_DottedLined_Finished ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"PDF檔已產生", pos = wx.DefaultPosition, size = wx.Size( 350,150 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer = wx.FlexGridSizer( 3, 1, 5, 5 )
		fgSizer.AddGrowableCol( 0 )
		fgSizer.AddGrowableRow( 0 )
		fgSizer.AddGrowableRow( 1 )
		fgSizer.AddGrowableRow( 2 )
		fgSizer.SetFlexibleDirection( wx.BOTH )
		fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.txt_msg = wx.StaticText( self, wx.ID_ANY, u"PDF檔已產生！", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_msg.Wrap( -1 )
		fgSizer.Add( self.txt_msg, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		fgSizer_path = wx.FlexGridSizer( 1, 2, 0, 0 )
		fgSizer_path.AddGrowableCol( 1 )
		fgSizer_path.SetFlexibleDirection( wx.BOTH )
		fgSizer_path.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.txt_pdfpath = wx.StaticText( self, wx.ID_ANY, u"檔案路徑：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_pdfpath.Wrap( -1 )
		fgSizer_path.Add( self.txt_pdfpath, 0, wx.ALL, 5 )
		
		self.tc_pdfpath = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer_path.Add( self.tc_pdfpath, 0, wx.EXPAND, 5 )
		
		fgSizer.Add( fgSizer_path, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btn_ok = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer.Add( self.btn_ok, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer.Add( fgSizer, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.SetSizer( bSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btn_ok.Bind( wx.EVT_BUTTON, self.btn_okOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btn_okOnButtonClick( self, event ):
		event.Skip()
	

