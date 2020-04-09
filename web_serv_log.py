import os
import sentry_sdk


from bottle import Bottle, run
from sentry_sdk.integrations.bottle import BottleIntegration

print(os.environ.get("SENTRY_DSN"))
sentry_sdk.init(dsn=os.environ.get("SENTRY_DSN"), integrations=[BottleIntegration()])

app = Bottle()

@app.route('/')
def index():
    return "It's works"
@app.route('/success')
def success():
    return "200 OK"

@app.route('/fail')
def fail():
    raise RuntimeError("This is an error!")
    return 

if os.environ.get("APP_LOCATION") == "heroku":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5001)),
        server="gunicorn",
        workers=3,
    )
else:
    app.run(host="localhost", port=8080, debug=True)
