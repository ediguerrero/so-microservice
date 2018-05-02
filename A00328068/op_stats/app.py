from flask import Flask

app = Flask(__name__)

@app.route('/v1/stats/cpu')
def get_cpu_percent():
  cpu_percent = "fajardo presidente :v"
  #return {'cpu_percent': cpu_percent}
  return '{}'.format(cpu_percent)

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=8080)
