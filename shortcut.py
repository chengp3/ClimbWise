# this file exists because MP shut its API down and throttles every sequential request :(
# the ticks have been pre-downloaded and processed into their own db specific to that user
# this critically skips the step where it takes 60 seconds for to dl tick info
# instead tickdf is loaded right from the db

import sqlite3 as sl
import pandas as pd

con = sl.connect('my-test.db')

tickdf = pd.read_sql('select * from ryan_westby', con, index_col='url')