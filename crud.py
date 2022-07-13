from datetime import date
from optparse import Values
from bson import re
from flask import Flask, render_template, request, jsonify
from matplotlib.pyplot import table
import mysql.connector as connection
import pandas as pd
from pkg_resources import safe_version
from zmq import NULL
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    return render_template('index.html')
@app.route('/new', methods=['GET', 'POST']) # To render Homepage
def new_page():
    return render_template('index.html')

class MySQL_Crud:
    def __init__(self,host,username,Password,Database):
        self.host = host
        self.username = username
        self.password = Password
        self.db = Database
    def create_table(self):
        try:
          if (request.method=='POST'):
            mydb = connection.connect(host = self.host,database=self.db,user=self.username,passwd = self.password,use_pure = True)
            print(mydb.is_connected())
            print(request.form.keys())
            for t,i in enumerate(request.form.keys()):
                if i == 'Table_name':
                  tablename = request.form[i]
                  query = 'CREATE TABLE '+ tablename +' ('
                elif (i[0:5] =='Aname') | (i[0:2] =='dt') :
                  query = query + ' '+ request.form[i]  
                elif i[0:4] == 'auto':
                  if request.form[i] == 'on':
                      query = query + ' AUTO_INCREMENT'
                elif i[0:3] =='con':
                  query = query + ' '+request.form[i]+','
                elif  i[0:5] == 'Rname':
                  if request.form[i] != '':
                      query = query + ' FOREIGN KEY ('+request.form[i]+')' 
                elif  i[0:2] == 'RT':
                  if request.form[i] != '':
                    query = query + ' REFERENCES '+request.form[i]
                elif  i[0:2] == 'RA':
                  if request.form[i] != '':
                    query = query + '('+request.form[i]+'),'
            query = query[:-1]
            query = query +')'
            print(query)
            cursor =  mydb.cursor()
            cursor.execute(query)
            mydb.close()
        except Exception as e:
         mydb.close()
         raise Exception(e)

@app.route('/db_det', methods=['POST']) # To render Homepage
def initalize():
  try:
    print(request.form)
    if (request.method=='POST'):
        operation=request.form['operation']
        host = request.form['host']
        username = request.form['username']
        pwd  = request.form['Password']
        db  = request.form['Database']
    try:
        mydb = connection.connect(host = host,database=db,user=username,passwd = pwd,use_pure = True)
    except:
        raise Exception("Incorrect DB cred")
    global mysql
    mysql = MySQL_Crud(host,username,pwd,db)
    if operation == "Create":
        return render_template('create.html')
    if operation == "Insert":
        insert_obj = insert(operation)
        return insert_obj
    if operation == "Update":
        update_obj = insert(operation)
        return update_obj
    if operation == "delete":
        return insert(operation)
    if operation == "show":
        return insert(operation)
  except Exception as e:
    print(e)
    return render_template("error1.html",error = e)

@app.route('/create', methods=['POST']) # To render Homepage
def create_runner():
  try:
    print(request.form)
    mysql.create_table()
    return render_template('shared.html')
  except Exception as e:
    print(e)
    return render_template("error.html",error = e)
@app.route('/create1', methods=['GET', 'POST'])
def create():
    return render_template("create.html")
@app.route('/insert1', methods=['GET'])
def insert(operation=''):
    try:
     mydb = connection.connect(host = mysql.host,database=mysql.db,user=mysql.username,passwd = mysql.password,use_pure = True)
     query = 'SELECT Table_name as TablesName from information_schema.tables where table_schema = ' +"'"+mysql.db+"'"
     res_df = pd.read_sql(query,mydb)
     table_list = res_df.values.tolist()
     print(table_list)
     if operation == '':
       opr = request.args['opr']
     else:
       opr = operation.lower()
     mydb.close()
     return render_template("insert.html",table_list = table_list,db = mysql.db,opr = opr)
    except Exception as e:
     mydb.close()
     print(e)
     return render_template("error.html",error = e)
