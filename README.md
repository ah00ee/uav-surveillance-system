# uav-surveillance-system

### Folder Structure
```
├── app
│   └── main.py
├── static
│   ├── css
│   │   └── main.css
│   └── js
│       └── modal.js
├── templates
│   ├── map.html
│   ├── navbar.html
│   └── streamLive.html
├── .gitignore
└── README.md
``` 

## Start running on localhost 
```
uvicorn app.main:app --reload
```