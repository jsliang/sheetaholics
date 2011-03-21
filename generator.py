# -*- coding: utf-8 -*-

import math
import sys
import xml.dom.minidom

from reportlab.graphics import renderPDF
from svglib.svglib import SvgRenderer
from StringIO import StringIO
from pyPdf import PdfFileWriter, PdfFileReader

def get_value_by_mm(mm):
    return float(mm) * 3.5433075 * 0.8

def get_svg(config):
    # Configurations
    gridSize = get_value_by_mm(config['gridSize'])
    pageWidth = get_value_by_mm(config['pageWidth'])
    pageHeight = get_value_by_mm(config['pageHeight'])
    marginInner = get_value_by_mm(config['marginInner'])
    marginOuter = get_value_by_mm(config['marginOuter'])
    marginTop = get_value_by_mm(config['marginTop'])
    marginBottom = get_value_by_mm(config['marginBottom'])
    dotDiameter = get_value_by_mm(config['dotDiameter'])
    dotRadius = dotDiameter / 2
    dotColor = config['dotColor']
    lineWidth = get_value_by_mm(config['lineWidth'])
    lineColor = config['lineColor']

    # Create the minidom document
    doc = xml.dom.minidom.Document()

    svg = doc.createElement("svg")
    svg.setAttribute('xmlns:dc', "http://purl.org/dc/elements/1.1/")
    svg.setAttribute('xmlns:cc', "http://creativecommons.org/ns#")
    svg.setAttribute('xmlns:rdf', "http://www.w3.org/1999/02/22-rdf-syntax-ns#")
    svg.setAttribute('xmlns:svg', "http://www.w3.org/2000/svg")
    svg.setAttribute('xmlns', "http://www.w3.org/2000/svg")
    svg.setAttribute('xmlns:sodipodi', "http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd")
    svg.setAttribute('width', str(pageWidth))
    svg.setAttribute('height', str(pageHeight))
    svg.setAttribute('style', "display:inline")
    doc.appendChild(svg)

    metadata = doc.createElement("metadata")
    metadata.setAttribute("id", "metadata1")
    svg.appendChild(metadata)
    rdf = doc.createElement("rdf:RDF")
    metadata.appendChild(rdf)
    cc_work = doc.createElement("cc:Work")
    rdf.appendChild(cc_work)
    dc_format = doc.createElement("dc:format")
    dc_format.appendChild(doc.createTextNode("image/svg+xml"))
    cc_work.appendChild(dc_format)
    dc_type = doc.createElement("dc:type")
    dc_type.setAttribute("rdf:resource", "http://purl.org/dc/dcmitype/StillImage")
    cc_work.appendChild(dc_type)
    dc_title = doc.createElement("dc:title")
    dc_title.setAttribute("rdf:resource", "http://purl.org/dc/dcmitype/StillImage")
    cc_work.appendChild(dc_title)

    col_count = int(math.floor((pageWidth - marginInner - marginOuter) / gridSize)) + 1
    row_count = int(math.floor((pageHeight - marginTop - marginBottom) / gridSize)) + 1
    
    x_adjust = ((pageWidth - marginInner - marginOuter) - (col_count - 1) * gridSize) / 2
    y_adjust = ((pageHeight - marginTop - marginBottom) - (row_count - 1) * gridSize) / 2

    # Draw lines
    lineLength = (pageWidth - marginInner - marginOuter)
    x_offset = marginInner
    y_offset = y_adjust + marginTop - lineWidth / 2

    for i in range (0, row_count):
        if i == 1:
            continue
        elif i == 0 or i == 2 or i == row_count - 1:
            _lineWidth = lineWidth * 2
        else:
            _lineWidth = lineWidth
            
        y = y_offset + i * gridSize
        path = doc.createElement("path")
        path.setAttribute("id", "line-%02d" % (i))
        path.setAttribute("sodipodi:nodetypes", "ccccc")
        path.setAttribute("d", "m %(x_offset)f,%(y)f c 0,0.354331 0,0.708661 0,%(lineWidth)f 217.322862,0 434.645722,0 %(lineLength)f,0 0,-0.354331 0,-0.708661 0,-%(lineWidth)f -217.32286,0 -434.64572,0 -%(lineLength)f,0 z" % {'x_offset': x_offset, 'lineLength': lineLength, 'lineWidth': _lineWidth, 'y': y})
        path.setAttribute("style", "fill:%(lineColor)s;fill-opacity:1;stroke:none" % {'lineColor': lineColor})
        svg.appendChild(path)

    # Draw dots
    ratio = dotRadius / get_value_by_mm(4)
    x_offset = x_adjust + marginInner - dotDiameter
    y_offset = y_adjust + marginTop - dotDiameter * 3.9

    for i in range (0, col_count):
        for j in range (3, row_count - 1):
            x = x_offset + i * gridSize
            y = y_offset + j * gridSize
            
            path = doc.createElement("path")
            path.setAttribute("id", "dot-%02d-%02d" % (i, j))
            path.setAttribute("style", "fill:%(dotColor)s;fill-opacity:1;stroke:none" % {'dotColor': dotColor})
            path.setAttribute("sodipodi:nodetypes", "cssss")
            path.setAttribute("d", "m 42.519691,88.582687 c 0,7.827659 -6.345572,14.173233 -14.173231,14.173233 -7.827659,0 -14.17323,-6.345574 -14.17323,-14.173233 0,-7.827659 6.345571,-14.17323 14.17323,-14.17323 7.827659,0 14.173231,6.345571 14.173231,14.17323 z")
            path.setAttribute("transform", "matrix(%(ratio)f,0,0,%(ratio)f,%(x)f,%(y)f)" % {'ratio': ratio, 'x': x, 'y': y})
            svg.appendChild(path)

    return doc

def get_pdf_string(config):
    # Get SVG XML data
    svg = get_svg(config).documentElement
    
    # Convert SVG XML data to an RLG Drawing object
    svgRenderer = SvgRenderer()
    svgRenderer.render(svg)
    drawing = svgRenderer.finish()
    
    return renderPDF.drawToString(drawing)

def swap_horizontal_margins(config):
    _config = {}
    for key, value in config.items():
        if key == 'marginInner':
            _config['marginOuter'] = value
        elif key == 'marginOuter':
            _config['marginInner'] = value
        else:
            _config[key] = value
    return _config

def get_pdf_content(config_param={}):
    config = {}
    config['gridSize'] =        8
    config['pageWidth'] =       210
    config['pageHeight'] =      297
    config['marginInner'] =     20
    config['marginOuter'] =     15
    config['marginTop'] =       15
    config['marginBottom'] =    15
    config['dotDiameter'] =     0.4
    config['dotColor'] =        "#000000"
    config['lineWidth'] =       0.2
    config['lineColor'] =       "#000000"
    config['pageCount'] =       5

    config.update(config_param)

    oddPage = get_pdf_string(config)
    evenPage = get_pdf_string(swap_horizontal_margins(config))
    oddPageReader = PdfFileReader(StringIO(oddPage)).getPage(0)
    evenPageReader = PdfFileReader(StringIO(evenPage)).getPage(0)
    
    output = PdfFileWriter()
    for i in range (0, int(config['pageCount'])):
        if i % 2 == 0:
            output.addPage(oddPageReader)
        else:
            output.addPage(evenPageReader)
    
    pdf_str = StringIO()
    outputStream = pdf_str
    output.write(outputStream)
    pdf_content = pdf_str.getvalue()
    outputStream.close()
    
    return pdf_content

if __name__ == "__main__":
    sys.exit(main())