@app.route('/insert2', methods=['POST'])
def insert2():
  if(request.method == "POST"):
    table_name=request.form['Tables']
    try:
     mydb = connection.connect(host = mysql.host,database=mysql.db,user=mysql.username,passwd = mysql.password,use_pure = True)
     query = 'SELECT Column_Name,Column_Type from information_schema.columns where Table_Name =  ' +"'"+table_name+"'"
     res_df = pd.read_sql(query,mydb)
     column_list = res_df['Column_Name'].values.tolist()
     dt_list = res_df['Column_Type'].values.tolist()
     print(column_list)
     query = 'select Column_Name,IS_NULLABLE,COLUMN_KEY,EXTRA from information_schema.columns where TABLE_NAME = '+"'"+table_name+"'"
     res_df = pd.read_sql(query,mydb)
     for index,row in res_df.iterrows():
       if(row['EXTRA'] == 'auto_increment'):
         column_list.remove(row['Column_Name'])
         dt_list.pop(index)
         res_df.drop(index,inplace = True)
     
     null_list = res_df['IS_NULLABLE'].values.tolist()
     key_list = res_df['COLUMN_KEY'].values.tolist()
     query = 'select Column_Name,Referenced_Table_Name,Referenced_Column_Name from information_schema.KEY_COLUMN_USAGE where TABLE_NAME = '+"'"+table_name+"'" +'and Referenced_Table_Name is not null'
     res_df = pd.read_sql(query,mydb)
     for_cols = res_df['Column_Name'].values.tolist()
     ref_tbls = res_df['Referenced_Table_Name'].values.tolist()
     ref_cols = res_df['Referenced_Column_Name'].values.tolist()
     mydb.close()
     return render_template("insert2.html",column_list = column_list,table = table_name,dt = dt_list,null_list=null_list,key_list=key_list,for_cols = for_cols,ref_tbls =ref_tbls,ref_cols =ref_cols)
    except Exception as e:
     mydb.close()
     print(e)
     return render_template("error.html",error = e)
@app.route('/insert3', methods=['POST'])
def insert3():
  if(request.method == "POST"):
    print(request.form)
    try:
     table_name = request.form["Table_name"]
     mydb = connection.connect(host = mysql.host,database=mysql.db,user=mysql.username,passwd = mysql.password,use_pure = True)
     query = 'SELECT Column_Name,Column_Type from information_schema.columns where Table_Name =  ' +"'"+table_name+"'"
     res_df = pd.read_sql(query,mydb)
     column_list = res_df['Column_Name'].values.tolist()
     dt_list = res_df['Column_Type'].values.tolist()
     print(column_list)
     query = 'select Column_Name,IS_NULLABLE,COLUMN_KEY,EXTRA from information_schema.columns where TABLE_NAME = '+"'"+table_name+"'"
     res_df = pd.read_sql(query,mydb)
     for index,row in res_df.iterrows():
       if(row['EXTRA'] == 'auto_increment'):
         column_list.remove(row['Column_Name'])
         dt_list.pop(index)
    
     query = 'insert into ' + table_name+'('
     i=0
     t=1
     for element in column_list:
        query = query + element+','
     query = query[:-1]
     query = query + ') Values('
     for element in request.form.keys(): 
        if(element[:-1]==column_list[i]):
           if((dt_list[i][0:3] == 'int')| (dt_list[i][0:5] == 'float')|(dt_list[i][0:8] == 'smallint')|(dt_list[i][0:7] == 'decimal')|(dt_list[i][0:7] == 'numeric')|(dt_list[i][0:4] == 'real')|(dt_list[i][0:6] =='double')|(dt_list[i][0:5] == 'money')|(dt_list[i][0:8] == 'smallmon')):
             if request.form[element] != '':
               query = query + request.form[element] +','
             else:
               query = query + 'null,'
               t = t+1
           else:
             if request.form[element] != '':
               query = query + "'"+request.form[element]+"'"+','
             else:
               query = query + 'null,'
               t = t+1
           print(t)
           print(len(column_list))
           if(t == len(column_list)):
             raise Exception('All Null Values Not Possible')
           if(i < len(column_list)-1):
             i = i + 1
           else:
             i = 0
             t=1
             query = query[:-1]
             query = query + '),('
        
     query = query[:-2] 
     print(query)   
     cursor =  mydb.cursor()
     cursor.execute(query)  
     print(mydb.commit())    
     mydb.close()
     return render_template('shared.html')
    except Exception as e:
     mydb.close()
     print(e)
     return render_template("error.html",error = e)
