from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from .forms import ContactForm
from .models import Comment
from django.conf import settings
from django.shortcuts import redirect
from django.contrib import messages
# Create your views here.
class HomerView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['comments']  = Comment.objects.all()[:5]
        
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        message = request.POST.get('message')
        position = request.POST.get('position')
        
        if not name or not message or not position:
            messages.error(request, "All fields are required!")
            return redirect(reverse_lazy('core:index'))
        
        if len(name) > 20:
            messages.error(request, "please use at most 20 characters")
            return redirect(reverse_lazy('core:index'))
        
        if len(message) > 255 and len(position) > 255:
            messages.error(request, "please use at most 255 characters") 
            return redirect(reverse_lazy('core:index'))


        Comment.objects.create(name=name, message=message, position=position)
        messages.success(request, "Tank You for your comment!")
        return redirect(reverse_lazy('core:index'))
    
    


class ContactView(CreateView):
    form_class = ContactForm
    template_name = 'contact.html'

    def form_valid(self,form):
        if form.is_valid():
            messages.success(self.request,'tank you, i will try to contact you shortly')
        else:messages.error(self.request,'something is wrong,try again please')
        return super().form_valid(form)
    
class DirectContact(TemplateView):
    template_name = 'direct_contact.html'




def error_404_view(request, exception):

	# we add the path to the 404.html file
	# here. The name of our HTML file is 404.html
	return render(request, '404.html')
