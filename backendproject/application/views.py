import json
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import OfficeuseSerializer,userstorytableSerializer
from rest_framework import status,viewsets
from .models import Officeuse,Project,Epic,User_story,Table,Role, device, userstoryepic, userstoryrole,userstorytable
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

# @api_view(['GET'])
# def taskEpic(request):
# 	tasks = Epic.objects.filter()
# 	abcd = []
# 	for i in Epic.objects.filter():
		
# 		abcd.append(i.Epic)
# 	return Response(abcd)
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
	print("ASS",data)
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
	
@api_view(['POST'])
def taskproject(request):
	data=request.data
	print("ASS",data)
	a = Project(Project_Name=data["Project"])
	a.save()
	print(data["Project"])
	print("aa",a)
	return Response(request.data)

@api_view(['GET'])
def taskListproject(request):
	tasks = Project.objects.filter()
	abcd = []
	for i in Project.objects.filter():
		
		abcd.append(i.Project_Name)
	a=[]
	for element in abcd:
		if element not in a:
			a.append(element)
		
	return Response(a)
	
@api_view(['POST'])
def taskadddetails(request):
	data=request.data
	print("ASS",data)
	a = Project(Project_Name=data["Project"])
	a.save()
	print(data["Project"])
	print("aa",a)

@api_view(['POST'])
def taskaddfull(request):
	data = request.data
	a = Project(Project_Name=data["Projectt"])
	a.save()
	print(data["Projectt"])
	print("aa",a)
	
	b = Epic(Project=a,Epic=request.data["Epicc"])
	b.save()
	print(data["Epicc"])
	print("bb",b)
	c = Role(Project=a,Role_Name=request.data["Rolee"])
	c.save()
	print(data["Rolee"])
	print("cc",c)
	d = User_story(Project=a,User_story=request.data['Userstory'])
	d.save()
	e = userstoryepic(Project=a,Epic=b,User_story=d)
	e.save()
	f = userstoryrole(Project=a,Role=c,User_story=d)
	f.save()

	g = device(Project=a,User_story=d,userstoryepic=e,userstoryrole=f,Portal=request.data['Portal'],website=request.data['website'],Application=request.data['Application'])
	
	print("ture",g.Portal,g.Application,g.website)
	g.save()
	return Response(request.data)

@api_view(['GET'])
def taskListadddetails(request):
	di =[]

	for user in device.objects.filter():
		lis = {"id":user.User_story.Project.id,
		"Projectt" :user.User_story.Project.Project_Name,
		"Userstory":user.User_story.User_story,
		"Epicc":user.userstoryepic.Epic.Epic,
		"Rolee":user.userstoryrole.Role.Role_Name,
		"Portal":user.Portal,
		"website":user.website,
		"Application":user.Application}
		di.append(lis)
	return Response(di)
@api_view(['POST'])	
def taskupd(request):#stillnot using update link in frontend
	datas = request.data
	print("aabcd",datas)
	# a= Project.objects.filter(id=datas["id"])
	# a.update(Project_Name=datas["Projectt"])
	a= Project.objects.filter(id=datas["id"])
	a.update(Project_Name=datas["Projectt"])
	# print("assasa",a)
	b = Epic.objects.filter(Project_id = datas["id"])
	b.update(Epic=datas["Epicc"])
	# print("asas",b)
	c = Role.objects.filter(Project_id = datas["id"])
	c.update(Role_Name=datas["Rolee"])
	d = User_story.objects.filter(Project_id = datas["id"])
	d.update(User_story =datas["Userstory"])
	
	g = device.objects.filter(Project_id = datas["id"])
	g.update(Portal=datas['Portal'],website=datas['website'],Application=datas['Application'])
	return Response(request.data)


@api_view(['GET'])
def taskEpic(request):
	abcd = []
	for i in Epic.objects.filter():
		
		abcd.append(i.Epic)
	a=[]
	for element in abcd:
		if element not in a:
			a.append(element)
	return Response(a)
@api_view(['POST'])
def taskdeletee(request):
	datas = request.data
	
	print("AAAAAA",datas)
	# Table.objects.filter(Project_id=datas).delete()
	Project.objects.filter(id=datas).delete()
	# userstorytable.objects.filter(User_Story__Project_id = datas["id"]).delete()
	# print(userstorytable.objects.filter(User_Story__Project_id = datas["id"]).delete())
	
	return Response('Item succsesfully delete!')
@api_view(['GET'])
def taskfilter(request):
	datas = request.data
	 