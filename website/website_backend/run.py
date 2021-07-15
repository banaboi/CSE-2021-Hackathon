from img_storage import app

SQLALCHEMY_TRACK_MODIFICATIONS = True

if __name__ == '__main__':
  app.run(debug=True, use_reloader=False)