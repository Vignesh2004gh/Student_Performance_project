from django import forms

class StudentForm(forms.Form):
    age = forms.IntegerField(label="Age")
    studytime = forms.IntegerField(label="Weekly Study Time (1–4)")
    failures = forms.IntegerField(label="Past Failures")
    absences = forms.IntegerField(label="Absences")
    G1 = forms.IntegerField(label="First Period Grade (0-20)")
    G2 = forms.IntegerField(label="Second Period Grade (0-20)")
