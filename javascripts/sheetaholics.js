(function() {
  var clickBtnGenPdf, ePreviewPDF, fillConfigIntoForm, form_input, form_select, genpdf, isBrowser, isMobile, loadConfigFromForm, updatePreview, _i, _j, _len, _len1, _ref, _ref1;

  fillConfigIntoForm = function(config) {
    var option, _i, _len, _ref, _results;

    if (config == null) {
      config = {
        gridSize: 8,
        dotColor: '000000',
        dotDiameter: 0.4,
        lineColor: '000000',
        lineWidth: 0.2,
        marginInner: 20,
        marginOuter: 15,
        marginTop: 15,
        marginBottom: 15,
        pageFormat: 'a4',
        pageCount: 2
      };
    }
    document.getElementById('gridSize').value = config['gridSize'];
    document.getElementById('marginInner').value = config['marginInner'];
    document.getElementById('marginOuter').value = config['marginOuter'];
    document.getElementById('marginTop').value = config['marginTop'];
    document.getElementById('marginBottom').value = config['marginBottom'];
    document.getElementById('dotDiameter').value = config['dotDiameter'];
    document.getElementById('dotColor').value = config['dotColor'];
    document.getElementById('lineWidth').value = config['lineWidth'];
    document.getElementById('lineColor').value = config['lineColor'];
    _ref = document.getElementById('pageFormat').childNodes;
    _results = [];
    for (_i = 0, _len = _ref.length; _i < _len; _i++) {
      option = _ref[_i];
      if (option.value === config['pageFormat'] && option.selected === false) {
        _results.push(option.selected = true);
      } else if (option.value !== config['pageFormat'] && option.selected === true) {
        _results.push(option.selected = false);
      } else {
        _results.push(void 0);
      }
    }
    return _results;
  };

  loadConfigFromForm = function() {
    var config;

    config = {
      gridSize: parseFloat(document.getElementById('gridSize').value),
      marginInner: parseFloat(document.getElementById('marginInner').value),
      marginOuter: parseFloat(document.getElementById('marginOuter').value),
      marginTop: parseFloat(document.getElementById('marginTop').value),
      marginBottom: parseFloat(document.getElementById('marginBottom').value),
      dotDiameter: parseFloat(document.getElementById('dotDiameter').value),
      dotColorR: parseInt(document.getElementById('dotColor').color.rgb[0] * 255),
      dotColorG: parseInt(document.getElementById('dotColor').color.rgb[1] * 255),
      dotColorB: parseInt(document.getElementById('dotColor').color.rgb[2] * 255),
      lineWidth: parseFloat(document.getElementById('lineWidth').value),
      lineColorR: parseInt(document.getElementById('lineColor').color.rgb[0] * 255),
      lineColorG: parseInt(document.getElementById('lineColor').color.rgb[1] * 255),
      lineColorB: parseInt(document.getElementById('lineColor').color.rgb[2] * 255),
      pageFormat: document.getElementById('pageFormat').value
    };
    config['dotRadius'] = config['dotDiameter'] / 2;
    if (config['pageFormat'] === 'a3') {
      config['pageWidth'] = 297;
      config['pageHeight'] = 420;
    } else if (config['pageFormat'] === 'a4') {
      config['pageWidth'] = 210;
      config['pageHeight'] = 297;
    } else if (config['pageFormat'] === 'a5') {
      config['pageWidth'] = 148;
      config['pageHeight'] = 210;
    } else if (config['pageFormat'] === 'letter') {
      config['pageWidth'] = 216;
      config['pageHeight'] = 279;
    } else if (config['pageFormat'] === 'legal') {
      config['pageWidth'] = 216;
      config['pageHeight'] = 356;
    }
    return config;
  };

  genpdf = function(config) {
    var col_count, dotColorB, dotColorG, dotColorR, dotDiameter, dotRadius, gridSize, i, isFirstLine, isLastLine, j, k, lineColorB, lineColorG, lineColorR, lineLength, lineWidth, marginBottom, marginInner, marginOuter, marginTop, pageFormat, pageHeight, pageWidth, pdf, row_count, x, x_adjust, x_offset, y, y_adjust, y_offset, _i, _j, _k, _l, _tmp;

    gridSize = config['gridSize'];
    marginInner = config['marginInner'];
    marginOuter = config['marginOuter'];
    marginTop = config['marginTop'];
    marginBottom = config['marginBottom'];
    dotDiameter = config['dotDiameter'];
    dotRadius = config['dotRadius'];
    dotColorR = config['dotColorR'];
    dotColorG = config['dotColorG'];
    dotColorB = config['dotColorB'];
    lineWidth = config['lineWidth'];
    lineColorR = config['lineColorR'];
    lineColorG = config['lineColorG'];
    lineColorB = config['lineColorB'];
    pageFormat = config['pageFormat'];
    pageWidth = config['pageWidth'];
    pageHeight = config['pageHeight'];
    pdf = new jsPDF('p', 'mm', pageFormat);
    col_count = parseInt(Math.floor((pageWidth - marginInner - marginOuter) / gridSize)) + 1;
    row_count = parseInt(Math.floor((pageHeight - marginTop - marginBottom) / gridSize)) + 1;
    for (i = _i = 1; _i <= 2; i = ++_i) {
      if (i > 1) {
        _tmp = marginOuter;
        marginOuter = marginInner;
        marginInner = _tmp;
      }
      x_adjust = ((pageWidth - marginInner - marginOuter) - (col_count - 1) * gridSize) / 2;
      y_adjust = ((pageHeight - marginTop - marginBottom) - (row_count - 1) * gridSize) / 2;
      if (lineWidth > 0) {
        lineLength = pageWidth - marginInner - marginOuter;
        x_offset = marginInner;
        y_offset = y_adjust + marginTop - lineWidth / 2;
        pdf.setDrawColor(lineColorR, lineColorG, lineColorB);
        for (j = _j = 1; 1 <= row_count ? _j <= row_count : _j >= row_count; j = 1 <= row_count ? ++_j : --_j) {
          isFirstLine = j === 1;
          isLastLine = j === row_count;
          y = y_offset + (j - 1) * gridSize;
          if (isFirstLine || isLastLine) {
            pdf.setLineWidth(lineWidth * 2);
          } else {
            pdf.setLineWidth(lineWidth);
          }
          pdf.line(x_offset, y, x_offset + lineLength, y);
        }
      }
      if (dotRadius > 0) {
        x_offset = x_adjust + marginInner;
        y_offset = y_adjust + marginTop - lineWidth / 2;
        pdf.setFillColor(dotColorR, dotColorG, dotColorB);
        for (j = _k = 1; 1 <= row_count ? _k <= row_count : _k >= row_count; j = 1 <= row_count ? ++_k : --_k) {
          y = y_offset + (j - 1) * gridSize;
          for (k = _l = 1; 1 <= col_count ? _l <= col_count : _l >= col_count; k = 1 <= col_count ? ++_l : --_l) {
            x = x_offset + (k - 1) * gridSize;
            pdf.circle(x, y, dotRadius, 'F');
          }
        }
      }
      if (i < 2) {
        pdf.addPage();
      }
    }
    return pdf;
  };

  isBrowser = {
    firefox: function() {
      return navigator.userAgent.toLowerCase().indexOf("firefox") > -1;
    },
    chrome: function() {
      return navigator.userAgent.toLowerCase().indexOf("chrome") > -1;
    },
    opera: function() {
      return navigator.userAgent.toLowerCase().indexOf("opera") > -1;
    },
    msie: function() {
      return navigator.userAgent.toLowerCase().indexOf("msie") > -1;
    },
    safari: function() {
      return navigator.userAgent.toLowerCase().indexOf("safari") > -1;
    }
  };

  isMobile = {
    Android: function() {
      return navigator.userAgent.match(/Android/i);
    },
    BlackBerry: function() {
      return navigator.userAgent.match(/BlackBerry/i);
    },
    iOS: function() {
      return navigator.userAgent.match(/iPhone|iPad|iPod/i);
    },
    Opera: function() {
      return navigator.userAgent.match(/Opera Mini/i);
    },
    Windows: function() {
      return navigator.userAgent.match(/IEMobile/i);
    },
    any: function() {
      return isMobile.Android() || isMobile.BlackBerry() || isMobile.iOS() || isMobile.Opera() || isMobile.Windows();
    }
  };

  clickBtnGenPdf = function() {
    var pdf;

    pdf = genpdf(loadConfigFromForm());
    return window.location.href = pdf.output('datauristring');
  };

  updatePreview = function() {
    var pdf, string;

    if (document.getElementById("iShowPDF") !== null) {
      pdf = genpdf(loadConfigFromForm());
      string = pdf.output('datauristring');
      return document.getElementById("iShowPDF").src = string;
    }
  };

  document.getElementById("btnGeneratePDF").onclick = clickBtnGenPdf;

  document.getElementById("btnGeneratePDF2").onclick = clickBtnGenPdf;

  if (isMobile.any() || isBrowser.firefox()) {
    ePreviewPDF = document.getElementById("previewPDF");
    ePreviewPDF.parentNode.removeChild(ePreviewPDF);
  } else {
    _ref = document.getElementsByTagName("input");
    for (_i = 0, _len = _ref.length; _i < _len; _i++) {
      form_input = _ref[_i];
      form_input.onchange = updatePreview;
    }
    _ref1 = document.getElementsByTagName("select");
    for (_j = 0, _len1 = _ref1.length; _j < _len1; _j++) {
      form_select = _ref1[_j];
      form_select.onchange = updatePreview;
    }
    window.onload = function() {
      fillConfigIntoForm();
      return updatePreview();
    };
  }

}).call(this);
