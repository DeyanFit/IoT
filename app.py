from flask import Flask, jsonify
import psutil
import datetime

app = Flask(__name__)

# Endpoint to get the time remaining until the battery runs out
@app.route('/battery', methods=['GET'])
def get_battery_time_remaining():
    battery = psutil.sensors_battery()
    if battery.power_plugged:
        return "Charging"
    else:
        remaining_seconds = battery.secsleft
        remaining_time = str(datetime.timedelta(seconds=remaining_seconds))
        return remaining_time

# Endpoint to get information about the current process
@app.route('/process', methods=['GET'])
def get_current_process_info():
    current_process = psutil.Process()
    process_info = {
        "ID": current_process.pid,
        "Name": current_process.name(),
        "Status": current_process.status(),
        "Started": datetime.datetime.fromtimestamp(current_process.create_time()).strftime('%Y-%m-%d %H:%M:%S')
    }
    return jsonify(process_info)

# Endpoint to get CPU usage for each CPU core
@app.route('/cpu', methods=['GET'])
def get_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1, percpu=True)
    return jsonify(cpu_usage)

if __name__ == '__main__':
    app.run(debug=True)
