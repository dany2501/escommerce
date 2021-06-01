from app import app
from flask_cors import CORS

if __name__ == "__main__":
    CORS(app, resources={r'/*':{"origins":"*"}})
    app.run(debug = True, host="localhost", port=5001,use_reloader=True)