@app.route('/update1', methods=['POST'])
def update1():
  if(request.method == "POST"):
    table_name=request.form['Tables']
    filter = request.form['where']
    try:
     mydb = connection.connect(host = mysql.host,database=mysql.db,user=mysql.username,passwd = mysql.password,use_pure = True)
     query = 'SELECT Column_Name,Column_Type from information_schema.columns where Table_Name =  ' +"'"+table_name+"'"
     res_df = pd.read_sql(query,mydb)
     column_list = res_df['Column_Name'].values.tolist()
     dt_list = res_df['Column_Type'].values.tolist()
     print(column_list)
     query = 'select Column_Name,IS_NULLABLE,COLUMN_KEY,EXTRA from information_schema.columns where TABLE_NAME = '+"'"+table_name+"'"
     res_df = pd.read_sql(query,mydb)
     for index,row in res_df.iterrows():
       if(row['EXTRA'] == 'auto_increment'):
         column_list.remove(row['Column_Name'])
         dt_list.pop(index)
         res_df.drop(index,inplace = True)
     dates = []
     for i in range(len(dt_list)):
       if dt_list[i] == 'date':
         dates.append(column_list[i])
     null_list = res_df['IS_NULLABLE'].values.tolist()
     key_list = res_df['COLUMN_KEY'].values.tolist()
     query = 'select Column_Name,Referenced_Table_Name,Referenced_Column_Name from information_schema.KEY_COLUMN_USAGE where TABLE_NAME = '+"'"+table_name+"'" +'and Referenced_Table_Name is not null'
     res_df = pd.read_sql(query,mydb)
     for_cols = res_df['Column_Name'].values.tolist()
     ref_tbls = res_df['Referenced_Table_Name'].values.tolist()
     ref_cols = res_df['Referenced_Column_Name'].values.tolist()
     query = 'SELECT '
     for i in column_list:
       query = query + i +','
     query  = query[:-1]
     if filter != '':
       query  = query +' FROM ' + mysql.db+ '.'+table_name+' where '+filter
     else:
       query  = query +' FROM ' + mysql.db+ '.'+table_name
     res_df = pd.read_sql(query,mydb)
     res_df[dates] = res_df[dates].astype(str)
     mylist = []
     for i in res_df.index:
       mylist.append(res_df.iloc[i].to_list())
     print(mylist)
     mydb.close()
     return render_template("update1.html",column_list = column_list,table = table_name,dt = dt_list,null_list=null_list,key_list=key_list,for_cols = for_cols,ref_tbls =ref_tbls,ref_cols =ref_cols,mylist=mylist)
    except Exception as e:
     mydb.close()
     print(e)
     return render_template("error.html",error = e)
@app.route('/update2', methods=['POST'])
def update2():
  if(request.method == "POST"):
    print(request.form)
    try:
     table_name = request.form["Table_name"]
     mydb = connection.connect(host = mysql.host,database=mysql.db,user=mysql.username,passwd = mysql.password,use_pure = True)
     query = 'SELECT Column_Name,Column_Type from information_schema.columns where Table_Name =  ' +"'"+table_name+"'"
     res_df = pd.read_sql(query,mydb)
     column_list = res_df['Column_Name'].values.tolist()
     dt_list = res_df['Column_Type'].values.tolist()
     print(column_list)
     query = 'select Column_Name,IS_NULLABLE,COLUMN_KEY,EXTRA from information_schema.columns where TABLE_NAME = '+"'"+table_name+"'"
     res_df = pd.read_sql(query,mydb)
     for index in res_df.index:
       if(res_df.iloc[index]['EXTRA'] == 'auto_increment'):
         column_list.remove(res_df.iloc[index]['Column_Name'])
         dt_list.pop(index)
     
     query = 'SET SQL_SAFE_UPDATES = 0; update ' +mysql.db+'.' + table_name+' SET '
     i=0
     index = list(request.form.keys())
     cnt = 0
     while(cnt < (len(index)-1)):
       if (index[cnt] != 'Table_name') :
        if (i < len(column_list)) & (index[cnt][-1]!='o'):
            if((dt_list[i][0:3] == 'int')| (dt_list[i][0:5] == 'float')|(dt_list[i][0:8] == 'smallint')|(dt_list[i][0:7] == 'decimal')|(dt_list[i][0:7] == 'numeric')|(dt_list[i][0:4] == 'real')|(dt_list[i][0:6] =='double')|(dt_list[i][0:5] == 'money')|(dt_list[i][0:8] == 'smallmon')):
              if (request.form[index[cnt]] == 'null')|(request.form[index[cnt]] == 'NaN'):
                query = query +index[cnt][:-1]+'='+'null'+','
              else:
                query = query +index[cnt][:-1]+'='+request.form[index[cnt]]+','
            else:
              query = query +index[cnt][:-1]+"= '"+request.form[index[cnt]]+"',"
            i = i + 1
            cnt = cnt +1
        else:
          query = query[:-1]
          query = query + ' where '
          for m in range(len(column_list)):
            if((dt_list[m][0:3] == 'int')| (dt_list[m][0:5] == 'float')|(dt_list[m][0:8] == 'smallint')|(dt_list[m][0:7] == 'decimal')|(dt_list[m][0:7] == 'numeric')|(dt_list[m][0:4] == 'real')|(dt_list[m][0:6] =='double')|(dt_list[m][0:5] == 'money')|(dt_list[m][0:8] == 'smallmon')):
              if (request.form[index[cnt]] == 'null')|(request.form[index[cnt]] == 'NaN'):
               query = query +index[cnt][:-2]+' is '+' null'+' and '
              else:
                query = query +index[cnt][:-2]+'='+request.form[index[cnt]]+' and '
            else:
              if (request.form[index[cnt]] == 'null'):
               query = query +index[cnt][:-2]+" is "+request.form[index[cnt]]+" and "
              else:
               query = query +index[cnt][:-2]+"='"+request.form[index[cnt]]+"' and "
            cnt = cnt +1
          query = query[:-4]
          query = query + ';' + 'update ' +mysql.db+'.' + table_name+' SET '
          i=0
  
     l1 = len(';' + 'update ' +mysql.db+'.' + table_name+' SET ')  
     query = query[:-l1]
     print(query)   
     cursor =  mydb.cursor()
     for _ in cursor.execute(query, multi=True): 
       pass
     mydb.commit()   
     mydb.close()
     return render_template('shared.html')
    except Exception as e:
     mydb.close()
     print(e)
     return render_template("error.html",error = e)
