import cx_Oracle
from dto import * 
import json
import collections

class MemberDAO:
    def memid(self):  

        data = ''
        try:
            conn = cx_Oracle.connect(user="MYMATH2", password="1234", dsn="xe")
            cur = conn.cursor()

            try:
                cur.execute("select mid from member")

            except Exception as e:
                print(e) 

        except Exception as e:
            print(e) 

        finally:
            cur.close() 
            conn.close()

        return data

    def meminsert(self, dto):
        # insert into emp01 values (1234, 'test', 200);
        conn = cx_Oracle.connect(user="MYMATH2", password="1234", dsn="xe")
        cur = conn.cursor()

        try:
            cur.execute("insert into members values (:empno, :ename, :sal)", \
                empno=dto.getEmpno(), ename=dto.getEname(), sal=dto.getSal()) 

            conn.commit()
        except Exception as e:
            print(e) 

        finally:
            cur.close() 
            conn.close()



class QuestionDAO:
    def questall(self):  

        data = []
        try:
            conn = cx_Oracle.connect(user="MYMATH2", password="1234", dsn="xe")
            cur = conn.cursor()

            try:
                cur.execute("select qsid, title, mname from questions, members where questions.memno=members.memno") 
                rows = cur.fetchall()

                v = []
                for row in rows:
                    d = collections.OrderedDict()
                    d['qsid'] = row[0]
                    d['title'] = row[1]
                    d['mname'] = row[2]
                    v.append(d)

                data = json.dumps(v, ensure_ascii = False)

            except Exception as e:
                print(e) 

        except Exception as e:
            print(e) 

        finally:
            cur.close() 
            conn.close()

        return data

    def questone(self, qsid):  

        data = ''
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()

            try:
                cur.execute("select * from emp01 where empno=:v", v=empno) 
                row = cur.fetchone() 
                data = '{"ename":"' + row[1] + '", "sal":' + str(row[2]) +'}'

            except Exception as e:
                print(e) 

        except Exception as e:
            print(e) 

        finally:
            cur.close() 
            conn.close()

        return data