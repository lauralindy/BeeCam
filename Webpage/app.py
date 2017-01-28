from flask import Flask, render_template, flash, request, redirect,url_for, session
import database

database.create_table()

import util

app=Flask(_name_)
app.config['SECRET_KEY']= 'bee'

if _name_ == "_main_":
    app.debug = True
