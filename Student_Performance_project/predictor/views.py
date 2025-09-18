from django.shortcuts import render

# Create your views here.
import joblib
import numpy as np
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import StudentForm

# Load model
model = joblib.load("ml_model/student_model.pkl")

@login_required
def home(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            features = np.array([[data["age"], data["studytime"], data["failures"],
                                  data["absences"], data["G1"], data["G2"]]])
            prediction = model.predict(features)[0]

            # Explanation & Suggestions
            if prediction == 1:
                result = "PASS"
                reason = "Good grades and study habits."
                suggestion = "Keep up the consistent performance."
            else:
                result = "FAIL"
                if data["G1"] < 10 or data["G2"] < 10:
                    reason = "Low internal grades."
                    suggestion = "Focus on improving grades through regular practice."
                elif data["studytime"] < 2:
                    reason = "Insufficient study time."
                    suggestion = "Increase study time to at least 2-3 hours daily."
                elif data["absences"] > 10:
                    reason = "Too many absences."
                    suggestion = "Attend classes regularly to avoid missing lessons."
                else:
                    reason = "Overall weak performance."
                    suggestion = "Seek help from teachers and create a study plan."

            return render(request, "predictor/result.html", {
                "result": result,
                "reason": reason,
                "suggestion": suggestion
            })
    else:
        form = StudentForm()
    return render(request, "predictor/input.html", {"form": form})
