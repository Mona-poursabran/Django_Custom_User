from django.urls import reverse_lazy
from django.urls.base import reverse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Topic , Entry

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'


class TopicsView(LoginRequiredMixin,ListView):
    model = Topic
    template_name = 'learning_log/topiclist.html'
    context_object_name= 'topics_list'

    def get_queryset(self):
        return Topic.objects.filter(owner = self.request.user)


class TopicDetailView(LoginRequiredMixin, DetailView):
    model = Topic
    template_name = 'learning_log/topicdetail.html'

    def get_queryset(self):
        return Topic.objects.filter(owner = self.request.user)
           

class ToipcUpdate(LoginRequiredMixin, UpdateView):
    model = Topic
    template_name = 'learning_log/edit_topic.html'
    success_url = reverse_lazy('topic_list')
    fields = ['topic']


class TopicDelete(LoginRequiredMixin, DeleteView):
    model = Topic
    template_name = 'learning_log/delete_topic.html'
    success_url = reverse_lazy('topic_list')


class TopicCreation(LoginRequiredMixin,CreateView):
    model = Topic
    template_name = 'learning_log/newtopic.html'
    fields = ['topic']

    def form_valid(self, form) :
        form.instance.owner = self.request.user
        return super().form_valid(form)



class NewEntry(LoginRequiredMixin,CreateView):
    model = Entry
    template_name = 'learning_log/newentry.html'
    fields= ['entry']

    def get_success_url(self) -> str:
        pk = self.kwargs['pk']
        return reverse('topic_detail', kwargs={'pk':pk})

    def form_valid(self, form):
        form.instance.topics_id = self.kwargs.get('pk')
        form.instance.owner = self.request.user
        return super().form_valid(form)


class EntryUpdate(LoginRequiredMixin, UpdateView):
    model = Entry
    template_name = 'learning_log/entry_update.html'
    fields = ['entry']

    def get_success_url(self) -> str:
        obj = self.get_object()
        pk = obj.topics.id
        return reverse('topic_detail', kwargs={'pk':pk} )
  


class EntryDelete(LoginRequiredMixin, DeleteView):
    model = Entry
    template_name = 'learning_log/delete_entry.html'

    def get_success_url(self) -> str:
        obj = self.get_object()
        pk = obj.topics.id
        return reverse('topic_detail', kwargs={'pk':pk} )

    



    
