import sqlalchemy
from sqlalchemy import Integer, Column, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

print(sqlalchemy.__version__)

engine = sqlalchemy.create_engine('postgresql+psycopg2://postgres:Vfrcbv04@localhost:5432/testdb')
#Создаём движок и конектимся к postgresql
connection = engine.connect()

result = connection.execute("SELECT * FROM person")
for now in result:
    print('first_name', now['first_name'])
result.close() # лучше всегда закрывать, что бы не тратить память
#Способы добавления данных
trans = connection.begin()
try:
    connection.execute("INSERT INTO author(author_id, full_name, rating) VALUES(644, 'Maks', 2)")
    trans.commit()
except:
    trans.rollback() #Если, что-то плохое произошло, то откатываем
    raise

with connection.begin() as trans:
    connection.execute("INSERT INTO author(author_id,full_name, rating) VALUES(241,'Maks',2)")

result = connection.execute("SELECT * FROM author")
for now in result:
    print('full_name', now['full_name'])


Base = declarative_base()


class Author(Base):

    __tablename__ = 'author'

    author_id = Column(Integer, primary_key= True)
    full_name = Column(String)
    rating = Column(Float)


Base.metadata.create_all(engine)

#создаём фабрику для сессий

Session = sessionmaker(bind=engine)
session = Session()
author = Author(author_id=19, full_name='FKJSD', rating=5)
session.add(author)
#session.flush() монжо вызвать, но не обязательно он работает автоматически. Но это не коммит. Всё содержится в памяти
session.commit()

for item in session.query(Author).order_by(Author.rating): #сортировка по рейтингу
    print(item.full_name,' ', item.rating)

print('Separation')

for item in session.query(Author).filter(Author.rating >4): #условие рейтинг больше 4
    print(item.full_name,' ', item.rating)


