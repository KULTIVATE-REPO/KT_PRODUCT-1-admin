from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	# path('task-list/', views.taskList, name="task-list"),
	path('task-epic/', views.taskEpic, name="task-detail"),
	# path('task-create/', views.taskCreate, name="task-create"),
	path('task-Role_Name/', views.taskRole_Name, name="task-detail"),
	path('task-Createeeeee/',views.taskCreateeeeee,name="task-Createeeeee"),
	path('task-last/', views.taskListlast, name="task-last"),
	# path('task-update/', views.taskUpdate,name="update"),
	path('task-deleteee/', views.taskdeletee, name="task-deleteee"),
	# path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
	path('task-updateee/', views.taskUpdateee,name="update"),
path('task-project/',views.taskproject,name="task-project"),
path('task-getproject/', views.taskListproject, name="task-getproject"),
path('task-taskaddfull/', views.taskaddfull, name="task-taskaddfull"),
path('task-taskListadddetails/', views.taskListadddetails, name="task-taskListadddetails"),
path('task-taskupd/', views.taskupd, name="task-taskupd")
]
