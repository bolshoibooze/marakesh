from django import forms
import datetime

class DateTextInput(forms.TextInput):
    def render(self, name, value, attrs=None):
        if (type(value) == datetime.date):
          value = value.strftime("%d-%m-%Y")
        if not 'size' in final_attrs:
            final_attrs['size']=10

        return super(DateTextInput, self).render(name, value, attrs)
