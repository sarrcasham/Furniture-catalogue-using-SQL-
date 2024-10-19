import mysql.connector
mydb=mysql.connector.connect(host = "localhost", user= "root", password= "Newdelhi25", database="world")  
mycur=mydb.cursor()
#mycur.execute("create database if not exists wor")
#mycur.execute("use pro")
##mycur.execute("create table if not exists furniture(Product_Id int(5) Primary Key,Name varchar(20),Price decimal(9,2),Colour varchar(10),Type varchar(20),Category varchar(15),size varchar(10),Polish varchar(20))")
##mycur.execute('insert into furniture values(1001,"Sofa-cum-bed",50000.50,"Blue","Pull Out","Living Room","Medium","Lacquer wood")')
##mycur.execute('insert into furniture values(1002,"Bed",45000.50,"Dark brown","King Size","Bedroom","Large","Varnish")')
##mycur.execute('insert into furniture values(1003,"Table",20000.50,"Yellow","Glass Top","Dining Room","Large","Varnish")')
##mycur.execute('insert into furniture values(1004,"Chair",10000.50,"Brown","Cushion","Study Room","Medium","Lacquer wood")')
##mycur.execute('insert into furniture values(1005,"Sofa Set",65000.50,"Green","Cushion","Living Room","Small","Lacquer wood")')
##mycur.execute('insert into furniture values(1006,"Table",18000.50,"Violet","Wooden","Study Room","Small","Varnish")')
##mycur.execute('insert into furniture values(1007,"Dressing Table",20000.50,"Violet",NULL,"Bedroom","Large","Lacquer wood")')
##mycur.execute('insert into furniture values(1008,"Cupboard",60000.50,"Red","Double door","Bedroom","Large","Polyurethane")')
##mycur.execute('insert into furniture values(1009,"Table",25000.50,"White","Glass Top","Living Room","Medium","Lacquer wood")')
##mycur.execute('insert into furniture values(1010,"Chair Set",40000.50,"Blue","Cushion","Dining Room","Medium","Varnish")')
##mycur.execute('insert into furniture values(1011,"Lamp",5000.50,"Yellow","Table Lamp","Decor","Small","Water based wood")')
##mycur.execute('insert into furniture values(1012,"Book shelf",20000.50,"Red","Barrister","Living Room","Medium","Lacquer wood")')
##mycur.execute('insert into furniture values(1013,"Lamp",8000.50,"Green","Floor Lamp","Bedroom","Small","Varnish")')
##mycur.execute('insert into furniture values(1014,"Book shelf",25000.50,"Blue","Revolving and Corner","Study Room","Large","Lacquer wood")')
##mycur.execute('insert into furniture values(1015,"Cupboard",40000.50,"Brown","Single Door","Decor","Large","Polyurethane")')
##mydb.commit()
def enter():
    ans=True
    ch=input("Want to enter a record?(y/n): ")
    if ch=="n":
        ans=False
    while ans:
        p=input("Product Id: ")
        n=input("Name: ")
        pr=input("Price: ")
        c=input("Colour: ")
        t=input("Type: ")
        ca=input("Category: ")
        s=input("Size: ")
        po=input("Polish: ")
        mycur.execute("insert into furniture values("+p+",'"+n+"',"+pr+",'"+c+"','"+t+"','"+ca+"','"+s+"','"+po+"')")
        mydb.commit()
        x=input("Want to continue?(y/n): ")
        if x=="n":
            ans=False
