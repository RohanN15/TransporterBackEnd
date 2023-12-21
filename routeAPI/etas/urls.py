from django.urls import path
from etas.views import AppDevClubReviewsView
from etas.views import CreateAppDevClubReview

urlpatterns = [
    path('etas', AppDevClubReviewsView.as_view()),
    path('add_eta', CreateAppDevClubReview.as_view())
]