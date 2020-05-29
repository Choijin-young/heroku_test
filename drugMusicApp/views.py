from django.shortcuts import render, redirect, get_object_or_404
from .models import profile, Video #profile은 models.py의 모델명

# Create your views here.
def main(request):
    profiles = profile.objects.all #models.py에서 가지고온(import해온) profile에 있는 모든 객체들을 profiles에 넣는다
    # profiled = get_object_or_404(profile, pk=1)
    # profiled.delete()
    return render(request, 'main.html', {"profiles":profiles}) #그 profiles안에 담은 걸 이곳으로 그대로 value값으로 가지고 와서 "profiles"라는 key에 넣어준다

def want(request):
    name = request.POST['name']
    nick = request.POST['nickname']
    img = request.FILES['photo']
    print(name, nick, img)
    
    field = profile() #profile은 models.py에서부터 import profile를 거쳐서 온거임. 이건models.py에서 만든 뼈대, 
    field.name = name #여기field는 그 뼈대 안을 채우는 내용들
    field.nick = nick
    field.photo = img #여기 name,nick,img는 위에 있는 name,nick,img를 가지고 온 것.
    
    field.save()

    return redirect('/')

def newVideo(request, artist_id): #url상의 artist_id가 이쪽으로 온것
    print(artist_id)
    link = request.POST.get('link')
    video = Video()
    video.link = link
    xrofile = get_object_or_404(profile, pk=artist_id)
    print(link)
    print(xrofile)
    video.profile = xrofile
    video.save()
    return redirect('/')