from django.urls import path
from .views import create_email_draft

urlpatterns = [
    path('email_drafts/', create_email_draft, name='create_email_draft'),
]
