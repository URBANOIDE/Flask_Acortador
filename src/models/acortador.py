from src.config.db import DB


class AcortadorUrl():
    
    def insertar(self, url_original, url_corta):
        cursor = DB.cursor()

        cursor.execute('insert into url(url_original, url_corta) values(?,?)', (url_original, url_corta,))
        
        cursor.close()

    def insertar_user(self, id, url_original, url_corta):
        cursor = DB.cursor()

        cursor.execute('insert into url(usuarios_id, url_original, url_corta) values(?,?,?)', (id, url_original, url_corta,))
        
        cursor.close()
    
    def registrar(self, nombre, email, password):
        cursor = DB.cursor()

        cursor.execute('insert into usuarios(nombre, email, password) values(?,?,?)', (nombre, email, password,))
        
        cursor.close()
    def iniciar(self, email, password):
        cursor = DB.cursor()

        cursor.execute('select * from usuarios where email = ? and password = ?', (email, password,))

        user_exist = cursor.fetchone()
        
        cursor.close()
        
        return user_exist
        
    def redirigir(self, url_corta):
        cursor = DB.cursor()

        cursor.execute('select * from url where url_corta = ?', (url_corta,))
        
        link = cursor.fetchone()

        cursor.close()

        return link
