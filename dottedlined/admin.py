from dottedlined.models import Log
from django.contrib import admin

class LogAdmin(admin.ModelAdmin):
    list_display = ('date_time', 'remote_addr', 'grid_size', 'dot_color', 'dot_diameter', 'line_color', 'line_width', 'margin_inner', 'margin_outer', 'margin_top', 'margin_bottom', 'page_size', 'page_count')
    date_hierarchy = 'date_time'
    list_filter = ['date_time', 'remote_addr', 'query_string']
admin.site.register(Log, LogAdmin)
