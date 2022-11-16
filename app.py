from flask import Flask, render_template
import ntplib
from time import ctime
app = Flask(__name__)
@app.route('/')

def import_time():

    c = ntplib.NTPClient()
    response = c.request('europe.pool.ntp.org', version=3)
    mytime=ctime(response.tx_time)
    print(mytime)  ##  if you want to see the time it displays
    return render_template('index.html', time = mytime)

if __name__ == '__main__':
    app.run()

    