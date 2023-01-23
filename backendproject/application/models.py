from django.db import models

# Create your models here.
class Officeuse(models.Model):
    

    Projects = models.CharField(max_length=200)
    Epic = models.CharField(max_length=200)
    Role_Name	 = models.TextField()    
    what = models.TextField()
    why = models.TextField()
    Table_Name = models.CharField(max_length=500)
    Purpose = models.TextField()
    CRUD_NAME = models.CharField(max_length=500)
        #IntegerField(default=0,choices=table)
        #IntegerField(choices=PRIORITIES,default=0)
    

class Project(models.Model):
    Project_Name = models.CharField(max_length=150)

class Epic(models.Model):
    Project = models.ForeignKey(Project,on_delete=models.CASCADE)
    Epic =  models.CharField(max_length=150)


class Role(models.Model):
    Project = models.ForeignKey(Project,on_delete=models.CASCADE)
    Role_Name = models.CharField(max_length=150)
    
class User_story(models.Model):
    Project = models.ForeignKey(Project,on_delete=models.CASCADE)
    # Epic = models.ForeignKey(Epic, on_delete=models.CASCADE)
    # Role = models.ForeignKey(Role,on_delete=models.CASCADE)
    User_story = models.TextField()
    
class Table(models.Model):#User_story
   Project = models.ForeignKey(Project,on_delete=models.CASCADE)
   Table_Name = models.CharField(max_length=250)
   Purpose = models.TextField()
    
class userstorytable(models.Model):
    User_Story = models.ForeignKey(User_story,on_delete=models.CASCADE,default=0)
    Table = models.ForeignKey(Table, on_delete=models.CASCADE)
    # crud_create = models.BooleanField(blank=True, null=True,default=0)
    crud = models.CharField(max_length=10,blank=True,null=True,default=0)  

class userstoryepic(models.Model):
    Project = models.ForeignKey(Project,on_delete=models.CASCADE)
    Epic = models.ForeignKey(Epic, on_delete=models.CASCADE)
    User_story = models.ForeignKey(User_story, on_delete=models.CASCADE)
class userstoryrole(models.Model):
    Project = models.ForeignKey(Project,on_delete=models.CASCADE)
    Role = models.ForeignKey(Role, on_delete=models.CASCADE)
    User_story = models.ForeignKey(User_story, on_delete=models.CASCADE)
class device(models.Model):
    Project = models.ForeignKey(Project,on_delete=models.CASCADE)
    User_story = models.ForeignKey(User_story, on_delete=models.CASCADE)
    userstoryepic = models.ForeignKey(userstoryepic, on_delete=models.CASCADE)
    userstoryrole = models.ForeignKey(userstoryrole, on_delete=models.CASCADE)
    Portal = models.CharField(max_length=10,blank=True,default=0)
    website = models.CharField(max_length=10,blank=True,null=True,default=0)
    Application = models.CharField(max_length=20,blank=True,null=True,default=0)
    