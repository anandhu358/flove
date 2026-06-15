from django.shortcuts import render

def home(request):
    return render(request, 'love/index.html')

def story(request):
    return render(request, 'love/story.html')

def gallery(request):
    return render(request, 'love/gallery.html')

def reasons(request):
    return render(request, 'love/reasons.html')

def secret(request):
    return render(request, 'love/secret.html')

def first_chat(request):
    return render(request, 'love/fchat.html')

def first_call(request):
    return render(request, 'love/fcall.html')

def first_date(request):
    return render(request, 'love/fdate.html')

def favorite_memory(request):
    return render(request, 'love/fmem.html')

def counter(request):
    return render(request, 'love/counter.html')

def lock(request):
    return render(request, 'love/lock.html')