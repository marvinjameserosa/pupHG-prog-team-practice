from flask import Flask, render_template, redirect, url_for
import aqms
import time
import threading

app = Flask(__name__)

def update_data():
    while True:
        time.sleep(2)
        try:
            app.config['current_data'] = {
                'temperature': aqms.temperature(),
                'pressure': aqms.pressure(),
                'humidity': aqms.humidity(),
                'gas': aqms.gas(),
                'altitude': aqms.altitude(),
                'tvoc': aqms.tvoc(),
                'eco2': aqms.eco2(),
                'raw_h2': aqms.raw_h2(),
                'raw_ethanol': aqms.raw_ethanol()
            }
        except Exception as e:
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
