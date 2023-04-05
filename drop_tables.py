from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+mysqldb://hbnb_dev:hbnb_dev_pwd@localhost/hbnb_dev_db")
meta = MetaData()
meta.reflect(bind=engine)
meta.drop_all(bind=engine)