from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from .models import Post
# from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import EmailPostForm
# Create your views here.

# def post_list(request):
#     posts=Post.published.all()
#     return render(request,'blog/post/list.html', {'posts':posts})
#
# def post_detail(request, year, month, day, post):
#     post = get_object_or_404(Post, slug=post,
#                              status='published',
#                              )
#     return render(request, 'blog/post/detail.html', {'post':post})

def home(request):
    return render(request,'blog/post/home.html');

def about(request):
    res=render(request,'blog/post/grid2.html');
    return res;

def contact(request):
    #if this is POST request we need to process the form data
    if request.method == 'POST':
        #create a form instance and populate it with data from the request
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # name = ContactForm.cleaned_data['yourName']
            email = contactForm.cleaned_data['email']
            # process the data in form.cleaned_data as required
            return render(request, 'contact.html', {'form': form})

    else:
        form = ContactForm()

    return render(request, 'grid2.html', {'form': form})

# def get(self,request):
#     template = 'grid2.html';
#     form = HomeForm();
#     return render(request, self.template, {'form': form})

def post_share(request):
    sent = False
    if request.method == 'POST':
        #Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            #Form fields passed validation
            cd = form.cleaned_data
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], )
            return HttpResponseRedirect(request, '/thanks/')
    else:
        form = EmailPostForm()

    return render(request, 'grid2.html', {'form': form })
