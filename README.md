# Mood-to-Music-Player
Detects your mood from text you type (or a short voice note) and plays a matching playlist from your local music folder.

## Respository Structure
```
mood-to-music-player/
│
├── README.md
├── LICENSE
├── requirements.txt
├── setup.py
├── .gitignore
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── src/
│   ├── __init__.py
│   ├── mood_detector/
│   │   ├── __init__.py
│   │   ├── sentiment_analyzer.py
│   │   └── voice_processor.py
│   ├── music_player/
│   │   ├── __init__.py
│   │   ├── playlist_manager.py
│   │   └── audio_controller.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── file_handler.py
│   └── main.py
│
├── gui/
│   ├── __init__.py
│   ├── main_window.py
│   ├── mood_input_dialog.py
│   └── assets/
│       ├── icons/
│       └── styles/
│           └── style.qss
│
├── models/
│   ├── __init__.py
│   └── mood_mapping.json
│
├── tests/
│   ├── __init__.py
│   ├── test_sentiment_analyzer.py
│   ├── test_playlist_manager.py
│   └── test_audio_controller.py
│
├── docs/
│   ├── installation.md
│   ├── usage.md
│   ├── api_reference.md
│   └── screenshots/
│       ├── main_interface.png
│       └── mood_detection.png
│
├── config/
│   ├── default_config.json
│   └── mood_playlists.json
│
├── scripts/
│   ├── setup_environment.py
│   └── download_models.py
│
└── examples/
    ├── sample_texts.txt
    └── demo.py
```
