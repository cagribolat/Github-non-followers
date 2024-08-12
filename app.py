from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

def get_followers(username, token):
    url = f'https://api.github.com/users/{username}/followers'
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return [follower['login'] for follower in response.json()]
    else:
        return []

def get_following(username, token):
    url = f'https://api.github.com/users/{username}/following'
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return [followee['login'] for followee in response.json()]
    else:
        return []

def find_non_followers(following, followers):
    return [user for user in following if user not in followers]

@app.route('/')
def index():
    return render_template('GitHub_Non_Followers.html')

@app.route('/check_non_followers', methods=['POST'])
def check_non_followers():
    data = request.get_json()
    username = data.get('username')
    token = data.get('token')

    if not username or not token:
        return jsonify({'error': 'Username and token are required'}), 400

    try:
        followers = get_followers(username, token)
        following = get_following(username, token)
        non_followers = find_non_followers(following, followers)
        return jsonify({
            'non_followers': non_followers,
            'count': len(non_followers)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
