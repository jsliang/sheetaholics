from django.db import models

# Create your models here.
class Log(models.Model):
    query_string = models.CharField(max_length= 512 )
    remote_addr = models.IPAddressField()
    date_time = models.DateTimeField(auto_now = False, auto_now_add = True)

    def get_query_dict(self):
        queries = [ x.split("=") for x in self.query_string.split("&") ]

        return_dict = {}
        for x in queries:
            if len(x) > 1:
                x[1].replace("%23", "#")
                return_dict[x[0]] = x[1]

        return return_dict

    def get_grid_size(self):
        _dict = self.get_query_dict()
        return _dict['gridSize'] if _dict.has_key('gridSize') else ''
    grid_size = property(get_grid_size)

    def get_dot_color(self):
        _dict = self.get_query_dict()
        return _dict['dotColor'].replace("%23", "#") if _dict.has_key('dotColor') else ''
    dot_color = property(get_dot_color)

    def get_dot_diameter(self):
        _dict = self.get_query_dict()
        return _dict['dotDiameter'] if _dict.has_key('dotDiameter') else ''
    dot_diameter = property(get_dot_diameter)

    def get_line_color(self):
        _dict = self.get_query_dict()
        return _dict['lineColor'].replace("%23", "#") if _dict.has_key('lineColor') else ''
    line_color = property(get_line_color)

    def get_line_width(self):
        _dict = self.get_query_dict()
        return _dict['lineWidth'] if _dict.has_key('lineWidth') else ''
    line_width = property(get_line_width)
    
    def get_margin_inner(self):
        _dict = self.get_query_dict()
        return _dict['marginInner'] if _dict.has_key('marginInner') else ''
    margin_inner = property(get_margin_inner)
    
    def get_margin_outer(self):
        _dict = self.get_query_dict()
        return _dict['marginOuter'] if _dict.has_key('marginOuter') else ''
    margin_outer = property(get_margin_outer)
    
    def get_margin_top(self):
        _dict = self.get_query_dict()
        return _dict['marginTop'] if _dict.has_key('marginTop') else ''
    margin_top = property(get_margin_top)
    
    def get_margin_bottom(self):
        _dict = self.get_query_dict()
        return _dict['marginBottom'] if _dict.has_key('marginBottom') else ''
    margin_bottom = property(get_margin_bottom)
    
    def get_page_width(self):
        _dict = self.get_query_dict()
        return _dict['pageWidth'] if _dict.has_key('pageWidth') else ''
    page_width = property(get_page_width)
    
    def get_page_height(self):
        _dict = self.get_query_dict()
        return _dict['pageHeight'] if _dict.has_key('pageHeight') else ''
    page_height = property(get_page_height)

    def get_page_size(self):
        _dict = self.get_query_dict()
        return "%smm x %smm" % (self.page_width, self.page_height)
    page_size = property(get_page_size)
    
    def get_page_count(self):
        _dict = self.get_query_dict()
        return _dict['pageCount'] if _dict.has_key('pageCount') else ''
    page_count = property(get_page_count)


