from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/proxy')
def proxy():
  # Get the target URL from the form submission
  url = request.args.get('url')

  # Make a request to the target URL and retrieve the content
  r = requests.get(url)
  content = r.text

  # Render the content in a template using the material dark theme
  return render_template('proxy.html', content=content, theme='dark')

if __name__ == '__main__':
  app.run()
