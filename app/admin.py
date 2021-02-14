from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Post

admin.site.site_header = 'Admin Panel'

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ('title','content')    
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 5

admin.site.register(Post,PostAdmin)
