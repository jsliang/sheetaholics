// Generated by CoffeeScript 1.4.0
(function() {
  var form_input, genpdf, _i, _len, _ref;

  genpdf = function() {
    var col_count, dotColorB, dotColorG, dotColorR, dotDiameter, dotRadius, gridSize, i, isFirstLine, isHeaderBottomLine, isLastLine, j, k, lineColorB, lineColorG, lineColorR, lineLength, lineWidth, marginBottom, marginInner, marginOuter, marginTop, pageCount, pageFormat, pageHeight, pageWidth, pdf, row_count, x, x_adjust, x_offset, y, y_adjust, y_offset, _i, _j, _k, _l, _ref, _tmp;
    gridSize = parseFloat(document.getElementById('gridSize').value);
    marginInner = parseFloat(document.getElementById('marginInner').value);
    marginOuter = parseFloat(document.getElementById('marginOuter').value);
    marginTop = parseFloat(document.getElementById('marginTop').value);
    marginBottom = parseFloat(document.getElementById('marginBottom').value);
    dotDiameter = parseFloat(document.getElementById('dotDiameter').value);
    dotRadius = dotDiameter / 2;
    dotColorR = parseInt(document.getElementById('dotColor').color.rgb[0] * 255);
    dotColorG = parseInt(document.getElementById('dotColor').color.rgb[1] * 255);
    dotColorB = parseInt(document.getElementById('dotColor').color.rgb[2] * 255);
    lineWidth = parseInt(document.getElementById('lineWidth').value);
    lineColorR = parseInt(document.getElementById('lineColor').color.rgb[0] * 255);
    lineColorG = parseInt(document.getElementById('lineColor').color.rgb[1] * 255);
    lineColorB = parseInt(document.getElementById('lineColor').color.rgb[2] * 255);
    pageFormat = document.getElementById('pageFormat').value;
    pageCount = parseInt(document.getElementById('pageCount').value);
    if (pageFormat === 'a3') {
      pageWidth = 297;
      pageHeight = 420;
    } else if (pageFormat === 'a4') {
      pageWidth = 210;
      pageHeight = 297;
    } else if (pageFormat === 'a5') {
      pageWidth = 148;
      pageHeight = 210;
    } else if (pageFormat === 'letter') {
      pageWidth = 216;
      pageHeight = 279;
    } else if (pageFormat === 'legal') {
      pageWidth = 216;
      pageHeight = 356;
    }
    pdf = new jsPDF('p', 'mm', pageFormat);
    col_count = parseInt(Math.floor((pageWidth - marginInner - marginOuter) / gridSize)) + 1;
    row_count = parseInt(Math.floor((pageHeight - marginTop - marginBottom) / gridSize)) + 1;
    for (i = _i = 1; 1 <= pageCount ? _i <= pageCount : _i >= pageCount; i = 1 <= pageCount ? ++_i : --_i) {
      if (i > 1) {
        _tmp = marginOuter;
        marginOuter = marginInner;
        marginInner = _tmp;
      }
      x_adjust = ((pageWidth - marginInner - marginOuter) - (col_count - 1) * gridSize) / 2;
      y_adjust = ((pageHeight - marginTop - marginBottom) - (row_count - 1) * gridSize) / 2;
      lineLength = pageWidth - marginInner - marginOuter;
      x_offset = marginInner;
      y_offset = y_adjust + marginTop - lineWidth / 2;
      pdf.setDrawColor(lineColorR, lineColorG, lineColorB);
      for (j = _j = 0; 0 <= row_count ? _j <= row_count : _j >= row_count; j = 0 <= row_count ? ++_j : --_j) {
        isFirstLine = j === 0;
        isLastLine = j === row_count - 1;
        y = y_offset + j * gridSize;
        isHeaderBottomLine = j === 2;
        if (isFirstLine || isHeaderBottomLine || isLastLine) {
          pdf.setLineWidth(lineWidth * 2);
        } else {
          pdf.setLineWidth(lineWidth);
        }
        pdf.line(x_offset, y, x_offset + lineLength, y);
      }
      x_offset = x_adjust + marginInner;
      y_offset = y_adjust + marginTop - lineWidth / 2;
      pdf.setFillColor(dotColorR, dotColorG, dotColorB);
      for (j = _k = 0; 0 <= row_count ? _k <= row_count : _k >= row_count; j = 0 <= row_count ? ++_k : --_k) {
        y = y_offset + j * gridSize;
        for (k = _l = 0, _ref = col_count - 1; 0 <= _ref ? _l <= _ref : _l >= _ref; k = 0 <= _ref ? ++_l : --_l) {
          x = x_offset + k * gridSize;
          pdf.circle(x, y, dotRadius, 'F');
        }
      }
      if (i < pageCount) {
        pdf.addPage();
      }
    }
    return pdf;
  };

  _ref = document.getElementsByTagName("input");
  for (_i = 0, _len = _ref.length; _i < _len; _i++) {
    form_input = _ref[_i];
    form_input.onchange = function() {
      var pdf, string;
      pdf = genpdf();
      string = pdf.output('datauristring');
      return document.getElementById("iShowPDF").src = string;
    };
  }

  document.getElementById("btnGeneratePDF").onclick = function() {
    var pdf;
    pdf = genpdf();
    return window.location.href = pdf.output('datauristring');
  };

}).call(this);