from django import forms

class Predict(forms.Form):
	sales = forms.FloatField(label="Target Sales Count",widget=forms.NumberInput(attrs={'placeholder':'Sales','style': 'width: 250px;', 'class': 'form-control'}),initial=0)
	weight = forms.FloatField(label="Weight",widget=forms.NumberInput(attrs={'placeholder':'Weight','style': 'width: 250px;', 'class': 'form-control'}),initial=0)
	resolution = forms.FloatField(label="Resolution",widget=forms.NumberInput(attrs={'placeholder':'Resolution','style': 'width: 250px;', 'class': 'form-control'}),initial=0)
	ppi = forms.FloatField(label="Pixel Per Inch(PPI)",widget=forms.NumberInput(attrs={'placeholder':'PPI','style': 'width: 250px;', 'class': 'form-control'}),initial=0)
	cpuCore = forms.FloatField(label="CPU Core",widget=forms.NumberInput(attrs={'placeholder':'CPU Core','style': 'width: 250px;', 'class': 'form-control'}),initial=0)
	cpuFrequency = forms.FloatField(label="CPU Frequency",widget=forms.NumberInput(attrs={'placeholder':'CPU Frequency','style': 'width: 250px;', 'class': 'form-control'}),initial=0)
	memory = forms.FloatField(label="Memory",widget=forms.NumberInput(attrs={'placeholder':'Memory','style': 'width: 250px;', 'class': 'form-control'}),initial=0)
	ram = forms.FloatField(label="RAM",widget=forms.NumberInput(attrs={'placeholder':'RAM','style': 'width: 250px;', 'class': 'form-control'}),initial=0)
	rearCam = forms.FloatField(label="Rear Camera",widget=forms.NumberInput(attrs={'placeholder':'Rear Cam','style': 'width: 250px;', 'class': 'form-control'}),initial=0)
	frontCam = forms.FloatField(label="Front Camera",widget=forms.NumberInput(attrs={'placeholder':'Front Cam','style': 'width: 250px;', 'class': 'form-control'}),initial=0)
	battery = forms.FloatField(label="Battery",widget=forms.NumberInput(attrs={'placeholder':'Battery','style': 'width: 250px;', 'class': 'form-control'}),initial=0)
	thickness = forms.FloatField(label="Thickness",widget=forms.NumberInput(attrs={'placeholder':'Thickness','style': 'width: 250px;', 'class': 'form-control'}),initial=0)