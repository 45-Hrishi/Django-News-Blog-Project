from django.shortcuts import  render,get_object_or_404
from django.views.generic import DetailView,ListView,CreateView,UpdateView,DeleteView
from .models import Post,Category,Comment
from .forms import PostForm,UpdateForm,CommnetForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
class HomeView(ListView):
    model = Post
    template_name ='home.html'
    ordering = ['-posting_date']

    def get_context_data(self,*args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView,self).get_context_data()
        context['cat_menu'] = cat_menu
        return context


def CategoryView(request,cats):
    category_posts = Post.objects.filter(category=cats.replace("-"," "))
    return render(request,'categories.html',{'cats':cats.replace('-',' '),'category_posts':category_posts})

def LikeView(request,pk):
    post = get_object_or_404(Post ,id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('article-detail',args=[str(pk)]))

def post_likes(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    post_likes = posts.likes.all()
    context = {'post_likes': post_likes,}
    return render(request, 'likes.html', context)

def userposts(request):
    post_by_user = Post.objects.filter(author = request.user)
    return render(request,'userposts.html',{'post_by_user':post_by_user})





class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'

    def get_context_data(self,*args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView,self).get_context_data()

        stuff = get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['cat_menu'] = cat_menu
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'
    #fields = ('title','author','body')

class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    form_class = PostForm
    #fields = ('title','author','body')

class AddCommentView(CreateView):
    model = Comment
    template_name = 'add_comment.html'
    form_class = CommnetForm
    
    success_url=reverse_lazy('home')
    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = UpdateForm
    #fields = ['title','body']

    

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


