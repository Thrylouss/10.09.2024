from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from . import views

schema_view = get_schema_view(
    openapi.Info(
        title="Project API",
        default_version="v1",
    ),
    public=True,
)

urlpatterns = [
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),

    path("list/", views.PostListView.as_view(), name="ListView"),
    path("create/", views.PostCreateView.as_view(), name="CreateView"),
    path("<int:pk>/detail/", views.PostDetailView.as_view(), name="DetailView"),
    path("<int:pk>/update/", views.PostUpdateView.as_view(), name="UpdateView"),
    path("<int:pk>/destroy/", views.PostDeleteView.as_view(), name="DeleteView"),
]
