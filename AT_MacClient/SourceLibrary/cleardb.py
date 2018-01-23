import MySQLdb




def connect(host, database, port='3320',user='Anyshare', passwd='asAlqlTkWU0zqfxrLTed'):

    try:
        section = "mysqld3320"
        dir_list = ["/var/lib/", section, "/", section, ".sock"]
        socket = "".join(dir_list)
        db = MySQLdb.connect(host=host, db=database, port=port,
                             user=user, passwd=passwd,
                             unix_socket=socket, charset='utf8')
        return db
    except Exception, e:
        print e
        return 'get an exception',e