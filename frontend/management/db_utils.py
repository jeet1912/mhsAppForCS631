import MySQLdb
import logging
from django.conf import settings

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def execute_query(query, params=None, fetchone=False, fetchall=False, insert_new=False):
    db = MySQLdb.connect(
        host=settings.DATABASES['default']['HOST'],
        user=settings.DATABASES['default']['USER'],
        passwd=settings.DATABASES['default']['PASSWORD'],
        db=settings.DATABASES['default']['NAME']
    )
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        logger.debug("Executing query: %s", query)
        logger.debug("Executing params: %s", params)
        cursor.execute(query, params or ())

        if fetchone:
            result = cursor.fetchone()
        elif fetchall:
            result = cursor.fetchall()
        elif insert_new:
            result = cursor.lastrowid
        else:
            result = "Success"

        db.commit()
        logger.debug("Query result: %s", result)
        return result
    except MySQLdb.Error as e:
        db.rollback()
        logger.error("Error in executing query: %s", e)
        return "Error"
    finally:
        cursor.close()
        db.close()
