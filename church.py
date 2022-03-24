from flask import Flask,render_template
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('index.html')


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/video')
def video_page():
    return render_template('embedded_video.html')


if __name__ == "__main__":
    app.run(debug=True)