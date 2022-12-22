import json
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import OfficeuseSerializer,userstorytableSerializer
from rest_framework import status,viewsets
from .models import Officeuse,Project,Epic,User_story,Table,Role,userstorytable
from django.views.decorators.csrf import csrf_exempt
import pandas as pd

# Create your views here.
api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}

	return Response(api_urls)
# @api_view(['GET'])
# def taskList(request):
# 	tasks = Officeuse.objects.all().order_by('-id')
# 	serializer = OfficeuseSerializer(tasks, many=True)
# 	return Response(serializer.data)

@api_view(['GET'])
def taskEpic(request):
	tasks = Epic.objects.filter()
	abcd = []
	for i in Epic.objects.filter():
		
		abcd.append(i.Epic)
	return Response(abcd)
@api_view(['GET'])
def taskRole_Name(request):
	abcd = []
	for i in Role.objects.filter():
		
		abcd.append(i.Role_Name)
	return Response(abcd)

	


# @api_view(['POST'])
# def taskCreate(request):
	
# 	serializer = OfficeuseSerializer(data=request.data)
# 	if serializer.is_valid():
# 		serializer.save()	
# 	return Response(serializer.data)
		


# @api_view(['POST'])	
# def taskUpdate(request):
# 	datas = request.data
# 	a=Officeuse.objects.filter(id=datas["id"])
# 	a.update( Projects = datas["Projects"],
# 						Epic= datas["Epic"],
# 						Role_Name= datas["Role_Name"],
# 						what= datas["what"],
# 						why= datas["why"],
# 						# Table_Name = datas["Table_Name"]
# 						Purpose= datas["Purpose"],
# 						CRUD_NAME= datas["CRUD_NAME"]
# 					)
# 	return Response(request.data)


# @api_view(['DELETE'])
# def taskDelete(request, pk):
# 	task = Officeuse.objects.get(id=pk)
# 	task.delete()

# 	return Response('Item succsesfully delete!')

@api_view(['POST'])
def taskCreateeeeee(request):
	data=request.data
	a = Project(Project_Name=data["Projects"])
	a.save()
	print(data["Projects"])
	print("aa",a)
	
	b = Epic(Project=a,Epic=request.data["Epic"])
	b.save()
	print(data["Epic"])
	print("bb",b)
	c = Role(Project=a,Role_Name=request.data["Role_Name"])
	c.save()
	print(data["Role_Name"])
	print("cc",c)
	d = User_story(Project=a,Epic=b,Role=c,what=request.data['what'],why=request.data['why'])
	
	d.save()
	print(data["what"])
	print(data["why"])
	print("dd",d)
	e = Table(Project=a,Table_Name=request.data["Table_Name"],Purpose = request.data['Purpose'])
	e.save()
	print("ee",e)
	f = userstorytable(User_Story=d,Table=e,crud=request.data['CRUD_NAME'])
	f.save()
	print("f",f)
	print("asasa",request.data)
	return Response(request.data)


# @api_view(['GET'])
# def taskListlast(request):
# 	di ={}

# 	obj = userstorytable.objects.all().values_list("User_Story__Project__id","User_Story.Project.Project_Name",
# 	"user.User_Story.Epic.Epic",
# 	"user.User_Story.Role.Role_Name",
# 	"user.User_Story.what",
# 	"user.User_Story.why",
# 	"user.Table.Table_Name",
# 	"user.Table.Purpose","user.crud")
# 	print(obj,"ooo")
# 	# serializer = userstorytableSerializer(obj, many=True)
# 	# print(serializer,"kk")
# 	# return Response(serializer.data)
# 	column = ["Project__id","Project_Name",
# 	"Epic",
# 	"Role_Name",
# 	"what",
# 	"why",
# 	"Table_Name",
# 	"Purpose","crud"]

# 	userstorytable_df = pd.DataFrame(obj,columns=column)
# 	userstorytable_dict = userstorytable_df.to_dict()


	
# 	print(obj)
# 	return Response(userstorytable_dict)
@api_view(['POST'])
def taskdeletee(request):
	datas = request.data
	
	print("AAAAAA",datas)
	Table.objects.filter(Project_id=datas).delete()
	Project.objects.filter(id=datas).delete()
	# userstorytable.objects.filter(User_Story__Project_id = datas["id"]).delete()
	# print(userstorytable.objects.filter(User_Story__Project_id = datas["id"]).delete())
	
	return Response('Item succsesfully delete!')


@api_view(['GET'])
def taskListlast(request):
	di =[]

	for user in userstorytable.objects.filter():
		lis = {"id":user.User_Story.Project.id, "Projects":user.User_Story.Project.Project_Name,
		"Epic":user.User_Story.Epic.Epic,
		"Role_Name":user.User_Story.Role.Role_Name,
		"what":user.User_Story.what,
		"why":user.User_Story.why,
		"Table_Name":user.Table.Table_Name,
		"Purpose":user.Table.Purpose,"CRUD_NAME":user.crud}
		di.append(lis)
	return Response(di)

@api_view(['POST'])	
def taskUpdateee(request):
	datas = request.data
	a= Project.objects.filter(id=datas["id"])
	a.update(Project_Name=datas["Projects"])
	# print("assasa",a)
	b = Epic.objects.filter(Project_id = datas["id"])
	b.update(Epic=datas["Epic"])
	# print("asas",b)
	c = Role.objects.filter(Project_id = datas["id"])
	c.update(Role_Name=datas["Role_Name"])
	# print("asas",c)
	d = User_story.objects.filter(Project_id = datas["id"])
	d.update(what =datas["what"],
	why =datas["why"],
	)
	# print("asas",d)
	e = userstorytable.objects.filter(User_Story__Project_id = datas["id"])
	e.update(crud =datas["CRUD_NAME"])
	# print("asas",e)
	f = Table.objects.filter(Project_id = datas["id"])
	f.update(Table_Name =datas["Table_Name"],
	Purpose =datas["Purpose"],
	)	
	print("FFFFFF",f)
	return Response(request.data)	


	# userstorytable.objects.filter(id=request.data["id"]).update(User_Story__Project__Project_Name=request["Projects"],
	# 	User_Story__Epic__Epic=request["Epic"],
	# 	User_Story__Role__Role_Name=request["Role_Name"],
	# 	User_Story__what=request["what"],
	# 	User_Story__why=request["why"],
	# 	"Table_Name":user.Table.Table_Name,
	# 	"Purpose":user.Table.Purpose,"CRUD_NAME":user.crud)
	# return Response(request.data)
	
