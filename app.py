from flask import Flask, render_template, request
# import app_utils
# import app_helpers
import app_helpers
import app_utils

# Put <script src="https://picabot.s3.amazonaws.com/pagejs/elxn_results_ham.js"></script> in DNN footer
# put <div class="pica-results"></div> in DNN body

app = Flask(__name__)
app.debug = True


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        print("Method is POST!")
        if request.form['action'] == 'fetch_ham':
            data_ham = app_helpers.get_data(app_helpers.source['ham'], city='hamilton')
        if request.form['action'] == 'deploy_ham':
            print("!!! In deploy_ham module:")
            build_name = app_utils.build_template('ham')
            app_utils.put_S3(build_name, './build')
            # return render_template('index.html', data=db)
        if request.form['action'] == 'fetch_burl':
            data_burl = app_helpers.get_data(app_helpers.source['burl'], city='burlington')
            # return render_template('index.html', data=model.db)
        if request.form['action'] == 'deploy_burl':
            build_name = app_utils.build_template('burl')
            app_utils.put_S3(build_name, './build')
            # return render_template('index.html', data=db)
    data_ham = app_helpers.get_input(app_helpers.files_saved['ham'])
    data_burl = app_helpers.get_input(app_helpers.files_saved['burl'])
    return render_template('index.html', data_ham=data_ham, data_burl=data_burl)
