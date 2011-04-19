# -*- coding: utf-8 -*-

import math
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
import sys

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

def genpdf(filename, config):
    if config == None:
        config = {}
        config['gridSize'] =        8
        config['drawPron'] =        False
        config['pronHeight'] =      4
        config['pageWidth'] =       210
        config['pageHeight'] =      297
        config['marginInner'] =     20
        config['marginOuter'] =     15
        config['marginTop'] =       15
        config['marginBottom'] =    15
        config['drawdots'] =        True
        config['dotDiameter'] =     0.4
        config['dotColor'] =        (0, 0, 0)
        config['drawlines'] =       True
        config['lineWidth'] =       0.2
        config['lineColor'] =       (0, 0, 0)
        config['pageCount'] =       5

    # Load Configurations from Parameters
    gridSize = config['gridSize']*mm
    drawPron = config['drawPron']
    if drawPron:
        pronHeight = config['pronHeight']*mm
    else:
        pronHeight = 0
    pageWidth = config['pageWidth']*mm
    pageHeight = config['pageHeight']*mm
    marginInner = config['marginInner']*mm
    marginOuter = config['marginOuter']*mm
    marginTop = config['marginTop']*mm
    marginBottom = config['marginBottom']*mm
    drawDots = config['drawdots']
    dotDiameter = config['dotDiameter']*mm
    dotRadius = dotDiameter / 2
    dotColor = config['dotColor']
    drawLines = config['drawlines']
    lineWidth = config['lineWidth']*mm
    lineColor = config['lineColor']

    # Create the document
    c = canvas.Canvas(filename, pagesize = (pageWidth, pageHeight), bottomup = 0)
    
    col_count = int(math.floor((pageWidth - marginInner - marginOuter) / gridSize)) + 1
    row_count = int(math.floor((pageHeight - marginTop - marginBottom) / (gridSize + pronHeight))) + 1
    
    for i in range (0, int(config['pageCount'])):
        # Swap marginOuter & marginInner alternatively for even & odd pages
        if i > 0:
            _tmp = marginOuter
            marginOuter = marginInner
            marginInner = _tmp
        
        # Required adjustment for reportlab
        x_adjust = ((pageWidth - marginInner - marginOuter) - (col_count - 1) * gridSize) / 2
        y_adjust = ((pageHeight - marginTop - marginBottom) - (row_count - 1) * (gridSize + pronHeight)) / 2
        
        if drawLines:
            # Draw lines
            lineLength = (pageWidth - marginInner - marginOuter)
            x_offset = marginInner
            y_offset = y_adjust + marginTop - lineWidth / 2
            
            c.setStrokeColorRGB(lineColor[0], lineColor[1], lineColor[2])
            for i in range (0, row_count):
                if i == 1 and not drawPron:
                    continue
                
                isFirstLine = (i == 0)
                isLastLine = (i == row_count - 1)
                
                y = y_offset + i * (gridSize + pronHeight)
                if drawPron and i == 1:
                    pass
                else:
                    isHeaderBottomLine = (i == 2)
                    
                    if isFirstLine or (not drawPron and (isHeaderBottomLine or isLastLine)):
                        c.setLineWidth(lineWidth * 2)
                    else:
                        c.setLineWidth(lineWidth)
                    
                    c.line(x_offset, y, x_offset + lineLength, y)
                    
                if drawPron:
                    y += pronHeight
                    
                    if isFirstLine:
                        y = y + gridSize
                    
                    if isFirstLine or isLastLine:
                        c.setLineWidth(lineWidth * 2)
                    else:
                        c.setLineWidth(lineWidth)
                    
                    c.line(x_offset, y, x_offset + lineLength, y)
        
        if drawDots:
            # Draw dots
            x_offset = x_adjust + marginInner
            y_offset = y_adjust + marginTop - lineWidth / 2

            c.setFillColorRGB(dotColor[0], dotColor[1], dotColor[2])
            
            for i in range (0, row_count):
                if i == 1 and not drawPron:
                    continue
                
                y = y_offset + i * (gridSize + pronHeight)
                
                for j in range (0, col_count):
                    x = x_offset + j * gridSize
                    c.circle(x, y, dotRadius, stroke=0, fill=1)
                
                if drawPron and not i == 0:
                    y += pronHeight
                    
                    for j in range (0, col_count):
                        x = x_offset + j * gridSize
                        c.circle(x, y, dotRadius, stroke=0, fill=1)
        
        c.showPage()
    
    c.save()

if __name__ == "__main__":
    sys.exit(main())
