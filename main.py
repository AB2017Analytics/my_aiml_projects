from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "My first flask app on GCP"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug = True)

# from flask import Flask
# import logging

# app = Flask(__name__)

# # Set up basic logging
# logging.basicConfig(level=logging.INFO)
# @app.route('/')
# def home():
#     app.logger.info("Home endpoint accessed")
#     return "Hello, GCP App Engine!"

# if __name__ == '__main__':
#     try:
#         app.logger.info("Starting Flask app")
#         app.run(host="0.0.0.0", port=8080, debug=True)
#     except Exception as e:
#         app.logger.error(f"Error starting app: {e}")
