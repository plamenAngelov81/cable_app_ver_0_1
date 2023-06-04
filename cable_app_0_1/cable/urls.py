from django.urls import path, include

from cable_app_0_1.cable.views import IndexView, CableCreateView, CableDetailsView, CableEditView, CableDeleteView, \
    MachineCreateView, MachineDetailsView, CapCreateView, CapDetailsView, ClutchCreateView, ClutchDetailsView, \
    InductorCreateView, InductorDetailsView

urlpatterns = [
    path('', IndexView.as_view(), name='home page'),

    path('cable/', include([
        path('create/', CableCreateView.as_view(), name='cable create'),
        path('details/<int:pk>/', CableDetailsView.as_view(), name='cable details'),
        path('edit/<int:pk>/', CableEditView.as_view(), name='cable edit'),
        path('delete/<int:pk>/', CableDeleteView.as_view(), name='cable delete'),
    ])),

    path('machine/', include([
        path('create/', MachineCreateView.as_view(), name='machine create'),
        path('details/<int:pk>', MachineDetailsView.as_view(), name='machine details'),
    ])),

    path('cap/', include([
        path('create/', CapCreateView.as_view(), name='cap create'),
        path('details/<int:pk>', CapDetailsView.as_view(), name='cap details'),
    ])),

    path('clutch/', include([
        path('create/', ClutchCreateView.as_view(), name='clutch create'),
        path('details/<int:pk>', ClutchDetailsView.as_view(), name='clutch details'),
    ])),

    path('inductor/', include([
        path('create/', InductorCreateView.as_view(), name='inductor create'),
        path('details/<int:pk>', InductorDetailsView.as_view(), name='inductor details'),
    ])),
]
