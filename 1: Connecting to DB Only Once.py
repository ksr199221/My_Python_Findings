
import pytest
@pytest.fixture(scope="module")
def cursfunc():
 db=MyDB()
 conn=db.connect("server")
 curs=conn.cursor()
 yield curs
 curs.close()
 conn.close()
 print("closing DB")
 
def func1(cursfunc):
 id=cursfunc.execute("select id from sample")
 assert id==123
 
def func2(cursfunc):
 id=cursfunc.execute("select id from sample")
 assert id==456
 
#connection is created only one time
