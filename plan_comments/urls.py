from django.urls import path
from plan_comments import views

urlpatterns = [
    path('plan_comments/', views.PlanCommentList.as_view()),
    path('plan_comments/<int:pk>/', views.PlanCommentDetail.as_view())
]
