from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from django.utils.translation import activate
from .models import Post, PostCategory, Comment
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
def home(request):
    activate('vi')
    my_date = datetime.now()
    first_news = Post.objects.filter(status=True).last()
    all_records = Post.objects.filter(status=True).all().order_by('-created_at')
    if len(all_records) > 1:
        right_news = all_records[1:6][::-1]
        bottom_news = all_records[:2:-1][:3]
    else:
        right_news = []
        bottom_news = []
        
    all_category = PostCategory.objects.filter(status=True).all()
    post_categories = PostCategory.objects.all()[0:1]
    post_categories2 = PostCategory.objects.all()[2:3]
    # bottom_news = Post.objects.all().order_by('-created_at')[:-7:-1][:3]
    return render(request,'app/home.html', {
        'my_date':my_date, 
        'first_news': first_news,
        'right_news' : right_news, 
        'bottom_news' : bottom_news,
        'all_records': all_records,
        'post_categories': post_categories,
        'post_categories2': post_categories2,
        'all_category': all_category
    })

def detail(request, id):
    post = Post.objects.get(pk = id)
    all_category = PostCategory.objects.all()
    related_posts = Post.objects.filter(post_catalogue=post.post_catalogue, status=True).exclude(pk=id)[:5]
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST['comment']
        parent_comment_id = request.POST.get('parent_comment_id')
        if parent_comment_id:
            parent_comment = Comment.objects.get(pk=parent_comment_id)
            Comment.objects.create(
                post =post,
                name = name,
                email = email,
                comment = comment,
                parent_comment=parent_comment
            )
        else:
            Comment.objects.create(
                post=post,
                name=name,
                email=email,
               comment = comment,
            )
        messages.success(request, 'Bình luận của bạn đã được gửi.')
        return redirect('detail', id=id)
    comments = Comment.objects.filter(post=post, status=True, parent_comment__isnull=True).order_by('-id')
    return render(request,'app/detail.html', {
        'post': post,
        'all_category': all_category,
        'related_posts': related_posts,
        'comments':comments
    })
    
def filter_category(request, category_id):
    category = get_object_or_404(PostCategory, pk=category_id)
    posts = category.post_set.all()  # Lấy danh sách sản phẩm của thể loại
    all_category = PostCategory.objects.all()
    new_posts = Post.objects.all().order_by('-created_at')
    
    context = {'category': category,'all_category': all_category, 'posts': posts, 'new_posts': new_posts}
    return render(request, 'app/filter_category.html', context)

def search_results(request):
    if 'q' in request.GET:
        q = request.GET['q']
        posts = Post.objects.filter(name__icontains=q)
    else:
        return render(request, 'app/search_results.html')
    
    return render(request, 'app/search_results.html', {'posts':posts })
    

    # if not query:
    #     return render(request, 'app/search_results.html')

    # # Tìm kiếm các bài viết có tên gần giống hoặc thuộc thể loại gần giống
    # posts = Post.objects.filter(
    #     Q(name__icontains=query) |
    #     Q(post_catalogue__title__icontains=query)  # Sử dụng trường 'title' của thể loại
    # ).distinct()

    # # Tìm kiếm các thể loại gần giống
    # categories = PostCategory.objects.filter(title__icontains=query)

    # context = {
    #     'query': query,
    #     'posts': posts,
    #     'categories': categories,
    # }

    return render(request, 'app/search_results.html', context)






def about(request):
    context={}
    return render(request,'app/about.html', context)

def category(request):
    context={}
    return render(request,'app/category.html', context)

def latestNews(request):
    context={}
    return render(request,'app/latestNews.html', context)

def contact(request):
    context={}
    return render(request,'app/contact.html', context)