from jinja2 import Environment
import requests
import boto3
from string import Template
import json
import htmlmin
import io
import random


def put_S3(filename, filepath):
    s3_bucket = 'picabot'
    s3_folder = 'pagejs'
    # print("++++++++++++\nNow in Put S3 module ...")
    s3 = boto3.resource('s3')
    data = open(filepath + '/' + filename, 'rb')
    s3.Bucket(s3_bucket).put_object(Key=s3_folder + filename, Body=data, CacheControl="max-age=600")
    return


def fetch_data(url, b_json=True):
    print("+++++++++++++\nNow in fetch_data module ...")
    # string s_url
    # boolean b_json whether to return json or text
    user_agents = [
        'Mozilla/5.0 (Linux; Android 7.1.2; HTC 2Q4R100 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
    ]
    headers = {'user-agent': random.choice(user_agents)}
    # print(f"Fetch headers: {headers}")
    r = requests.get(url, headers=headers)
    if b_json:
        return r.json()
    else:
        return r.text


def fetch_css(filename, filepath):
    print("++++++++++\nNow in fetch_css module ...")
    # get CSS from file, minify said css
    css_file = {'input': open(filepath + '/' + filename, 'rb').read()}
    response = requests.post('https://cssminifier.com/raw', data=css_file)
    css = response.text
    return css


def build_template(db):
    print("Building template for DNN")
    # template_data = {"posts": model.get_lineup()}
    html = Environment().from_string(tmpl.core_template).render(data=db)
    html_minified = minify_html(html)
    css = fetch.fetch_css()
    script = Template(tmpl.script_template).substitute(css=css, minified=html_minified)
    script_name = f"{cfg.config['project_name']}_{cfg.config['name']}.js"
    save_file_overwrite(script, script_name)
    page = Template(tmpl.page_template).substitute(css=css, core=html)
    page_name = f"{cfg.config['project_name']}_{cfg.config['name']}_preview.html"
    save_file_overwrite(page, page_name)
    pass


def minify_html(s_html):
    # returns string of minified html
    return htmlmin.minify(s_html, remove_comments=True, remove_empty_space=True)


def save_file_overwrite(s_contents, s_name):
    print("Now in save file module")
    build_directory = 'build'
    with io.open(f"{build_directory}/{s_name}", "w+", encoding='utf8') as file:
        file.write(s_contents)
    print(f"File saved in {build_directory}: {s_name}")
    return












