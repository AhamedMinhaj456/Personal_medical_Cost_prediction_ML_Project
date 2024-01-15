from django import forms

class MedicalCostForm(forms.Form):
    age = forms.FloatField()
    sex = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female')])
    bmi = forms.FloatField()
    children = forms.IntegerField()
    smoker = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')])
    region = forms.ChoiceField(choices=[('southeast', 'Southeast'), ('southwest', 'Southwest'), ('northeast', 'Northeast'), ('northwest', 'Northwest')])

    def clean(self):
        cleaned_data = super().clean()
        
        # Convert age to float
        cleaned_data['age'] = float(cleaned_data.get('age', 0))

        # Convert children to float
        cleaned_data['children'] = float(cleaned_data.get('children', 0))

        # Convert smoker to float (assuming 'yes' becomes 1 and 'no' becomes 0)
        cleaned_data['smoker'] = float(cleaned_data.get('smoker', 'no') == 'yes')

        # Convert region to float (assigning numeric values based on choices)
        region_mapping = {
            'southeast': 1.0,
            'southwest': 2.0,
            'northeast': 3.0,
            'northwest': 4.0,
        }
        cleaned_data['region'] = region_mapping.get(cleaned_data.get('region', 'southeast'), 0.0)

        return cleaned_data
