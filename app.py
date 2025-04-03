from flask import Flask, request, jsonify, render_template
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from urllib.parse import urlparse, parse_qs
import re

app = Flask(__name__)

def extract_video_id(youtube_url):
    """Extract the video ID from a YouTube URL"""
    # Handle youtu.be URLs
    if 'youtu.be' in youtube_url:
        return youtube_url.split('/')[-1].split('?')[0]
    
    # Handle youtube.com URLs
    parsed_url = urlparse(youtube_url)
    if 'youtube.com' in parsed_url.netloc:
        if '/watch' in parsed_url.path:
            return parse_qs(parsed_url.query)['v'][0]
        elif '/embed/' in parsed_url.path:
            return parsed_url.path.split('/')[-1]
        elif '/v/' in parsed_url.path:
            return parsed_url.path.split('/')[-1]
    
    # If it's just the ID
    if re.match(r'^[a-zA-Z0-9_-]{11}$', youtube_url):
        return youtube_url
    
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/transcript', methods=['POST'])
def get_transcript():
    data = request.json
    youtube_url = data.get('youtube_url', '')
    
    if not youtube_url:
        return jsonify({'error': 'Please provide a YouTube URL'}), 400
    
    video_id = extract_video_id(youtube_url)
    
    if not video_id:
        return jsonify({'error': 'Could not extract video ID from the URL'}), 400
    
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        
        # Try to get the transcript in the original language first
        try:
            transcript = transcript_list.find_transcript(['en'])
        except NoTranscriptFound:
            # If English is not available, get any available transcript
            transcript = transcript_list.find_transcript([])
        
        transcript_data = transcript.fetch()
        
        # Combine all text parts
        full_transcript = ' '.join([part['text'] for part in transcript_data])
        
        return jsonify({'transcript': full_transcript})
    
    except TranscriptsDisabled:
        return jsonify({'error': 'Transcripts are disabled for this video'}), 404
    except NoTranscriptFound:
        return jsonify({'error': 'No transcript found for this video'}), 404
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
