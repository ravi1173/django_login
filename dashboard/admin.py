from django.contrib import admin
from .models import my_images, Books
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(Books)
class BooksAdmin(ImportExportModelAdmin):
    list_display = ('bookID','title','authors','average_rating','isbn','language_code')


admin.site.register(my_images)