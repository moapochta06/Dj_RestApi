from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
   path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
   path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
   path('users/', views.UserList.as_view(), name='user-list'),
   path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
   path('auth/', include('rest_framework.urls')),
   path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
   path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)

