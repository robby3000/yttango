# YouTube Transcript Extractor - Setup Guide

This guide will help you set up and run the YouTube Transcript Extractor application.

## Requirements

- Python 3.7+
- pip (Python package installer)

## Local Development Setup

1. **Clone or download the project files to your local machine**

2. **Create and activate a virtual environment (recommended)**
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required packages**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create the directory structure**
   Make sure your project structure looks like this:
   ```
   youtube-transcript-extractor/
   ├── app.py
   ├── requirements.txt
   └── templates/
       └── index.html
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the application**
   Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## Deployment Options

### Deploying to Heroku

1. **Create a Procfile**
   Create a file named `Procfile` (no file extension) in the root directory with:
   ```
   web: gunicorn app:app
   ```

2. **Initialize a Git repository**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

3. **Create a Heroku app and deploy**
   ```bash
   heroku create your-app-name
   git push heroku master
   ```

### Deploying to Vercel

1. **Create a vercel.json file**
   ```json
   {
     "version": 2,
     "builds": [
       {
         "src": "app.py",
         "use": "@vercel/python"
       }
     ],
     "routes": [
       {
         "src": "/(.*)",
         "dest": "app.py"
       }
     ]
   }
   ```

2. **Deploy using Vercel CLI or GitHub integration**

## Usage Instructions

1. Enter a valid YouTube URL in the input field
2. Click the "Extract Transcript" button
3. View the transcript in the results area
4. Use the "Copy to Clipboard" button to copy the transcript

## Troubleshooting

- **No transcript found**: Not all YouTube videos have transcripts available
- **Transcripts disabled**: Some content creators disable transcripts for their videos
- **Invalid URL**: Ensure you're entering a valid YouTube URL

## Further Development

- Add support for selecting specific languages
- Implement auto-translation features
- Add ability to download transcripts as TXT or SRT files
- Implement user authentication for saving favorite transcripts
