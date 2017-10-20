from django.contrib.gis import forms
from models import MapImage
from django.contrib.gis.forms.widgets import OSMWidget


class MapImageForm(forms.ModelForm):
	location = forms.PointField(
        widget=
        OSMWidget(
            attrs={
                'default_lat': '18.653238',
                'default_lon': '-72.093788',
                'map_width': 600,
                'map_height': 500
            }
        ))
	class Meta:
		model = MapImage
		fields = ['name', 'image', 'location']