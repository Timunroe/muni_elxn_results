from flask import Flask, render_template, request, url_for, redirect
import app_utils

app = Flask(__name__)
app.debug = True

apis = {
    'ham': 'https://www.hamilton.ca/municipal-election/media/arearesults.json',
    'burl': 'https://www.burlington.ca/en/elections/results/data/arearesults.json'
}

# Put <script src="https://picabot.s3.amazonaws.com/pagejs/elxn_results.js"></script> in DNN footer
# put <div class="pica-results"></div> in DNN body

data_ham = app_utils.parse_results('arearesults.json')
data_burl = app_utils.parse_results('burl_arearesults.json', city='burlington')
data = {'ham': data_ham, 'burl': data_burl}

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        if request.form['action'] == 'fetch_cp':
            db = model.get_api()
            return render_template('index.html', data=db)
        if request.form['action'] == 'deploy_cp':
            # read file cp.db
            with open('cp.db') as json_data:
                db = json.load(json_data)
            data.build_template(db)
            fetch.put_S3()
            return render_template('index.html', data=db)
        if request.form['action'] == 'fetch_manual':
            return render_template('index.html', data=model.db)
        if request.form['action'] == 'deploy_manual':
            data.build_template(model.db)
            fetch.put_S3()
            return render_template('index.html', data=model.db)
    return render_template('index.html', data=model.db)

    return render_template('index.html', data = data)



