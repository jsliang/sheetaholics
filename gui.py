# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 30 2011)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Sheetaholics_Main
###########################################################################

class Sheetaholics_Main ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Sheetaholics: 筆記頁產生器 V2.0", pos = wx.DefaultPosition, size = wx.Size( 600,450 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer = wx.FlexGridSizer( 1, 2, 5, 5 )
		fgSizer.AddGrowableCol( 0 )
		fgSizer.AddGrowableCol( 1 )
		fgSizer.AddGrowableRow( 0 )
		fgSizer.AddGrowableRow( 1 )
		fgSizer.SetFlexibleDirection( wx.BOTH )
		fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer_left = wx.FlexGridSizer( 3, 1, 10, 10 )
		fgSizer_left.AddGrowableCol( 0 )
		fgSizer_left.AddGrowableRow( 0 )
		fgSizer_left.AddGrowableRow( 1 )
		fgSizer_left.AddGrowableRow( 2 )
		fgSizer_left.SetFlexibleDirection( wx.BOTH )
		fgSizer_left.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		sbSizer_dottedlined_papersize = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"紙張尺寸" ), wx.VERTICAL )
		
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
		
		sbSizer_dottedlined_papersize.Add( fgSizer_papersize, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		fgSizer_left.Add( sbSizer_dottedlined_papersize, 1, wx.EXPAND, 5 )
		
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
		
		fgSizer_left.Add( sbSizer_margin, 1, wx.EXPAND, 5 )
		
		sbSizer_dottedlined_output = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"輸出設定" ), wx.VERTICAL )
		
		fgSizer_output = wx.FlexGridSizer( 2, 2, 5, 5 )
		fgSizer_output.AddGrowableCol( 1 )
		fgSizer_output.AddGrowableRow( 0 )
		fgSizer_output.AddGrowableRow( 1 )
		fgSizer_output.SetFlexibleDirection( wx.BOTH )
		fgSizer_output.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.txt_numberofpages = wx.StaticText( self, wx.ID_ANY, u"輸出頁數：", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_numberofpages.Wrap( -1 )
		fgSizer_output.Add( self.txt_numberofpages, 0, wx.BOTTOM|wx.TOP|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.sc_pagecount = wx.SpinCtrl( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 1000, 2 )
		fgSizer_output.Add( self.sc_pagecount, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt_outputdir = wx.StaticText( self, wx.ID_ANY, u"輸出目錄：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_outputdir.Wrap( -1 )
		fgSizer_output.Add( self.txt_outputdir, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.BOTTOM|wx.TOP, 5 )
		
		self.dp_output = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"請選擇PDF檔案的輸出目錄", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		fgSizer_output.Add( self.dp_output, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		sbSizer_dottedlined_output.Add( fgSizer_output, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 5 )
		
		fgSizer_left.Add( sbSizer_dottedlined_output, 1, wx.EXPAND, 5 )
		
		fgSizer.Add( fgSizer_left, 1, wx.ALL|wx.EXPAND, 5 )
		
		fgSizer_right = wx.FlexGridSizer( 4, 1, 0, 0 )
		fgSizer_right.AddGrowableCol( 0 )
		fgSizer_right.AddGrowableRow( 0 )
		fgSizer_right.AddGrowableRow( 1 )
		fgSizer_right.AddGrowableRow( 2 )
		fgSizer_right.SetFlexibleDirection( wx.BOTH )
		fgSizer_right.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		sbSizer_dotnline = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"點線設定" ), wx.VERTICAL )
		
		fgSizer_dotnline = wx.FlexGridSizer( 7, 4, 5, 5 )
		fgSizer_dotnline.AddGrowableRow( 0 )
		fgSizer_dotnline.AddGrowableRow( 1 )
		fgSizer_dotnline.AddGrowableRow( 2 )
		fgSizer_dotnline.AddGrowableRow( 3 )
		fgSizer_dotnline.AddGrowableRow( 4 )
		fgSizer_dotnline.AddGrowableRow( 5 )
		fgSizer_dotnline.AddGrowableRow( 6 )
		fgSizer_dotnline.SetFlexibleDirection( wx.BOTH )
		fgSizer_dotnline.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer_dotnline.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.txt_gridsize = wx.StaticText( self, wx.ID_ANY, u"點線間距：", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_gridsize.Wrap( -1 )
		fgSizer_dotnline.Add( self.txt_gridsize, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.BOTTOM|wx.TOP, 5 )
		
		self.tc_gridsize = wx.TextCtrl( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_dotnline.Add( self.tc_gridsize, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt_mm_0 = wx.StaticText( self, wx.ID_ANY, u"mm", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_mm_0.Wrap( -1 )
		fgSizer_dotnline.Add( self.txt_mm_0, 0, wx.BOTTOM|wx.TOP|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer_dotnline.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer_dotnline.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer_dotnline.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer_dotnline.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.cb_drawdots = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cb_drawdots.SetValue(True) 
		self.cb_drawdots.SetToolTipString( u"繪製點" )
		
		fgSizer_dotnline.Add( self.cb_drawdots, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt_dotcolor = wx.StaticText( self, wx.ID_ANY, u"圓點顏色：", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_dotcolor.Wrap( -1 )
		fgSizer_dotnline.Add( self.txt_dotcolor, 0, wx.ALIGN_RIGHT|wx.BOTTOM|wx.TOP|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.clrpk_dotcolor = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		fgSizer_dotnline.Add( self.clrpk_dotcolor, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer_dotnline.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer_dotnline.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.txt_dotdiameter = wx.StaticText( self, wx.ID_ANY, u"圓點直徑：", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_dotdiameter.Wrap( -1 )
		fgSizer_dotnline.Add( self.txt_dotdiameter, 0, wx.ALIGN_RIGHT|wx.BOTTOM|wx.TOP|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.tc_dotdiameter = wx.TextCtrl( self, wx.ID_ANY, u"0.4", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_dotnline.Add( self.tc_dotdiameter, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt_mm_1 = wx.StaticText( self, wx.ID_ANY, u"mm", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_mm_1.Wrap( -1 )
		fgSizer_dotnline.Add( self.txt_mm_1, 0, wx.BOTTOM|wx.TOP|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer_dotnline.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer_dotnline.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer_dotnline.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer_dotnline.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.cb_drawlines = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cb_drawlines.SetValue(True) 
		self.cb_drawlines.SetToolTipString( u"繪製線" )
		
		fgSizer_dotnline.Add( self.cb_drawlines, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt_linecolor = wx.StaticText( self, wx.ID_ANY, u"橫線顏色：", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_linecolor.Wrap( -1 )
		fgSizer_dotnline.Add( self.txt_linecolor, 0, wx.ALIGN_RIGHT|wx.BOTTOM|wx.TOP|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.clrpk_linecolor = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		fgSizer_dotnline.Add( self.clrpk_linecolor, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer_dotnline.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer_dotnline.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.txt_linewidth = wx.StaticText( self, wx.ID_ANY, u"橫線線寬：", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_linewidth.Wrap( -1 )
		fgSizer_dotnline.Add( self.txt_linewidth, 0, wx.ALIGN_RIGHT|wx.BOTTOM|wx.TOP|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.tc_linewidth = wx.TextCtrl( self, wx.ID_ANY, u"0.2", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_dotnline.Add( self.tc_linewidth, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt_mm_2 = wx.StaticText( self, wx.ID_ANY, u"mm", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_mm_2.Wrap( -1 )
		fgSizer_dotnline.Add( self.txt_mm_2, 0, wx.BOTTOM|wx.TOP|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sbSizer_dotnline.Add( fgSizer_dotnline, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		fgSizer_right.Add( sbSizer_dotnline, 1, wx.ALL|wx.EXPAND, 5 )
		
		sbSizer_pronunciation = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"音標區" ), wx.VERTICAL )
		
		fgSizer_pronunciation = wx.FlexGridSizer( 3, 1, 5, 5 )
		fgSizer_pronunciation.AddGrowableRow( 0 )
		fgSizer_pronunciation.AddGrowableRow( 1 )
		fgSizer_pronunciation.AddGrowableRow( 2 )
		fgSizer_pronunciation.SetFlexibleDirection( wx.BOTH )
		fgSizer_pronunciation.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.cb_drawpron = wx.CheckBox( self, wx.ID_ANY, u"插入音標列", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_pronunciation.Add( self.cb_drawpron, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		fgSizer_pronunheight = wx.FlexGridSizer( 1, 3, 5, 5 )
		fgSizer_pronunheight.SetFlexibleDirection( wx.BOTH )
		fgSizer_pronunheight.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.txt_pron = wx.StaticText( self, wx.ID_ANY, u"音標列高度：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_pron.Wrap( -1 )
		fgSizer_pronunheight.Add( self.txt_pron, 0, wx.TOP|wx.BOTTOM|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.tc_pronheight = wx.TextCtrl( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_pronunheight.Add( self.tc_pronheight, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt_dottedlined_mm_3 = wx.StaticText( self, wx.ID_ANY, u"mm", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.txt_dottedlined_mm_3.Wrap( -1 )
		fgSizer_pronunheight.Add( self.txt_dottedlined_mm_3, 0, wx.TOP|wx.BOTTOM|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		fgSizer_pronunciation.Add( fgSizer_pronunheight, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt_pronun_comments = wx.StaticText( self, wx.ID_ANY, u"音標區可書寫英文音標、日文假名等，\n適用於語言學習筆記。", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_pronun_comments.Wrap( -1 )
		fgSizer_pronunciation.Add( self.txt_pronun_comments, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sbSizer_pronunciation.Add( fgSizer_pronunciation, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		fgSizer_right.Add( sbSizer_pronunciation, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.btn_dottedlined_genpdf = wx.Button( self, wx.ID_ANY, u"產生點線筆記頁PDF檔", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_right.Add( self.btn_dottedlined_genpdf, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		fgSizer_footer = wx.FlexGridSizer( 2, 2, 5, 5 )
		fgSizer_footer.SetFlexibleDirection( wx.BOTH )
		fgSizer_footer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.txt_author = wx.StaticText( self, wx.ID_ANY, u"作者:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_author.Wrap( -1 )
		fgSizer_footer.Add( self.txt_author, 0, wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT, 5 )
		
		self.txt_authormail = wx.StaticText( self, wx.ID_ANY, u"jsliang (jsliang.tw@gmail.com)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_authormail.Wrap( -1 )
		fgSizer_footer.Add( self.txt_authormail, 0, 0, 5 )
		
		self.txt_github = wx.StaticText( self, wx.ID_ANY, u"GitHub:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_github.Wrap( -1 )
		fgSizer_footer.Add( self.txt_github, 0, wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT, 5 )
		
		self.hl_github = wx.HyperlinkCtrl( self, wx.ID_ANY, u"jsliang/sheetaholics ", u"https://github.com/jsliang/sheetaholics", wx.DefaultPosition, wx.DefaultSize, wx.HL_DEFAULT_STYLE )
		fgSizer_footer.Add( self.hl_github, 0, wx.ALIGN_BOTTOM, 5 )
		
		fgSizer_right.Add( fgSizer_footer, 1, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )
		
		fgSizer.Add( fgSizer_right, 1, wx.EXPAND, 5 )
		
		bSizer.Add( fgSizer, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.SetSizer( bSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.cb_drawdots.Bind( wx.EVT_CHECKBOX, self.cb_drawdotsOnCheckBox )
		self.cb_drawlines.Bind( wx.EVT_CHECKBOX, self.cb_drawlinesOnCheckBox )
		self.cb_drawpron.Bind( wx.EVT_CHECKBOX, self.cb_drawpronOnCheckBox )
		self.btn_dottedlined_genpdf.Bind( wx.EVT_BUTTON, self.btn_dottedlined_genpdfOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def cb_drawdotsOnCheckBox( self, event ):
		event.Skip()
	
	def cb_drawlinesOnCheckBox( self, event ):
		event.Skip()
	
	def cb_drawpronOnCheckBox( self, event ):
		event.Skip()
	
	def btn_dottedlined_genpdfOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class Sheetaholics_Finished_Dialog
###########################################################################

class Sheetaholics_Finished_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"PDF檔已產生", pos = wx.DefaultPosition, size = wx.Size( 500,150 ), style = wx.DEFAULT_DIALOG_STYLE )
		
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
	

