from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponseForbidden
from .models import Post, Comment
from .forms import CommentForm

# News Article view (credit to course material in Readme)


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 4


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        context = {
            "post": post,
            "comments": comments,
            "commented": False,
            "liked": liked,
            "comment_form": CommentForm()
        }
        return render(request, "article.html", context)

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        context = {
            "post": post,
            "comments": comments,
            "commented": True,
            "comment_form": comment_form,
            "liked": liked
        }
        return render(request, "article.html", context)

# Code to Edit comments (credit to course material in Readme)


class EditCommentView(View):
    def get(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        if comment.author != request.user and not request.user.is_superuser:
            return HttpResponseForbidden(
                "You don't have permission to edit this comment."
            )

        form = CommentForm(instance=comment)
        return render(
            request,
            'edit_item.html',
            {
                'form': form,
                'commented': False
            }
        )

    def post(self, request, comment_id, *args, **kwargs):
        comment = get_object_or_404(Comment, id=comment_id)
        if comment.author != request.user and not request.user.is_superuser:
            return HttpResponseForbidden(
                "You don't have permission to edit this comment."
            )

        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid():
            comment_form.save()
            context = {
                "post": comment.post,
                "comments": comment.post.comments.filter
                (approved=True).order_by(
                    "-created_on"
                ),
                "commented": True,
                "comment_form": CommentForm(),
                "liked": comment.post.likes.filter(id=request.user.id).exists()
            }
            return render(request, "article.html", context)
        else:
            return render(
                request,
                'edit_item.html',
                {'form': comment_form, 'commented': False}
            )

# Code for Delete Comment functionality


class DeleteCommentView(View):
    def get(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        if comment.author != request.user and not request.user.is_superuser:
            return HttpResponseForbidden(
                "You don't have permission to delete this comment."
            )

        context = {'comment': comment}
        return render(request, 'delete_item.html', context)

    def post(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        if comment.author != request.user and not request.user.is_superuser:
            return HttpResponseForbidden(
                "You don't have permission to delete this comment."
            )

        comment.delete()
        return redirect('your-success-page-url')


# Code for Like functionality


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class AboutPage(TemplateView):

    template_name = 'about.html'


class ContactPage(TemplateView):

    template_name = 'contact.html'
