# views.py

from django.shortcuts import render
from .models import MedicalCostForm
from .utils import load_and_preprocess_data, train_linear_regression, save_model
import numpy as np
import joblib

def predict_medical_cost(request):
    prediction = None

    if request.method == 'POST':
        form = MedicalCostForm(request.POST)
        if form.is_valid():
            # Get user input
            input_data = [
                form.cleaned_data['age'],
                form.cleaned_data['sex'],
                form.cleaned_data['bmi'],
                form.cleaned_data['children'],
                form.cleaned_data['smoker'],
                form.cleaned_data['region']
            ]

            # Load and preprocess the data
            X_train, Y_train = load_and_preprocess_data('insurance.csv')

            # Train the model
            regressor = train_linear_regression(X_train, Y_train)

            # Reshape input data and make a prediction
            input_data_reshaped = np.asarray(input_data).reshape(1, -1)
            prediction = regressor.predict(input_data_reshaped)[0]

            # Save the trained model (optional)
            save_model(regressor)
    else:
        form = MedicalCostForm()

    return render(request, 'predictor/predict_medical_cost.html', {'form': form, 'prediction': prediction})
