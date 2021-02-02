# GotIt

## Setup

- Prereqs: Have Python 3.9.0 & pip installed
- Create venv: `py -3 -m venv .venv`
- Activate venv: `.venv\scripts\activate`
- Download pyaudio wheel file from <https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio>
  - check which version works for you by entering `python` in your command line and seeing what comes up, for me it's "[MSC v.1927 64 bit (AMD64)]"
  - We're on Python 3.9, so it should be "PyAudio‑0.2.11‑cp39‑cp39‑win_amd64.whl" or "PyAudio‑0.2.11‑cp39‑cp39‑win32.whl".
- Install PyAudio: `pip install PyAudio‑0.2.11‑cp39‑cp39‑win[YOUR VERSION HERE]`
- Install requirements: `pip install -r requirements.txt`

## Maintenance

- If you add any new imports, make sure to freeze: `pip freeze > requirements.txt`
