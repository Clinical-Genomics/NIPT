# encoding: utf-8
from database import  db
import os
from views import app  
from flask_debugtoolbar import DebugToolbarExtension



def main():
    db.init_app(app)
    app.debug = True
    toolbar = DebugToolbarExtension(app)
    app.run(host='0.0.0.0', port=7072)    

if __name__ == "__main__":
    main()











