#!/usr/bin/env python3 
# -*- coding=utf-8 -*-

import os 
import sqlite3

dbfile=os.path.join(os.path.dirname(__file__),'sql.db')
if os.path.isfile(dbfile):
    os.remove(dbfile)

conn=sqlite3.connect(dbfile)
cursor=conn.cursor()
cursor.execute('create table classes(id bigint primary key,name varchar(10))')
cursor.execute(r"insert into classes values (1,'一班')")
cursor.execute(r"insert into classes values (2,'二班')")
cursor.execute(r"insert into classes values (3,'三班')")
cursor.execute(r"insert into classes values (4,'四班')")

cursor.execute('create table student(id INTEGER PRIMARY KEY AUTOINCREMENT,classes_id bigint,name varchar(10),gender varchar(10),score int)')
cursor.execute(r"insert into student values(1,1,'李一','m','90')")
cursor.execute(r"insert into student(id,classes_id,name,gender,score) values(2,1,'王二','f','96')")
cursor.execute(r"insert into student values(3,1,'张三','m','87'),(4,1,'李四','f','73'),(5,2,'王老五','m','81'),(6,2,'六','f','55'),(7,2,'七','m','85'),(8,3,'八','f','91'),(9,3,'九','m','89'),(10,3,'十','f','85')")
cursor.execute(r"insert into student(classes_id,name,gender,score) values(1,'李十一','f','90')")
conn.commit()
cursor.close()
conn.close()

def get_table(table):
    try:
        conn=sqlite3.connect(dbfile)
        cursor=conn.cursor()
        #cursor.execute('select * from student')
        #cursor.execute('select * from student where score=?;',(table,))
        cursor.execute(f'select * from {table}')
        a=cursor.fetchall()
        #print(a)
        return a
    except sqlite3.ProgrammingError as b:
        raise b
    finally:
        cursor.close()
        conn.close()

def print_table(table,line=None,where=None):
    try:
        conn=sqlite3.connect(dbfile)
        cursor=conn.cursor()

        if where==None and line==None:
            cursor.execute(f'select * from {table}')
        elif where==None:
            cursor.execute(f'select {line} from {table}')
        elif line==None and where.startswith('order'):
            cursor.execute(f'select * from {table} {where}')
        elif line==None:
            cursor.execute(f'select * from {table} where {where}')
        elif where.startswith('order'):
            cursor.execute(f'select {line} from {table} {where}')
        else:
            cursor.execute(f'select {line} from {table} where {where}')
        a=cursor.fetchall()
        for name in a:
            print(name)
        #return a
    except sqlite3.ProgrammingError as b:
        raise b
    finally:
        cursor.close()
        conn.close()

def print_table_curl(curl):
    try:
        conn=sqlite3.connect(dbfile)
        cursor=conn.cursor()
        cursor.execute(f'{curl}')
        a=cursor.fetchall()
        for name in a:
            print(name)
        #return a
    except sqlite3.ProgrammingError as b:
        raise b
    finally:
        cursor.close()
        conn.close()

def commit_table_curl(curl):
    try:
        conn=sqlite3.connect(dbfile)
        cursor=conn.cursor()
        cursor.execute(f'{curl}')
        conn.commit()
    except sqlite3.ProgrammingError as b:
        raise b
    finally:
        cursor.close()
        conn.close()

a=get_table('student')
print(a)
a=get_table('classes')
print(a)
print_table('student')
print_table('classes')
print('tiaojian')
print_table('student',where='score>80')

print('投影')
print_table('student',line='id,score,name')

print_table('student',line='id,score point,name')

print_table('student',line='id,score point,name',where='gender="m"')

print('顺序')
print_table('student',where='order by score')

print_table('student',line='id,score point,name',where='order by score DESC')

print_table_curl('SELECT id,name,gender,score FROM student where classes_id=1 ORDER BY score,gender')

print_table_curl('SELECT * FROM student WHERE classes_id=1 ORDER BY score DESC')

print('分页')
print_table_curl('SELECT * FROM student LIMIT 3 OFFSET 0')

print_table_curl('SELECT * FROM student ORDER BY score LIMIT 3 OFFSET 0')
print_table_curl('SELECT * FROM student ORDER BY score LIMIT 3 OFFSET 2')

print('聚合')
print_table_curl('SELECT count(*) num,SUM(score),AVG(score),MAX(score),MIN(score) FROM student')

print_table_curl('SELECT classes_id,count(*) num,SUM(score),AVG(score),MAX(score),MIN(score) FROM student GROUP BY classes_id')
print_table_curl('SELECT classes_id,count(*) num,SUM(score),AVG(score),MAX(score),MIN(score) FROM student GROUP BY classes_id,gender')

print('多表')
print_table_curl("select * from student s,classes c")

print('连接')
print_table_curl('SELECT * from student s INNER JOIN classes c ON s.classes_id=c.id')

print_table_curl('SELECT * FROM student s RIGHT OUTER JOIN classes c ON s.classes_id=c.id')

print_table_curl('SELECT * FROM student s LEFT OUTER JOIN classes c ON s.classes_id=c.id')


commit_table_curl('INSERT INTO student(classes_id,name,gender,score) values(5,"十二","f",78)')

print_table_curl('SELECT * FROM student s LEFT OUTER JOIN classes c ON s.classes_id=c.id')
print_table_curl('SELECT * FROM student s FULL OUTER JOIN classes c ON s.classes_id=c.id')


commit_table_curl('UPDATE student SET score=score+100')

print_table_curl('SELECT * FROM student s FULL OUTER JOIN classes c ON s.classes_id=c.id')

commit_table_curl('UPDATE student SET score=score+100 where id=12' )

print_table_curl('SELECT * FROM student s FULL OUTER JOIN classes c ON s.classes_id=c.id')

commit_table_curl('DELETE FROM student  where id=12' )
print_table_curl('SELECT * FROM student s FULL OUTER JOIN classes c ON s.classes_id=c.id')

commit_table_curl('DELETE FROM classes' )
print_table_curl('SELECT * FROM student s FULL OUTER JOIN classes c ON s.classes_id=c.id')

# commit_table_curl('REPLACE INTO student ("11","2","lishiyi","m","18")')
commit_table_curl('REPLACE INTO student(classes_id,name,gender,score) values(5,"十二","f",78)')
print_table_curl('SELECT * FROM student s FULL OUTER JOIN classes c ON s.classes_id=c.id')
commit_table_curl('REPLACE INTO student values(13,5,"十二2","f",78)')
print_table_curl('SELECT * FROM student where id >=13')
