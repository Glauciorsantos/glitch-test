import pandas as pd
import warnings
import requests

from flask import Flask, render_template
from datetime import datetime

warnings.filterwarnings("ignore")

app = Flask(__name__)

# Function to get date just one state
# abreviation_state is string with 2 positions
def process_data_one_state(abreviation_state):

    #url
    url = "https://s3-sa-east-1.amazonaws.com/ckan.saude.gov.br/dados-"
    extension = ".csv"

    #Join variables
    full_url = url + abreviation_state + extension

    #pylint(unused-variable)
    #df_data = pd.DataFrame()

    #pylint(unused-variable)
    #df = pd.read_table(full_url, sep = ";", encoding = "iso-8859-1", error_bad_lines=False, engine='python')

     # print(df.shape)
    #df_data = df_data.append(df, ignore_index=True, sort = False)

     # Cleanin Data
    #df_data = df_data.dropna()

    #df_data.to_csv('Dados/data_state.csv', sep=';')

    return full_url



# Function to get data and clear data
def process_data():

    #pylint(unused-variable)
    url = "https://s3-sa-east-1.amazonaws.com/ckan.saude.gov.br/"

    #pylint(unused-variable)
    df_file_name = pd.read_csv("Dados/url_data_file_name.csv")
    
    #pylint(unused-variable)
    lst_result = [x for x in df_file_name['name_data_file']]
    
    #
    for idx in range(len(lst_result)):
        
        #pylint(unused-variable)
        url_file = url+lst_result[idx]

        df = pd.read_csv(url_file, sep = ";",
                         encoding = "iso-8859-1", # quoting=csv.QUOTE_NONE,
                         error_bad_lines=False)

        df_data = df_data.append(df, ignore_index=True, sort = False)
        
    # Cleanin Data
    df_data = df_data.dropna()

    df_data.to_csv('Dados/data.csv', sep=';')

    txt_return = 'Success'

    return txt_return



# Route to index page
@app.route("/")
def index():
    return render_template("index.html", now=datetime.now())

# Route to Exploratory Data Analysis
@app.route("/exploratory/")
def ExploratoryDataAnalysis():
    return render_template("exploratory_data_analysis.html", now=datetime.now())

# Route to train the model.
@app.route("/process")
def process():
    return process_data()

# Route to train the model.
#@app.route("/process_state", methods=['GET'])
@app.route("/process_state/<state>")
def process_state(state):

    #state = requests.get('http://127.0.0.1:5000/process_state/'+'state')
    #return_value = state #
    mss = 'Essa é a url que irá ser processada: ' + process_data_one_state(state)
    return_value = mss

    return return_value


if __name__ == "__main__":
    app.run()