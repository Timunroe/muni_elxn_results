from flask import Flask, render_template, request, url_for, redirect
import app_utils

app = Flask(__name__)

data = app_utils.parse_results('arearesults.json')

@app.route("/")
def main():
    return render_template('main.html', data = data)

races = {
    '1': 'Mayor',
    '3': 'Ward 1',
    '4': 'Ward 2',
    '5': 'Ward 3',
    '6': 'Ward 4',
    '7': 'Ward 5',
    '8': 'Ward 6',
    '9': 'Ward 7',
    '10': 'Ward 8',
    '11': 'Ward 9',
    '12': 'Ward 10',
    '13': 'Ward 11',
    '14': 'Ward 12',
    '15': 'Ward 13',
    '16': 'Ward 14',
    '17': 'Ward 15',
    '18': 'Trustee, Hamilton-Wentworth District School Board Wards 1 & 2',
    '19': 'Trustee, Hamilton-Wentworth District School Board Ward 3',
    '20': 'Trustee, Hamilton-Wentworth District School Board Ward 4',
    '21': 'Trustee, Hamilton-Wentworth District School Board Ward 5',
    '22': 'Trustee, Hamilton-Wentworth District School Board Ward 6',
    '23': 'Trustee, Hamilton-Wentworth District School Board Ward 7',
    '24': 'Trustee, Hamilton-Wentworth District School Board Wards 8 & 14',
    '25': 'Trustee, Hamilton-Wentworth District School Board Ward 9 & 10',
    '26': 'Trustee, Hamilton-Wentworth District School Board Ward 11 & 12',
    '27': 'Trustee, Hamilton-Wentworth District School Board Ward 13',
    '28': 'Trustee, Hamilton-Wentworth District School Board Ward 15',
    '29': 'Trustee, Hamilton-Wentworth Catholic District School Board Wards 1, 2 & 15',
    '30': 'Trustee, Hamilton-Wentworth Catholic District School Board Wards 3 & 4',
    '31': 'Trustee, Hamilton-Wentworth Catholic District School Board Ward 5',
    '32': 'Trustee, Hamilton-Wentworth Catholic District School Board Ward 6',
    '33': 'Trustee, Hamilton-Wentworth Catholic District School Board Ward 7',
    '34': 'Trustee, Hamilton-Wentworth Catholic District School Board Wards 8 & 14',
    '35': 'Trustee, Hamilton-Wentworth Catholic District School Board Wards 9 & 11',
    '36': 'Trustee, Hamilton-Wentworth Catholic District School Board Ward 10',
    '37': 'Trustee, Hamilton-Wentworth Catholic District School Board Wards 12 & 13',
    '38': 'Trustee, Conseil scolaire catholique MonAvenir - French Catholic'
}

