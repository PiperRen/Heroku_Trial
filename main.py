# --------------------------------------------------------------- #
# This file is for setting up the web pages for each action
# LTurner, 12.3.22, Setting up the files
# LTurner, 12.4.22, Troubleshooting the files and getting started on adding create page.
# LTurner, 12.5.22, Found the error with the create donations
# LTurner, 12.6.22, Getting the file ready to submit
# --------------------------------------------------------------- #

import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donation, Donor

app = Flask(__name__)


@app.route('/')
def home():
    return redirect(url_for('all'))


@app.route('/donations/')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)


@app.route('/create/', methods=['GET', 'POST'])
def create():
    if request.method == "POST":
        # Getting the instance of donor from the donor table
        donor = Donor.select().where(Donor.name == request.form['name']).get()

        # Finding the donor instance in the donation table
        new_donation = Donation(value=request.form['donation-amt'], donor=donor)
        new_donation.save()
        return redirect(url_for('all'))
    else:
        return render_template('create.jinja2')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)
