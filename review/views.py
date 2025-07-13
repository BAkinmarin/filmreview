from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm, ReviewRequestForm
from django.db.models import Q


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
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        print("Received a POST request")
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Success! Thank you for sharing your thoughts! '
                'Your comment will be visible once approved.'
            )

    # Reset Comment Form
    comment_form = CommentForm()

    return render(
        request,
        "review/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


def comment_edit(request, slug, comment_id):
    """
    View to edit comments
    Inspired by Code Institute's Codestar Blog Walkthrough
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error, please try again!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    View to delete comment
    Inspired by Code Institute's Codestar Blog Walkthrough
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS,
                             'Comment, Bye-Bye!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def search_results(request):
    q = request.GET.get('q')
    error_message = None
    results = []

    if q:
        results = Post.objects.filter(title__icontains=q)
    else:
        error_message = "Please enter a search criteria!"

    context = {
        'results': results,
        'q': q,
        'error_message': error_message
    }

    return render(request, 'review/search_results.html', context)


def about(request):
    form = ReviewRequestForm()
    if request.method == 'POST':
        form = ReviewRequestForm(request.POST)

        if form.is_valid():
            return render(request, 'review/about.html', {
                'form': ReviewRequestForm(),  # This resets the form
                'success_message': "Your review request is sent!"
            })
    return render(request, 'review/about.html', {'form': form})
