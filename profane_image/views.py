from django.shortcuts import render
from .models import DemoImage
# Create your views here.
def index(request):
    if request.method == 'POST' and request.FILES['deimg']:
        deimg = request.FILES['deimg']
        latestImage = DemoImage(dimg = deimg)
        latestImage.save()
        print('location = {}'.format(latestImage.dimg.url))
        print('name = {}'.format(latestImage.filename()))
        return render(request, 'profane_image/index.html', {'latestImage': latestImage })
    return render(request, 'profane_image/index.html')