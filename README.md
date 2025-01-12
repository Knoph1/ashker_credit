# Ashker Crediting Shopping Solution
This repository contains the MVP implementation of Ashker Crediting Shopping Solution.

## Features
- User authentication (Firebase Auth).
- Product catalog with real-time data (Firestore).
- Shopping cart and order management.
- Back-end API (Flask hosted on Heroku).

## Installation
### Back-End
1. Navigate to `backend/`.
2. Install dependencies: `pip install -r requirements.txt`.
3. Create a `.env` file and add your Firebase credentials.
4. Run the server: `python app.py`.

### Front-End
1. Navigate to `frontend/`.
2. Install dependencies: `flutter pub get`.
3. Run the app: `flutter run`.

## Deployment
- Back-End: Deployed to Heroku.
  1. Ensure `Procfile` and `runtime.txt` are correctly configured.
  2. Push the repository to Heroku.

- Front-End: Deployed to Firebase Hosting.
  1. Run `flutter build web`.
  2. Deploy with `firebase deploy`.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.
