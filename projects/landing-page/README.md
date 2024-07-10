# landing-page

## Configuring

- Create virtual environment and install `requirements.txt`
```
$ virtualenv -p python3 env
$ . env/bin/activate
(env) $ pip install -r requirements.txt
```

- `config.py` file is required, should look like:
```
DEBUG = True # or False
HOST = ["0.0.0.0"] # or []
```

## Run

- start service: `zdaemon -p "python app.py" -d -f start`

- stop service: `zdaemon -p "python app.py" stop`

## Template credits

**Dimension by HTML5 UP**
html5up.net | @ajlkn

Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)

- Demo Images: Unsplash (unsplash.com)
- Icons: Font Awesome (fontawesome.io)
- jQuery (jquery.com)
- Responsive Tools (github.com/ajlkn/responsive-tools)
