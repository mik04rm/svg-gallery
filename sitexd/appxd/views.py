from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, HttpResponse

from django.urls import reverse
from django.views import generic

from .models import Image, Rectangle, Tag

from django.core.paginator import Paginator

# Create your views here.


# def index(request):
#     image_list = Image.objects.all()
#     context = {'image_list': image_list}
#     return render(request, 'appxd/index.html', context)

# class ImageListView(generic.ListView):
#     paginate_by = 3
#     model = Image
#     template_name = "appxd/index.html"


def index(request):
    images = Image.objects.all()
    
    # Filtering by tags
    tag = request.GET.get('tag')
    if tag:
        images = images.filter(tags__name=tag)
    
    # Sorting
    sort = request.GET.get('sort')
    if sort == 'asc':
        images = images.order_by('pub_date')
    elif sort == 'desc':
        images = images.order_by('-pub_date')
    
    # Pagination
    paginator = Paginator(images, 3)  # 3 images per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'tag': tag,
        'sort': sort,
        'tags': Tag.objects.all(),
    }
    return render(request, 'appxd/index.html', context)

class ImageView(generic.DetailView):
    model = Image
    template_name = "appxd/image.html"

def delete_rectangle(request, image_id, rectangle_id):
    image = get_object_or_404(Image, pk=image_id)
    rectangle = get_object_or_404(Rectangle, pk=rectangle_id)

    if rectangle.image == image:
        rectangle.delete()
        return redirect(reverse('appxd:image', args=(image_id,)))
    else:
        raise Http404("the rectangle doesn't belong to the image")
    
def add_rectangle(request, image_id):
    image = get_object_or_404(Image, pk=image_id)

    if request.method == 'POST':
        # get form data from POST request
        try:
            x = int(request.POST.get('x'))
            y = int(request.POST.get('y'))
            width = int(request.POST.get('width'))
            height = int(request.POST.get('height'))
            fill_color = request.POST.get('fill_color')
        except (TypeError, ValueError):
            raise Http404("Invalid input")


        Rectangle.objects.create(
            image=image,
            x=x,
            y=y,
            width=width,
            height=height,
            fill_color=fill_color
        )


    return redirect(reverse('appxd:image', args=(image_id,)))

    # return render(request, 'appxd/image.html', {'image': image})
