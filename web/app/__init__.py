from flask import Flask, render_template, request
import os, smtplib
app = Flask(__name__)
from app import routes