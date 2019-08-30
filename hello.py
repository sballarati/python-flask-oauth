from flask import Flask
from flask import redirect, url_for
#, session, request, jsonify, render_template
from authlib.flask.client import OAuth
# for later, try from auth0.v3.authentication import Social

app = Flask(__name__)
app.secret_key = 'a secret key'
oauth = OAuth(app)

#OAuth2 login
oauth.register(
    name='github',
    client_id='YOURGITHUBCLIENTID',
    client_secret='YOURGITHUBSECRET',
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize',
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'user:email'},
)

@app.route("/")
def hello():
    return "Hello, OAuth World!"

@app.route("/worked")
def worked():
    return "Authenticated with GitHub :)"

@app.route('/login')
def login():
    redirect_uri = url_for('authorize', _external=True)
    return oauth.github.authorize_redirect(redirect_uri)

@app.route('/authorize')
def authorize():
    token = oauth.github.authorize_access_token()
    resp = oauth.github.get('user')
    profile = resp.json()
    print(profile)
    # do something with the token and profile
    return redirect('/worked')