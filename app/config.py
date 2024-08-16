class Config:
    SECRET_KEY = 'mysecretkey'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MONGO_URI = 'mongodb+srv://st5282362:ekVMHdrYO6qx85X4@cluster0.s1by6.mongodb.net/task_management'
from .config import Config
print(Config.SECRET_KEY)
