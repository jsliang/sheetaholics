genpdf = () ->
    # Load Configurations from Parameters
    gridSize = parseFloat(document.getElementById('gridSize').value)
    marginInner = parseFloat(document.getElementById('marginInner').value)
    marginOuter = parseFloat(document.getElementById('marginOuter').value)
    marginTop = parseFloat(document.getElementById('marginTop').value)
    marginBottom = parseFloat(document.getElementById('marginBottom').value)
    dotDiameter = parseFloat(document.getElementById('dotDiameter').value)
    dotRadius = dotDiameter / 2
    dotColorR = parseInt(document.getElementById('dotColor').color.rgb[0] * 255)
    dotColorG = parseInt(document.getElementById('dotColor').color.rgb[1] * 255)
    dotColorB = parseInt(document.getElementById('dotColor').color.rgb[2] * 255)
    lineWidth = parseInt(document.getElementById('lineWidth').value)
    lineColorR = parseInt(document.getElementById('lineColor').color.rgb[0] * 255)
    lineColorG = parseInt(document.getElementById('lineColor').color.rgb[1] * 255)
    lineColorB = parseInt(document.getElementById('lineColor').color.rgb[2] * 255)
    pageFormat = document.getElementById('pageFormat').value
    pageCount = parseInt(document.getElementById('pageCount').value)

    if pageFormat is 'a3'
        pageWidth = 297
        pageHeight = 420
    else if pageFormat is 'a4'
        pageWidth = 210
        pageHeight = 297
    else if pageFormat is 'a5'
        pageWidth = 148
        pageHeight = 210
    else if pageFormat is 'letter'
        pageWidth = 216
        pageHeight = 279
    else if pageFormat is 'legal'
        pageWidth = 216
        pageHeight = 356

    # Create the document
    pdf = new jsPDF('p','mm',pageFormat)

    col_count = parseInt(Math.floor((pageWidth - marginInner - marginOuter) / gridSize)) + 1
    row_count = parseInt(Math.floor((pageHeight - marginTop - marginBottom) / gridSize)) + 1


    for i in [1..pageCount]
        # Swap marginOuter & marginInner alternatively for even & odd pages
        if i > 1
            _tmp = marginOuter
            marginOuter = marginInner
            marginInner = _tmp

        x_adjust = ((pageWidth - marginInner - marginOuter) - (col_count - 1) * gridSize) / 2
        y_adjust = ((pageHeight - marginTop - marginBottom) - (row_count - 1) * gridSize) / 2

        # Draw lines
        lineLength = (pageWidth - marginInner - marginOuter)
        x_offset = marginInner
        y_offset = y_adjust + marginTop - lineWidth / 2

        pdf.setDrawColor(lineColorR, lineColorG, lineColorB)
        for j in [0..row_count]
            isFirstLine = (j == 0)
            isLastLine = (j == row_count - 1)

            y = y_offset + j * gridSize
            isHeaderBottomLine = (j == 2)

            if isFirstLine or isHeaderBottomLine or isLastLine
                pdf.setLineWidth(lineWidth * 2)
            else
                pdf.setLineWidth(lineWidth)

            pdf.line(x_offset, y, x_offset + lineLength, y)

        # Draw dots
        x_offset = x_adjust + marginInner
        y_offset = y_adjust + marginTop - lineWidth / 2

        pdf.setFillColor(dotColorR, dotColorG, dotColorB)

        for j in [0..row_count]
            y = y_offset + j * gridSize

            for k in [0..(col_count - 1)]
                x = x_offset + k * gridSize
                pdf.circle(x, y, dotRadius, 'F')

        if i < pageCount
            pdf.addPage()
    return pdf

for form_input in document.getElementsByTagName("input")
    form_input.onchange = () ->
        pdf = genpdf()
        string = pdf.output('datauristring')
        document.getElementById("iShowPDF").src = string

document.getElementById("btnGeneratePDF").onclick = () ->
    pdf = genpdf()
    window.location.href = pdf.output('datauristring')