@app.route('/show1', methods=['POST'])
def show1():
    try:
     mydb = connection.connect(host = mysql.host,database=mysql.db,user=mysql.username,passwd = mysql.password,use_pure = True)
     where = request.form['where']
     table_nm = request.form['Tables']
     query = 'SELECT Column_Name as ColumnName from information_schema.columns where table_schema = ' +"'"+mysql.db+"'" + ' and Table_Name ='+"'"+table_nm+"'"
     res_df = pd.read_sql(query,mydb)
     col_list = res_df.values.tolist()
     mydb.close()
     return render_template("show.html",col_list = col_list,where = where, table_nm= table_nm)
    except Exception as e:
     mydb.close()
     print(e)  
     return render_template("error.html",error = e)
@app.route('/show2', methods=['POST'])
def show2():
    try:
     mydb = connection.connect(host = mysql.host,database=mysql.db,user=mysql.username,passwd = mysql.password,use_pure = True)
     where = request.form['where']
     table_nm = request.form['tbl_name']
     query = 'SELECT '
     col_list = []
     for i in request.form.keys():
         if(request.form[i]=='on'):
           query = query + i+','
           col_list.append(i)
     query = query[:-1]
     if where == '':
       query = query + ' FROM ' + mysql.db+'.'+table_nm
     else:
       query = query + ' FROM ' + mysql.db+'.'+table_nm +' where '+where
     res_df = pd.read_sql(query,mydb)
     mylist = []
     for i in res_df.columns:
       mylist.append(res_df[i].to_list())
     mydb.close()
     if request.form['view'] == 'CSV':
        res_df.to_csv(request.form['file_pth'],index=False)
        return render_template("shared.html")
     else:
        return render_template("show1.html",mylist = mylist,col_list = col_list,table_nm =table_nm)
    except Exception as e:
     mydb.close()
     print(e) 
     return render_template("error.html",error = e)
@app.route('/show3', methods=['GET'])
def show3():  
   return render_template("shared.html")
@app.route('/delete1', methods=['POST'])
def delete1():
    try:
     mydb = connection.connect(host = mysql.host,database=mysql.db,user=mysql.username,passwd = mysql.password,use_pure = True)
     where = request.form['where']
     table_nm = request.form['Tables']
     opr = request.form['del_opt']
     if(opr == 'delete'):
      query = 'DELETE FROM ' +mysql.db+ '.'+table_nm
      if where != '':
        query = query +' where '+where
      cursor =  mydb.cursor()
      cursor.execute(query)
      mydb.commit()
      mydb.close()
     else:
      query = 'DROP TABLE ' +mysql.db+ '.'+table_nm
      cursor =  mydb.cursor()
      cursor.execute(query)
      mydb.commit()
      mydb.close()
     return render_template("shared.html")
    except Exception as e:
     mydb.close()
     print(e)
     return render_template("error.html",error = e)  

if __name__ == '__main__':
    app.run()
