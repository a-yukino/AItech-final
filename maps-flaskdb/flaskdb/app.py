# app.py - to run a sample web application on a console
# Copyright (C) 2024 Yasuhiro Hayashi

from flaskdb import app

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
