from django.contrib import admin
from .models import Stock, Tag
from .forms import StockAdminFormView, TagAdminFormView
# Register your models here.


class StockAdminView(admin.ModelAdmin):
    list_display = ['name', 'description', 'date_created', 'last_updated', 'receive_by', 'quantity', 'price', 'total_quantity', 'issue_by']
    form = StockAdminFormView
    list_filter = ['tags_id', 'date_created']
    search_fields = ['name']
    ordering = ['-date_created']
    # actions = [make_published]


class TagAdminView(admin.ModelAdmin):
    list_display = ['name']
    form = TagAdminFormView
    # list_filter = ['name']
    search_fields = ['name']


admin.site.register(Stock, StockAdminView)
admin.site.register(Tag, TagAdminView)

