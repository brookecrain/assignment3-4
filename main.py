# Brooklyn Crain
# Assignment 3&4 STQA
# 4/18/2021
#main.py
# this .py file will manage all the routing for the flask application and will also handle sending the calculated values to the user
from calculator import *
from flask import Flask, render_template, url_for, flash, redirect, request
from forms import retirementForm, BMIForm