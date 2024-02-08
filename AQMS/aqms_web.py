from flask import Flask, render_template, redirect, url_for
import aqms
import time
import threading

app = Flask(__name__)

def update_data():
    while True:
        time.sleep(1)
        sensor_data = aqms.sensor_data()
        try:
            app.config['current_data'] = {
                'temperature': sensor_data[0]+'°C',
                'pressure': sensor_data[1]+' hPa',
                'humidity': sensor_data[2]+'%',
                'gas': sensor_data[3],
                'altitude': sensor_data[4] + ' m',
                'tvoc': sensor_data[5] + ' ug/m3',
                'eco2': sensor_data[6],
                'raw_h2': sensor_data[7],
                'raw_ethanol': sensor_data[8]
            }
        except Exception as e:
            print("Error updating data:", e)
            continue
update_thread = threading.Thread(target=update_data)
update_thread.daemon = True
update_thread.start()

@app.route('/')

def index():
    current_data = app.config.get('current_data', {
        'temperature': 'N/A', 
        'pressure': 'N/A',
        'humidity': 'N/A',
        'gas': 'N/A',
        'altitude': 'N/A',
        'tvoc': 'N/A',
        'eco2': 'N/A',
        'raw_h2': 'N/A',
        'raw_ethanol': 'N/A'
        })
    return render_template("index.html", 
        temperature=current_data['temperature'], 
        pressure=current_data['pressure'],
        humidity=current_data['humidity'],
        gas=current_data['gas'],
        altitude=current_data['altitude'],
        tvoc=current_data['tvoc'],
        eco2=current_data['eco2'],
        raw_h2=current_data['raw_h2'],
        raw_ethanol=current_data['raw_ethanol'])
    print("Current Data:", app.config['current_data'])
@app.route('/refresh')
def refresh():
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=False)
