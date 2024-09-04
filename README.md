# ElevenLabs Text-to-Speech Web Application

This web application allows users to convert text to speech using the ElevenLabs API. It provides a simple and intuitive interface for users to input text and generate high-quality audio output.

## Features

- User-friendly web interface
- Text-to-speech conversion using ElevenLabs API
- Real-time audio playback in the browser
- Responsive design for various screen sizes

## Technologies Used

- Backend: Python with Flask framework
- Frontend: HTML, CSS, and JavaScript
- API: ElevenLabs Text-to-Speech API

## Setup and Installation

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Set up your ElevenLabs API key:
   - Create a `.env` file in the root directory
   - Add your API key: `ELEVENLABS_API_KEY=your_api_key_here`

3. Run the application:
   ```
   python run.py
   ```

4. Open your web browser and navigate to `http://localhost:5000`

## Usage

1. Enter the text you want to convert to speech in the provided text area.
2. Click the "Generate Speech" button.
3. Wait for the audio to be generated (a loading spinner will be displayed).
4. Once generated, the audio will automatically play in the browser.
5. You can replay the audio using the audio controls provided.