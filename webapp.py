from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def render_main():
   return render_template('home.html')

@app.route("/response")
def render_response():
    choose = request.args['fav_language']
    if choose == 'Underground Music':
        reply1 = "Underground Music"
    elif choose == 'Todays Top Hits':
        reply1 = "Today's Top Hits"
    else:
        reply1 = "Relevancy does not matter"
        
    reply2 = ""
    choose = request.args.getlist("music1")
    if 'Rock' in choose:
        reply2 = "Black Sabbath, The Kinks, Jimi Hendrix"
    if 'Psychedelic Music' in choose:
        reply2 += "Still Woozy, MGMT, Tame Impala, Glass Animals"
    if 'Rap' in choose:
        reply2 += "Kanye West, J. Cole, Kendrick Lamar, Baby Keem"
    if 'R&B' in choose:
        reply2 += "Solange, Frank Ocean, SZA, Rejjie Snow, Childish Gambino"
    if 'Alternative' in choose:
        reply2 += "Grimes, Alt-J, Joji, Phoebe Bridgers"
    if 'Folk & Acoustic' in choose:
        reply2 += "Flyte, The Lummineers, Half Moon Run"   
    return render_template('page1.html', response1 = reply1, response2=reply2)
    
if __name__=="__main__":
    app.run(debug=True)
