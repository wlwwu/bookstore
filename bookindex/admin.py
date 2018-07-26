from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance
# 
# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)

class Authoradmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

admin.site.register(Author, Authoradmin)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
        list_display = ('title', 'author')

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
        list_display = ('book', 'status')




