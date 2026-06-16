# JARVIS Voice Assistant

> **⚠️ Windows Only:** This application is designed for Windows systems. System-level features (opening/closing applications) require Windows OS.

A sophisticated AI-powered voice assistant with a modern Streamlit web interface. JARVIS enables users to interact through both text and voice commands, leveraging Google's Gemini API for intelligent responses.

## Features

- **Voice Command Interface**: Speech-to-text and text-to-speech capabilities
- **Modern Web Dashboard**: Responsive Streamlit application with chat history
- **AI-Powered Responses**: Integration with Google Gemini API for intelligent answers
- **Session Management**: Persistent chat history within user sessions
- **Multi-Modal Input**: Support for text input and microphone voice commands

## Prerequisites

- **Windows OS** (Windows 10 or later)
- Python 3.8 or higher
- Google Gemini API key ([Get one here](https://ai.google.dev/))
- Microphone access (for voice features)

## Installation

### Option 1: Automatic Setup (Recommended)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/chethan95155/Jarvis-Voice-And-Text-Assistant.git
   cd Jarvis-Voice-And-Text-Assistant
   ```

2. **Run the setup script:**
   
   **For Command Prompt (cmd):**
   ```bash
   setup_venv.bat
   ```
   
   **For PowerShell:**
   ```powershell
   .\setup_venv.ps1
   ```
   
   This will automatically:
   - Create a virtual environment
   - Activate it
   - Install all dependencies from requirements.txt

3. **Configure API credentials:**
   - Create a `.env` file in the project root:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```
   - Replace `your_api_key_here` with your actual Google Gemini API key

### Option 2: Manual Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/chethan95155/Jarvis-Voice-And-Text-Assistant.git
   cd Jarvis-Voice-And-Text-Assistant
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   
   **For Command Prompt:**
   ```bash
   venv\Scripts\activate.bat
   ```
   
   **For PowerShell:**
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure API credentials:**
   - Create a `.env` file in the project root:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```
   - Replace `your_api_key_here` with your actual Google Gemini API key

## Usage

### Activate Virtual Environment (Required for each session)

Before running the application, activate the virtual environment:

**For Command Prompt:**
```bash
venv\Scripts\activate.bat
```

**For PowerShell:**
```powershell
.\venv\Scripts\Activate.ps1
```

You should see `(venv)` appear in your terminal prompt when activated.

### Launch the Application

```bash
streamlit run App.py
```

The application will open in your default browser at `http://localhost:8501`.

### Supported Commands

- **Search**: `"search [topic]"` - Get AI-powered answers
- **Time**: `"what time is it"` - Get current time
- **Info**: `"what is your name"` - Get assistant information
- **System Control**: `"open [program]"` and `"close [program]"` (local deployment only)

## Project Structure

```
jarvis-voice-assistant/
├── App.py                 # Streamlit frontend application
├── jarvis.py              # Backend logic and command processing
├── requirements.txt       # Python dependencies
├── setup_venv.bat         # Windows batch setup script
├── setup_venv.ps1         # Windows PowerShell setup script
├── venv/                  # Virtual environment (created after setup)
├── .env                   # API keys and configuration (not committed)
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## Architecture

- **Frontend** (`App.py`): Streamlit web interface with chat UI and voice input
- **Backend** (`jarvis.py`): Command processing and Gemini API integration

## Security

- **API Keys**: Stored in `.env` file, never committed to version control
- **Environment Variables**: Loaded at runtime using `python-dotenv`
- `.gitignore` protects sensitive files from accidental commits

## Limitations & Notes

- Voice input requires browser microphone permissions
- System-level program launching (open/close) only works on local deployment
- Cloud deployments may have browser security restrictions on audio

## Troubleshooting

| Issue | Solution |
|-------|----------|
| ModuleNotFoundError: No module named 'dotenv' | Run `pip install python-dotenv` |
| Microphone not working | Check browser permissions and allow microphone access |
| API key errors | Verify GEMINI_API_KEY is correctly set in .env |

## License

MIT License - See LICENSE file for details

## Support

For issues and questions, please open an issue on GitHub.