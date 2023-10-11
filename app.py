from flask import Flask, render_template
from markupsafe import Markup
import psutil

app = Flask(__name__)

def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)

battery = psutil.sensors_battery()
process = psutil.Process()
title=Markup('Use /battery, /process and /cpu to navigate.<br> Made by Deyan Atanasov')

print("Battery left: ", battery.secsleft)
print("Process: ", process)
print("CPU cores util: ", psutil.cpu_percent(interval=None, percpu=True))

@app.route("/")
def func():
    return render_template("index.html", text=title)

@app.route("/battery", methods=["GET"])
def bat():
    return render_template("index1.html", batteryInfo="Baterry percentage and time left: " + str(battery.percent) + "%, " + str(convertTime(battery.secsleft)))

@app.route("/process", methods=["GET"])
def proc():
    return render_template("index2.html", processInfo="Current process, PID, name, status and time started: " + str(process))

@app.route("/cpu", methods=["GET"])
def cpu():
    return render_template("index3.html", cpuInfo="Cpu usage in % for all cores:" + str(psutil.cpu_percent(interval=None, percpu=True)))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
