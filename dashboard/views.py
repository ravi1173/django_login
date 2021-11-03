from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.core.files.storage import FileSystemStorage
from .models import my_images, Books
from .resources import BooksResource
from tablib import Dataset
import pandas as pd
import os

from .forms import my_image_form
# Create your views here.


def upload_img(request):
    if request.method == "POST":
        img = my_images()
        img.img = request.FILES['image_file']
        img.username = request.POST['username']
        img.user_id = request.user.id
        img.save()
        return render(request, 'form-basic.html')
    else:
        try:
            img_list = my_images.objects.all()
            return render(request, 'form-basic.html', {'img_list':img_list})
        except:
            return render(request, 'form-basic.html')
        
def upload_excel(request):
    if request.method == "POST":
        csv_file = request.FILES['csv_file']
        print(csv_file)
        if csv_file.name.endswith('.csv'):
            savefile = FileSystemStorage()
            name = savefile.save(csv_file.name, csv_file)
            
            d = os.getcwd()
            file_directory = d+'\media\\'+name
            df = pd.read_csv(file_directory)
            
            for i in df.index:
                book_obj = Books()
                book_obj.bookID = df['bookID'][i]
                book_obj.title = df['title'][i]
                book_obj.authors = df['authors'][i]
                book_obj.average_rating = df['average_rating'][i]
                book_obj.isbn = df['isbn'][i]
                book_obj.language_code = df['language_code'][i]
                book_obj.save()
            print('db created')
        
        return render(request, 'basic-table.html')
    
    else:
        excel_obj = Books.objects.all()
        # user_id=request.user.id
        return render(request, 'basic-table.html', {'excel_obj':excel_obj})
    
def index(request):
    return render(request, 'index.html')

def logout(request):
    auth.logout(request)
    print("logged out")
    return redirect("/")
