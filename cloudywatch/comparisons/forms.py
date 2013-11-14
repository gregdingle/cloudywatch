from django import forms

from .models import Comparison


class ComparisonForm(forms.ModelForm):
    class Meta:
        model = Comparison

    def clean_applications(self):
        apps = self.cleaned_data['applications']
        slug = Comparison.generate_slug(apps)
        if len(apps) < 2:
            raise forms.ValidationError('You should add at least 2 applications.')

        if Comparison.objects.filter(slug=slug).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Comparison with these apps already exists.')

        # qs = Comparison.objects.annotate(total=Count('applications'))
        # for app in apps:
        #     qs = qs.filter(applications=app)
        # qs = qs.filter(total=len(apps))

        # if qs and self.instance not in qs:
        #     raise forms.ValidationError('Comparison with these apps already exists.')

        self.instance.apps = apps
        return apps

