from django.contrib import admin

from .models import PostCategory, Post, Comment

class AdminPostCatalogy(admin.ModelAdmin):
    list_display=('title','description','order','status','created_at')
    list_editable = ('status',)
    
admin.site.register(PostCategory, AdminPostCatalogy)

class AdminPost(admin.ModelAdmin):
    list_display = ('name', 'post_catalogue', 'status', 'created_at')
    list_editable = ('status',)
    list_per_page = 10  # Số lượng bản ghi hiển thị trên mỗi trang
    search_fields = ['name','url', 'post_catalogue__title']

admin.site.register(Post, AdminPost)

class AdminCommnet(admin.ModelAdmin):
    list_display=('email','comment','post','status','created_at')
admin.site.register(Comment,AdminCommnet)



