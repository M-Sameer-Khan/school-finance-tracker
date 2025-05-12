from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Create a minimal diagnostic app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'debug-key-123'

@app.route('/')
def home():
    username = session.get('username')
    if username:
        return f'''
        <h1>Logged in successfully!</h1>
        <p>You are logged in as: <strong>{username}</strong></p>
        <p>Session data: {session}</p>
        <a href="/logout">Logout</a>
        '''
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Simple hardcoded authentication for testing
        if username == 'admin' and password == 'SchoolFinance2025!':
            # Set session variable
            session['username'] = username
            flash('Login successful!')
            return redirect(url_for('home'))
        else:
            error = 'Invalid credentials'
    
    return f'''
    <h1>Login</h1>
    {f'<p style="color: red">{error}</p>' if error else ''}
    <form method="POST">
        <div>
            <label>Username:</label>
            <input type="text" name="username" required>
        </div>
        <div style="margin-top: 10px;">
            <label>Password:</label>
            <input type="password" name="password" required>
        </div>
        <div style="margin-top: 20px;">
            <button type="submit">Login</button>
        </div>
    </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, port=5050)
