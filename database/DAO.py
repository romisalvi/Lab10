from database.DB_connect import DBConnect
from model.country import Country
from model.border import Border


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getCountries():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT c.*
                    from country c
                    order by c.StateNme
                                   """

        cursor.execute(query)

        for row in cursor:
            result.append(
               Country(**row
                       )
            )

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getConfini(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT c.*
                    FROM contiguity c
                    where c.conttype=1 and c.year<=%s
        
                                           """

        cursor.execute(query, (anno,))

        for row in cursor:
            result.append(
                Border(**row
                        )
            )

        cursor.close()
        conn.close()
        return result


