from django.conf.urls import url, include
from trainmefitapp.models import *
# from django.contrib.auth.models import UserProfile
from rest_framework import routers, serializers, viewsets
 # Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Workout
        fields = ('workout_name', 'workout_id', 'number_of_exercise_in_chest')


 
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'workout', UserViewSet)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

