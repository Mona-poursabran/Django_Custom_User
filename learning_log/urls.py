from django.urls import path
from .views import *
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('topics/', TopicsView.as_view(), name = 'topic_list'),
    path('topics/<int:pk>/', TopicDetailView.as_view(), name= 'topic_detail'),
    path('topics/<int:pk>/edite/', ToipcUpdate.as_view(), name = 'topic_update'),
    path('topics/<int:pk>/delete/', TopicDelete.as_view(), name= 'topic_delete' ),
    path('topics/new', TopicCreation.as_view(), name='topic_new'),


    path('topics/<int:pk>/entry/', NewEntry.as_view(), name= 'new_entry'),  
    path('topics/update/<int:pk>/', EntryUpdate.as_view(), name="entry_update"),
    path('topics/deleteentry/<int:pk>', EntryDelete.as_view(), name="entry_delete"),
]
