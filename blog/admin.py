from django.contrib import admin

from .models import Author, Post , Tag

class PostAdmin(admin.ModelAdmin):
   
   prepopulated_fields = {"slug": ("title",)}
   list_filter = ("author" ,"tags" , "date", )
   list_display = ("title" ,"date" ,"author" , )


admin.site.register(Post , PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
