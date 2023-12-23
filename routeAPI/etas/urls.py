from django.urls import path
from etas.views import AppDevClubReviewsView
from etas.views import CreateAppDevClubReview
from etas.views import CreateWalk
from etas.views import CreateBike

urlpatterns = [
    path('etas', AppDevClubReviewsView.as_view()),
    path('add_eta', CreateAppDevClubReview.as_view()),
    path('add_walk', CreateWalk.as_view()),
    path('add_bike', CreateBike.as_view())
]