from jinja2 import Environment
from string import Template
import htmlmin
import io
import data_templates as tmpl
import app_fetch
import app_model


def parse_results(file, city="hamilton"):
    with open(file, encoding='utf-8-sig') as f:
        data = json.load(f)

    new_results = []
    temp = data['areaResults']

    for item in temp:
        for k,v in item.items():
            new_dict = {}
            new_dict['id'] = k
            new_dict['statistics'] = v['statistics']
            new_dict['results'] = v['contestResults'][0]
            new_dict['race'] = new_dict['results']['contestName']
            new_results.append(new_dict)

    this_object = {'stats': data['statistics'], 'races': new_results}
    # pprint(this_object)
    with open(f'data_{city}.json', 'w') as outfile:
        json.dump(this_object, outfile, sort_keys=True, indent=4)

    return this_object


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


if __name__ == "__main__":
    # call api, update database
    # model.get_new_data()
    # build template
    build_template()
