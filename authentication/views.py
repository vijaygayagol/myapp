from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
# from .forms import *
from django.contrib import messages
from django.shortcuts import render
# from .forms import UserImageForm
from django.http import HttpResponseRedirect, JsonResponse
import json
from .models import UploadImage

# Create your views here.
def home(request):
    return render(request, 'authentication/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('/login/')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'authentication/register.html', context)



  # Create your views here.*/
# def avatarView(request):
#     if request.method == 'POST':
#         form = UserImageForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#             messages.success(request, f'upload succesfully!')
#             return redirect('core/post_detail.html')
#     else:
#        form = UserImageForm()
#
#
#     context = {'form': form}
#     return render(request, 'core/image_form.html', context)
# def uploadok(request):
#     return HttpResponse(' upload successful')


# Python program to view
# for displaying images

def display_hotel_images(request):
    if request.method == 'GET':
        # getting all the objects of hotel.
        Hotels = UploadImage.objects.all()
        return render(request, 'authentication/post_detail.html',
                       {'hotel_images': Hotels})
def like(request,id):
    currentImage = UploadImage.objects.get(id=id)
    currentUser = request.user

    for i in currentImage.hot.all():
        if i == currentUser:
            currentImage.hot.remove(currentUser)
            break
        else:
            for i in currentImage.n_not.all():
                if i == currentUser:
                    currentImage.n_not.remove(currentUser)
                else:
                    currentImage.hot.add(currentUser)
    return  redirect('hotel_images')

def dislike(request,id):
    currentImage = UploadImage.objects.get(id=id)
    currentUser = request.user

    for i in currentImage.n_not.all():
        if i == currentUser:
            currentImage.n_not.remove(currentUser)
            break
        else:
            for i in currentImage.hot.all():
                if i == currentUser:
                    currentImage.hot.remove(currentUser)
                else:
                    currentImage.n_not.add(currentUser)
    return  redirect('hotel_images')
def followers_count(request,id):
    currentImage = UploadImage.objects.get(id=id)
    currentUser = request.user

    for i in currentImage.follower.all():
        if i == currentUser:
            currentImage.follower.remove(currentUser)
            break
        else:
            for i in currentImage.unfollower.all():
                if i == currentUser:
                    currentImage.unfollower.remove(currentUser)
                else:
                    currentImage.follower.add(currentUser)
    return redirect('hotel_images')
def unfollowers_count(request,id):
    currentImage = UploadImage.objects.get(id=id)
    currentUser = request.user

    for i in currentImage.unfollower.all():
        if i == currentUser:
            currentImage.unfollower.remove(currentUser)
            break
        else:
            for i in currentImage.follower.all():
                if i == currentUser:
                    currentImage.follower.remove(currentUser)
                else:
                    currentImage.unfollower.add(currentUser)
    return redirect('hotel_images')
#
from .foms import Upload
def emp(request):
    if request.method == "POST":
        form = Upload(request.POST)
        print(form)
        if form.is_valid():
            try:
                form.save()
                return redirect('hotel_images')
            except:
                pass
    else:
        form = Upload()
    return render(request, 'authentication/add_detail.html', {'form': form})


