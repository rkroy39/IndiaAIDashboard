""" from django.shortcuts import render, redirect
from indiaAI_Dashboard.forms.UserCreationWithRoleForm import UserCreationWithRoleForm

def create_user(request):
    if request.method == 'POST':
        form = UserCreationWithRoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # You can create a simple success page or redirect to home
    else:
        form = UserCreationWithRoleForm()
    return render(request, 'create_user.html', {'form': form}) """