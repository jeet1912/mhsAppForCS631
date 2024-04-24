import MySQLdb
from django.conf import settings

def execute_query(query, params=None, fetchone=False, fetchall=False):
    db = MySQLdb.connect(
        host=settings.DATABASES['default']['HOST'],
        user=settings.DATABASES['default']['USER'],
        passwd=settings.DATABASES['default']['PASSWORD'],
        db=settings.DATABASES['default']['NAME']
    )
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(query, params or ())

    if fetchone:
        result = cursor.fetchone()
    elif fetchall:
        result = cursor.fetchall()
    else:
        result = None

    db.commit()
    cursor.close()
    db.close()
    return result
