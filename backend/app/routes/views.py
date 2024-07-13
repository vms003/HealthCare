# Views for rendering UI
from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Example route for rendering a dashboard or homepage
@app.route('/')
def index():
    return render_template('index.html')

# Example route for displaying data analysis results
@app.route('/data_analysis')
def data_analysis():
    data = {
        'message': 'Data analysis results',
        'data': [
            {'label': 'Label 1', 'value': 10},
            {'label': 'Label 2', 'value': 20},
            {'label': 'Label 3', 'value': 30}
        ]
    }
    return render_template('data_analysis.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
