import cx_Oracle
from dto import * 
import json
import collections

class MemberDAO:
    def meminsert(self, dto):
        # insert into emp01 values (1234, 'test', 200);
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
        cur = conn.cursor()

        try:
            cur.execute("insert into members values (:empno, :ename, :sal)", \
                empno=dto.getEmpno(), ename=dto.getEname(), sal=dto.getSal()) 
            print("------------")
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
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()

            try:
                cur.execute("select * from questions") 
                rows = cur.fetchall()

                v = []
                for row in rows:
                    d = collections.OrderedDict()
                    d['empno'] = row[0]
                    d['ename'] = row[1]
                    d['sal'] = row[2]
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

