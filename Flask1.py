from flask import Flask, render_template

webApp = Flask(__name__)

@webApp.route('/') # Decorator
def rootPage():
    return render_template( 'rootPage.html' )

@webApp.route('/menu') # Decorator
def menuPage():
    return 'PACELAB - Menu'

@webApp.route('/menu/<option>') # Decorator
def optionPage(option):
    option = int(option)
    print(type(option))
    return render_template( 'operation.html', optionValue= option )

@webApp.route('/score/<score>') # Decorator
def scorePage(score):
    score = int(score)
    return render_template( 'score.html', scoreValue= score )

if __name__ == '__main__':
    webApp.run( host= '0.0.0.0', port= 8080, debug= True )

