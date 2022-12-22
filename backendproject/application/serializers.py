from application.models import Officeuse,Project,Role,User_story,Table,userstorytable
from rest_framework import serializers


class OfficeuseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Officeuse
        #fields = ("Project_name,Epic,Role_Name,what,why,Table_name,Table_Purpose,Table_CRUD")  
        fields = '__all__'
class userstorytableSerializer(serializers.ModelSerializer):
    class Meta:
        model = userstorytable, 
        
        fields = "__all__"
