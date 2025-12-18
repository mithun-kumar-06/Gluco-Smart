# Gluco-Smart

=========================================================================
PROJECT NAME: GlucoSmart 360 - Intelligent Diabetes Management System
AUTHOR: [Your Name Here]
DATE: December 2025
TYPE: Internship Project / Web Application Prototype
=========================================================================

1. PROJECT OVERVIEW
-------------------
People with diabetes often struggle to interpret raw glucose numbers (e.g., "145 mg/dL") and make immediate lifestyle decisions. 

GlucoSmart is a web-based "Digital Assistant" that acts as an interpretive layer between raw data and the patient. It focuses on reducing cognitive load by converting numbers into actionable advice (e.g., "Eat 15g carbs" or "Levels Stable").

2. KEY FEATURES implemented
---------------------------
[x] Smart Analysis Engine: 
    - Automatically categorizes readings as Hypoglycemia, Normal, or Hyperglycemia.
    - Provides specific medical context advice (e.g., "Drink water" vs "Eat sugar").

[x] Trend Detection: 
    - Compares current reading with previous data to show trend arrows (⬆️ Rising / ⬇️ Falling).

[x] Context Logging:
    - Allows users to add notes (e.g., "Ate Pizza", "Ran 5km") to understand spikes.

[x] Visual Analytics:
    - Integrated Chart.js to display a live line graph of glucose trends over time.

[x] Color-Coded Interface:
    - Rows change color (Red/Green/Yellow) for instant visual status recognition.

[x] Data Export:
    - One-click CSV download to share reports with doctors.

3. TECH STACK
-------------
- Backend: Python (Flask Framework)
- Frontend: HTML5, Bootstrap 5 (for responsive design)
- Visualization: Chart.js (JavaScript library)
- Data Storage: In-memory Python Lists (Prototype version)

4. PREREQUISITES
----------------
- Python 3.x installed
- Pip (Python Package Manager)

5. HOW TO RUN THIS PROJECT
--------------------------
Step 1: Open your terminal/command prompt.
Step 2: Navigate to the project folder.
Step 3: Install the required framework:
        pip install flask

Step 4: Run the application:
        python app.py

Step 5: Open your web browser and go to:
        http://127.0.0.1:5000/

6. PROJECT STRUCTURE
--------------------
GlucoSmart/
│
├── app.py                # Main backend logic (Flask server)
├── README.txt            # Documentation
└── templates/
    └── index.html        # Frontend UI (HTML + Chart.js + Bootstrap)

7. FUTURE SCOPE (Roadmap)
-------------------------
- Integration with IoT Glucometers via Bluetooth for auto-sync.
- User Authentication (Login/Signup) for multi-patient support.
- Machine Learning model to predict hypoglycemia 30 minutes in advance.
- Mobile App version using Flutter.

=========================================================================
