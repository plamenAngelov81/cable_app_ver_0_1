from django import forms

from cable_app_0_1.cable.models import Cable, Machine, Cap, Clutch, Inductor


class CableCreateForm(forms.ModelForm):
    class Meta:
        model = Cable
        fields = '__all__'


class MachineCreateForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = '__all__'


class CapCreateForm(forms.ModelForm):
    class Meta:
        model = Cap
        fields = '__all__'


class ClutchCreateForm(forms.ModelForm):
    class Meta:
        model = Clutch
        fields = '__all__'


class InductorCreateForm(forms.ModelForm):
    class Meta:
        model = Inductor
        fields = '__all__'
