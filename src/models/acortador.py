from src.config.db import DB


class AcortadorUrl():
    
    def insertar(self, url_original, url_corta):
        cursor = DB.cursor()

        cursor.execute('insert into url(url_original, url_corta) values(?,?)', (url_original, url_corta,))
        
        cursor.close()