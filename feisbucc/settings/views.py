from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserSettings
from .forms import UserSettingsForm

@login_required
def user_settings(request):
    settings, created = UserSettings.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserSettingsForm(request.POST, instance=settings)
        if form.is_valid():
            form.save()
            return redirect('settings')
    else:
        form = UserSettingsForm(instance=settings)
    return render(request, 'settings/settings.html', {'form': form})