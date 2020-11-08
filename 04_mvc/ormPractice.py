from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:root@localhost:3306/TESTDB')
Base = declarative_base()

class Staff(Base):
    __tablename__ = 'Staff'

    ID = Column(String(10), primary_key=True)
    Name = Column(String(45), nullable=False)
    DeptId = Column(String(10), nullable=False)
    Age = Column(Integer, default=None)
    Gender = Column(String(3), default=None)
    Salary = Column(Integer, default=None)
    RecordDt = Column(Date, nullable=False)

    def __repr__(self):
        return "<User(name='%s', record='%s', Salary=%s>" % (self.Name, self.RecordDt, self.Salary)

DBSession = sessionmaker(bind=engine)
session = DBSession()

for r in session.query(Staff):
    # print(r.ID, r.Name, r.Salary, r.RecordDt)
    print(r)

print('=====')

for r in session.query(Staff).filter(Staff.Salary < 50000):
    print(r.ID, r.Name, r.RecordDt)

staff = Staff(ID='009', Name='Allen', DeptId='001', Age=25, Gender='M', Salary=80000, RecordDt='2020-05-01 21:04:52')
print(staff)

session.add_all([staff])
for r in session.query(Staff):
    # print(r.ID, r.Name, r.Salary, r.RecordDt)
    print(r)

# Commit 並關閉 session
session.commit()
session.close()
