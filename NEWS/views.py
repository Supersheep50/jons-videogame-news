from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic import (TemplateView)
from django.http import HttpResponseRedirect
from django.http import HttpResponseForbidden
from .models import Post, Comment
from .forms import CommentForm


# News Artcile view (credit to course material in Readme)


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

        return render(
            request,
            "article.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

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

        return render(
            request,
            "article.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )

# Code to Edit comments (credit to course material in Readme)


class EditCommentView(View):
    def get(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        # Check if the logged-in user is the author of the comment or a superuser.
        # If not, return a forbidden response.
        if comment.author != request.user and not request.user.is_superuser:
            return HttpResponseForbidden("You don't have permission to edit this comment.")
        
        form = CommentForm(instance=comment)
        context = {'form': form, 'commented': False}  
        return render(request, 'edit_item.html', context)

    def post(self, request, comment_id, *args, **kwargs):
        comment = get_object_or_404(Comment, id=comment_id)
        # Repeating the authorization check in the post method to handle form submissions.
        if comment.author != request.user and not request.user.is_superuser:
            return HttpResponseForbidden("You don't have permission to edit this comment.")

        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid():
            # Updating the comment instance without altering the author or other fields.
            # Removed the lines that reset the email and name to the current user,
            # as they should remain unchanged.
            comment = comment_form.save(commit=False)
            comment.save()
            
            context = {
                "post": comment.post,
                "comments": comment.post.comments.filter(approved=True).order_by("-created_on"),
                "commented": True,
                "comment_form": CommentForm(),
                "liked": comment.post.likes.filter(id=request.user.id).exists(),
            }
            return render(request, "article.html", context)
        else:
            context = {'form': comment_form, 'commented': False}  
            return render(request, 'edit_item.html', context)


# Code to Edit comments (credit to tutor support and course material in Readme)


class DeleteCommentView(View):
    def get(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        context = {'comment': comment}
        return render(request, 'delete_item.html', context)

    def post(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        comment.delete()
        context = {'deleted': True}  
        return render(request, 'delete_item.html', context)

        
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


