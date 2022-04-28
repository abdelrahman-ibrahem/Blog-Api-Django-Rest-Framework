from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter
router = SimpleRouter()

router.register('' , views.PostView , basename="posts"),
# urlpatterns = [ 
#     path('<int:pk>' , views.PostDetailView.as_view() , name="single_post_api"),
#     path('' , views.PostListView.as_view() , name="post_api_list"),
# ]

urlpatterns = router.urls