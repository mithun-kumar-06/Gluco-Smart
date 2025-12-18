from flask import Flask, render_template, request, redirect, url_for, Response
from datetime import datetime
import csv
import io

app = Flask(__name__)

# Storage
readings = []

def analyze_glucose(value):
    value = int(value)
    if value < 70:
        return "Hypoglycemia", "⚠️ Danger! Eat 15g sugar.", "danger"
    elif 70 <= value <= 180:
        return "Normal", "✅ Stable.", "success"
    else:
        return "Hyperglycemia", "⚠️ High! Check insulin.", "warning"

def get_trend(current_value):
    """Simple logic to show if glucose is rising or falling"""
    if not readings:
        return "➖" # No previous data
    
    last_value = int(readings[0]['value'])
    diff = int(current_value) - last_value
    
    if diff > 10:
        return "⬆️ Rising"
    elif diff < -10:
        return "⬇️ Falling"
    else:
        return "➡️ Stable"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        glucose_val = request.form.get('glucose')
        # New Feature: Capture user notes (Diet/Meds)
        user_notes = request.form.get('notes') 
        
        if glucose_val:
            status, message, css_class = analyze_glucose(glucose_val)
            trend_icon = get_trend(glucose_val)
            
            new_entry = {
                'value': glucose_val,
                'status': status,
                'message': message,
                'class': css_class,
                'trend': trend_icon,     # New Trend Feature
                'notes': user_notes,     # New Notes Feature
                'time': datetime.now().strftime("%Y-%m-%d %H:%M")
            }
            readings.insert(0, new_entry)
            
        return redirect(url_for('index'))

    return render_template('index.html', readings=readings)

# New Feature: Download Data as CSV
@app.route('/download')
def download_csv():
    # Create a CSV in memory
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['Time', 'Glucose', 'Status', 'Trend', 'Notes']) # Header
    
    for row in readings:
        writer.writerow([row['time'], row['value'], row['status'], row['trend'], row['notes']])
        
    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-disposition": "attachment; filename=glucose_report.csv"}
    )

@app.route('/clear')
def clear():
    readings.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)