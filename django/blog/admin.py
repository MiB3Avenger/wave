from django.contrib import admin

# Register your models here.
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User
#
# class CustomUserAdmin(UserAdmin):
#     # 定义一个方法来删除用户
#     def delete_user(self, request, queryset):
#         for user in queryset:
#             user.delete()
#         self.message_user(request, '用户已成功删除。')
#
#     delete_user.short_description = '删除用户'
#
# # 注册自定义的管理器类
# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)



#后台编辑post功能，测试搜索功能
from .models import Post
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
   list_display = ('title', 'slug', 'author', 'publish', 'status',)
   list_filter = ('status', 'created', 'publish', 'author',)
   search_fields = ('title', 'body',)
   prepopulated_fields = {'slug': ('title',)}
   raw_id_fields = ('author',)
   date_hierarchy = 'publish'
   ordering = ('status', 'publish',)
