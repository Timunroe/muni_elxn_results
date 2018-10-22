from flask import Flask, render_template, request, url_for, redirect
# import app_utils
# import app_helpers
import app_helpers
import app_utils

# Put <script src="https://picabot.s3.amazonaws.com/pagejs/elxn_results.js"></script> in DNN footer
# put <div class="pica-results"></div> in DNN body

app = Flask(__name__)
app.debug = True

files = {
    'ham': 'arearesults.json',
    'burl': 'burl_arearesults.json'
}
apis = {
    'ham': 'https://www.hamilton.ca/municipal-election/media/arearesults.json',
    'burl': 'https://www.burlington.ca/en/elections/results/data/arearesults.json'
}
# SWITCH!
source = apis


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        if request.form['action'] == 'fetch_ham':
            data_ham = app_helpers.get_data(source['ham'], city='hamilton')
            # return render_template('index.html', data=db)
        if request.form['action'] == 'update_ham':
            pass
            # read file cp.db
            # with open('cp.db') as json_data:
                # db = json.load(json_data)
            # data.build_template(db)
            # fetch.put_S3()
            # return render_template('index.html', data=db)
        if request.form['action'] == 'fetch_burl':
            data_burl = app_helpers.get_data(source['burl'], city='burlington')
            # return render_template('index.html', data=model.db)
        if request.form['action'] == 'update_burl':
            pass
            # data.build_template(model.db)
            # fetch.put_S3()
            # return render_template('index.html', data=model.db)
    data_ham = app_helpers.get_data(source['ham'], city='hamilton')
    data_burl = app_helpers.get_data(source['burl'], city='burlington')
    return render_template('index.html', data_ham = data_ham, data_burl = data_burl)


# data = fetch.fetch_data(cfg.config['api'])

# with io.open("cp.db", "w+", encoding='utf8') as file:
    # file.write(json.dumps(db, ensure_ascii=False))
