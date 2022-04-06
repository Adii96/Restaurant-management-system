from django.contrib import admin
from .models import Category, Menu, Comments, Table, Reserve, Order, OrderItem

admin.site.register(Category)
admin.site.register(Menu)
# admin.site.register(Comments)
admin.site.register(Table)
admin.site.register(Reserve)

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('title', 'meal', 'text', 'author', 'data_create')
    list_filter = ('meal', 'data_create')
    search_fields = ('title', 'meal', 'text')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
admin.site.register(Order)
admin.site.register(OrderItem)