from flask import Flask, request
from flask_socketio import SocketIO, send, disconnect
from difflib import get_close_matches
import pandas as pd
import sqlite3
import time
import threading

con = sqlite3.connect("qa.sqlite3")

dataframe = pd.read_sql_query("SELECT question, answer FROM qa_pair", con)