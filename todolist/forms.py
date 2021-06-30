from django import forms 

class TodoListForm(forms.Form):
    text = forms.CharField(max_length=60, 
                           widget=forms.TextInput(
                              attrs={'class': 'form-control','placeholder' : 'Enter todo e.g. Homework', 'aria-label': 'Todo', 'aria-describeby' : 'add-btn'}))