def select():
    ch=int(input("MENU:\n1.Display all\n2.Display in asc. or desc. order of a column\n3.Display based on an entry in a column\n4.Display based on name\n5.Count no. of entries in a column\n6.Max,min,avg,sum based on price\n7.Display group all entries based on a particular column\n"))
    if ch==1:
        mycur.execute("select * from furniture")
        a=mycur.fetchall()
        for k in a:
            print(k)
    elif ch==2:
        c=int(input("1.Ascending\n2.Descending\n"))
        if c==1:
            n=input("Enter column: ")
            mycur.execute("select * from furniture order by "+n+"")
            a=mycur.fetchall()
            for k in a:
                print(k)
        elif c==2:
            n=input("Enter column: ")
            mycur.execute("select * from furniture order by "+n+" desc")
            a=mycur.fetchall()
            for k in a:
                print(k)
        else:
            print("Wrong choice!!")
    elif ch==3:
        n=input("Enter column: ")
        z=input("Enter search value: ")
        mycur.execute("select * from furniture where "+n+"='"+z+"'")
        a=mycur.fetchall()
        for k in a:
            print(k)
    elif ch==4:
        n=int(input("1.To display rows with specified no. of characters in a name\n2.To display rows with a specified string present in it\n"))
        if n==1:
            z=input("Enter underscores: ")
            mycur.execute("select * from furniture where Name like '"+z+"'")
            a=mycur.fetchall()
            for k in a:
                print(k)
        elif n==2:
            z=input("Enter string: ")
            mycur.execute("select * from furniture where Name like '"+z+"'")
            a=mycur.fetchall()
            for k in a:
                print(k)
        else:
            print("Wrong choice!!")
    elif ch==5:
        z=input("Enter column: ")
        mycur.execute("select count("+z+") from furniture")
        a=mycur.fetchall()
        for k in a:
            print(k)
    elif ch==6:
        z=int(input("1.Sum\n2.Average\n3.Maximum\n4.Minimum\n"))
        s=input("Enter where condition item name: ")
        if z==1:
            mycur.execute("select sum(Price) from furniture where name='"+s+"'")
            a=mycur.fetchall()
            for k in a:
                print(k)
        elif z==2:
            mycur.execute("select avg(Price) from furniture where name='"+s+"'")
            a=mycur.fetchall()
            for k in a:
                print(k)
        elif z==3:
            mycur.execute("select max(Price) from furniture where name='"+s+"'")
            a=mycur.fetchall()
            for k in a:
                print(k)
        elif z==4:
            mycur.execute("select min(Price) from furniture where name='"+s+"'")
            a=mycur.fetchall()
            for k in a:
                print(k)
        else:
            print("Wrong choice!!")
    elif ch==7:
        q=input("Enter 'group by' condition: ")
        mycur.execute("select * from furniture where Price>=20000 group by "+q+"")
        a=mycur.fetchall()
        for k in a:
            print(k)
def update():
    z=input("Enter column to be updated: ")
    q=input("Enter row condition: ")
    w=input("Enter updated value: ")
    mycur.execute("update furniture set "+z+"="+w+" where "+q+"")
    print("Updated table: ")
    mycur.execute("select * from furniture")
    a=mycur.fetchall()
    for k in a:
        print(k)
def alter():
    z=int(input("1.Add\n2.Modify\n3.Delete\n"))
    if z==1:
        q=input("Enter new column along with its data type, size etc.: ")
        mycur.execute("alter table furniture add("+q+")")
        mydb.commit()
        print("Table structure: ")
        mycur.execute("describe furniture")
        a=mycur.fetchall()
        for k in a:
            print(k)
    elif z==2:
        q=input("Enter column to be modified along with its data type, size etc.: ")
        mycur.execute("alter table furniture modify "+q+"")
        mydb.commit()
        print("Table structure: ")
        mycur.execute("describe furniture")
        a=mycur.fetchall()
        for k in a:
            print(k)
    elif z==3:
        q=input("Enter column to be deleted: ")
        mycur.execute("alter table furniture drop column "+q+"")
        mydb.commit()
        print("Table structure: ")
        mycur.execute("describe furniture")
        a=mycur.fetchall()
        for k in a:
            print(k)
    else:
        print("Wrong choice:")
def delete():
    z=int(input("1.Delete particular rows\n2.Delete entire table\n"))
    if z==1:
        q=input("Enter where condition: ")
        mycur.execute("delete from furniture where "+q+"")
        mycur.execute("select * from furniture")
        a=mycur.fetchall()
        for k in a:
            print(k)
    elif z==2:
        mycur.execute("drop table furniture")
        print("Table deleted!")
        mydb.commit()
    else:
        print("Wrong choice!!")
ans='y'
while ans in("yY"):
    p=int(input("MENU:\n1.Enter new values\n2.Display from table\n3.Update table\n4.Alter table\n5.Delete from table\n"))
    if p==1:
        enter()
    elif p==2:
        select()
    elif p==3:
        update()
    elif p==4:
        alter()
    elif p==5:
        delete()
    else:
        print("Wrong choice!!")
    ans=input("Want to continue?(y/n): ")
