from flask import Flask, render_template, request
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)  # Start ngrok when app is run

def parse_command(previous_command, current_command):

    ## tvc
    if current_command in ['tvc-0.4', 'TVC-0.4', 'tvc-.4', 'TVC-.4']:
        return 'Successful\nThrust Vector Control -0.4'
    
    ## Hyd1
    elif current_command in ['hyd01on', 'Hyd01on']:
        return 'Successful\nHydraulic 1 activated'
    
    ## Hyd2
    elif current_command in ['hyd02on', 'Hyd02on']:
        return 'Successful\nHydraulic 2 activated'
    
    ## Hyd3
    elif current_command in ['hyd03on', 'Hyd03on']:
        return 'Successful\nHydraulic 3 activated'
    
    ## Hyd4
    elif current_command in ['hyd04on', 'Hyd04on']:
        return 'Successful\nHydraulic 4 activated'
    
    ## Hyd5
    elif current_command in ['hyd05on', 'Hyd05on']:
        return 'Successful\nHydraulic 5 activated'
    
    ## Hyd6
    elif current_command in ['hyd06on', 'Hyd06on']:
        return 'Successful\nHydraulic 6 activated'

    ## Hyd7
    elif current_command in ['hyd07on', 'Hyd07on']:
        return 'Successful\nHydraulic 7 activated'
    


    ## Hyd1off
    elif current_command in ['hyd01off', 'Hyd01off']:
        return 'Successful\nHydraulic 1 off'
    
    ## Hyd2off
    elif current_command in ['hyd02off', 'Hyd02off']:
        return 'Successful\nHydraulic 2 off'
    
    ## Hyd3off
    elif current_command in ['hyd03off', 'Hyd03off']:
        return 'Successful\nHydraulic 3 off'
    
    ## Hyd4off
    elif current_command in ['hyd04off', 'Hyd04off']:
        return 'Successful\nHydraulic 4 off'
    
    ## Hyd5off
    elif current_command in ['hyd05off', 'Hyd05off']:
        return 'Successful\nHydraulic 5 off'
    
    ## Hyd6off
    elif current_command in ['hyd06off', 'Hyd06off']:
        return 'Successful\nHydraulic 6 off'

    ## Hyd7off
    elif current_command in ['hyd07off', 'Hyd07off']:
        return 'Successful\nHydraulic 7 off'
    
    ## Elon
    elif current_command in ['hyd06off', 'Hyd06off']:
        return 'Hi'
    
    ## NOUN
    elif current_command in ['NOUN93-00014', 'noun93-00014']:
        return 'Successful\nCDR 11021\nCMP 10027\nLMP 09024'
    
    ## install
    elif current_command in ['df2.13', 'DF2.13']:
        return 'DreamFlow 2.13a\nInstall DreamFlow 2.13a (Y/N)'
    
    ## install y/Y
    elif current_command in ['y', 'Y']:
        return 'DreamFlow 2.13a is being installed...'
    
    ## install n/N
    elif current_command in ['n', 'N']:
        return 'DreamFlow 2.13a installation aborted'
    
    ## gimbal
    elif current_command in ['g43r2', 'G43R2']:
        return 'Successful\ngimbal 43, rotate 2'

    ## dream
    elif current_command in ['dream', 'Dream']:
        return 'A strange place to be'
    
    ## elon
    elif current_command in ['helloelon', 'HelloElon']:
        return 'Hi'

    ## nightmare
    elif current_command in ['Nightmare', 'nightmare']:
        return 'Did you have a nightmare last night?'
    else:
        return 'Not a valid input'

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/command',methods=['POST'])
def command():
    data = request.form['command']
    return parse_command('', data)

