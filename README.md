# Pokémon Scanner Service

## Overview
Pokémon Scanner Service is a backend application designed to automate the process of scanning, recognizing, and cropping Pokémon cards from images. This service streamlines the task of digitizing large collections of Pokémon cards by processing images that contain multiple cards, identifying each card, and saving them as individual image files.

## Features
- **Image Upload**: Users can upload images containing multiple Pokémon cards.
- **Card Recognition**: The service automatically detects the boundaries of each Pokémon card in the uploaded images.
- **Image Cropping**: Each identified card is cropped from the main image and saved as a separate file.
- **Easy Integration**: Designed with a simple REST API interface for easy integration with front-end applications or other services.

## Technologies
- Python
- Flask
- OpenCV for image processing

## Getting Started

### Prerequisites
- Python 3.6 or later
- pip and virtualenv

### Installation
1. Clone the repository: https://github.com/andresz74/pokemon-scanner-service.git
2. Navigate to the project directory: `cd pokemon-scanner-service`
3. Create and activate a virtual environment:
- On Windows:
  ```
  python -m venv venv
  .\venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```
4. Install the required dependencies: `pip install -r requirements.txt`

### Running the Application
1. Start the Flask application: `python app.py`
2. The service will be available at `http://localhost:5000`.

## Usage
Provide instructions on how to use the service, including any relevant endpoints and how to format requests.

## Contributing
We welcome contributions! Please read our contributing guidelines (you can include a link to CONTRIBUTING.md here) to learn how to contribute to the project.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Mention any libraries or projects you used in building this application.
- Any individual contributors or organizations that helped with development.

## Contact
For any questions or suggestions, feel free to contact Andres Zenteno at azenteno74@gmail.com.

