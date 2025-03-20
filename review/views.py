from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "review/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Display an individual :model:`review.Post`.

    **Context**

    ``review``
        An instance of :model:`review.Post`.

    **Template:**

    :template:`review/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    print('post:', post)

    return render(
        request,
        "review/post_detail.html",
        {"post": post},
    )
