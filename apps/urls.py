from django.urls import path, include

urlpatterns = [
    path('book/', include('books.urls')),
    path('user/', include('users.urls')),
]
