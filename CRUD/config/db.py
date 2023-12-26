from sqlalchemy import create_engine

# engine=create_engine("mysql+pymysql://root:your_password@localhost:3306/test")
# engine=create_engine("sqlite:///crud.db")
engine = create_engine('mysql+mysqlconnector://root:Him20@12@localhost:3306/test')

conn = engine.connect()

# engine = create_engine('mysql+mysqlconnector://root:Him20@12@localhost/test')
