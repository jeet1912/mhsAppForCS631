import MySQLdb
import logging
from django.conf import settings

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def execute_query(query, params=None, fetchone=False, fetchall=False, insert_new = False):
    db = MySQLdb.connect(
        host=settings.DATABASES['default']['HOST'],
        user=settings.DATABASES['default']['USER'],
        passwd=settings.DATABASES['default']['PASSWORD'],
        db=settings.DATABASES['default']['NAME']
    )
    cursor = db.cursor(MySQLdb.cursors.DictCursor)

    # Log the query
    logger.debug("Executing query: %s", query)
    print(params)

    cursor.execute(query, params or ())

    if fetchone:
        result = cursor.fetchone()
    elif fetchall:
        result = cursor.fetchall()
    elif insert_new:
        result = cursor.lastrowid
    else:
        result = None


    # Print the result
    logger.debug("Query result: %s", result)

    db.commit()
    cursor.close()
    db.close()
    return result
