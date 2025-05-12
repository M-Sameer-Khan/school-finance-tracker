import logging
from app import app, db

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='server.log')

def start_server():
    try:
        print('Starting School Finance Tracker...')
        print('To log in, use the credentials in the README')
        print('Navigate to http://127.0.0.1:5000 in your web browser')
        
        # Ensure database is created
        with app.app_context():
            db.create_all()
        
        # Start the application
        app.run(debug=True, host='0.0.0.0', port=5000)
    except Exception as e:
        logging.error(f'Server startup error: {e}', exc_info=True)
        print(f'Error starting server: {e}')

if __name__ == '__main__':
    start_server()
