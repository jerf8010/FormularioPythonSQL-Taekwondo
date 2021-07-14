from tkinter import ttk
from tkinter import *

import sqlite3

class Product:

    dbName = 'database.db'

    def __init__(self, window):
        self.wind = window
        self.wind.title('Registro App')

        frame = LabelFrame(self.wind, text = 'Registro nuevo alumno')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        # nombre
        Label(frame, text = 'Nombre: ').grid(row = 1, column = 0)
        self.nombre = Entry(frame)
        self.nombre.focus()
        self.nombre.grid(row = 1, column = 1)

        #inscripcion
        Label(frame, text = 'Inscripción: ').grid(row = 1, column = 3)
        self.inscripcion = Entry(frame)
        self.inscripcion.grid(row = 1, column = 4)

        # apellido
        Label(frame, text = 'Apellidos: ').grid(row = 2, column = 0)
        self.apellidos = Entry(frame)
        self.apellidos.grid(row = 2, column = 1)

        #Fecha de nacimiento
        Label(frame, text = 'Fecha de nacimiento: ').grid(row = 3, column = 0)
        self.dia = Entry(frame)
        self.dia.grid(row = 3, column = 1)
        '''
        Label(frame, text = 'de ').grid(row = 3, column = 2)
        self.mes = Entry(frame)
        self.mes.grid(row = 3, column = 3)
        Label(frame, text = 'del ').grid(row = 3, column = 4)
        self.anio = Entry(frame)
        self.anio.grid(row = 3, column = 5)
        '''

        # direccion
        Label(frame, text = 'Dirección: ').grid(row = 4, column = 0)
        self.direccion = Entry(frame)
        self.direccion.grid(row = 4, column = 1)

        # Representante
        Label(frame, text = 'Representante: ').grid(row = 5, column = 0)
        self.representante = Entry(frame)
        self.representante.grid(row = 5, column = 1)

        # Escuela
        Label(frame, text = 'Escuela: ').grid(row = 6, column = 0)
        self.escuela = Entry(frame)
        self.escuela.grid(row = 6, column = 1)

        # Telefono
        Label(frame, text = 'Teléfono: ').grid(row = 7, column = 0)
        self.telefono = Entry(frame)
        self.telefono.grid(row = 7, column = 1)

        # Celular
        Label(frame, text = 'Celular: ').grid(row = 7, column = 3)
        self.celular = Entry(frame)
        self.celular.grid(row = 7, column = 4)

        #Fecha de ingreso
        Label(frame, text = 'Fecha de ingreso: ').grid(row = 8, column = 0)
        self.diaI = Entry(frame)
        self.diaI.grid(row = 8, column = 1)
        '''
        Label(frame, text = 'de ').grid(row = 8, column = 2)
        self.mesI = Entry(frame)
        self.mesI.grid(row = 8, column = 3)
        Label(frame, text = 'del ').grid(row = 8, column = 4)
        self.anioI = Entry(frame)
        self.anioI.grid(row = 8, column = 5)
        '''


        # Boton

        ttk.Button(frame, text = 'Registrar', command = self.add_product).grid(row = 15 , column = 0, columnspan = 3, sticky = W + E)

        ttk.Button(frame, text = 'Exportar CSV', command = self.exportar).grid(row = 15, column = 2, columnspan = 3, sticky = W + E)
        # Output mensaje
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 16, column = 0, columnspan = 2, sticky = W + E)
        # tabla

        self.tree = ttk.Treeview(height = 10, columns = (0, 1, 2, 3, 4, 5, 6, 7, 8, 0))
        self.tree.grid(row = 18, column = 0, columnspan = 2)
        self.tree.heading('#0', text = 'ID', anchor = CENTER)
        self.tree.heading('#1', text = 'Nombre', anchor = CENTER)
        self.tree.heading('#2', text = 'Apellidos', anchor = CENTER)
        self.tree.heading('#3', text = 'Dirección', anchor = CENTER)
        self.tree.heading('#4', text = 'Representante', anchor = CENTER)
        self.tree.heading('#5', text = 'Escuela', anchor = CENTER)
        self.tree.heading('#6', text = 'teléfono', anchor = CENTER)
        self.tree.heading('#7', text = 'Celular', anchor = CENTER)
        self.tree.heading('#8', text = 'Fecha de nacimiento', anchor = CENTER)
        self.tree.heading('#9', text = 'Fecha de ingreso', anchor = CENTER)
        self.tree.heading('#10', text = 'Inscripcion', anchor = CENTER)

        self.tree.column("#0", width = 50)
        self.tree.column("#6", width = 100)
        self.tree.column("#7", width = 100)
        self.tree.column("#8", width = 110)
        self.tree.column("#9", width = 110)
        self.tree.column("#10", width = 100)


        ttk.Button(text = 'BORRAR', command = self.delete_product).grid(row = 20, column = 0, sticky = W + E)
        ttk.Button(text = 'EDITAR', command = self.edit_product).grid(row = 20, column = 1, sticky = W + E)

        self.get_product()




    def run_query(self, query, parametros = ()): 
        with sqlite3.connect(self.dbName) as conn: 
            cursor = conn.cursor()
            result = cursor.execute(query, parametros)
            conn.commit()
        return result

    def get_product(self): 

        records = self.tree.get_children()
        for element in records: 
            self.tree.delete(element)

        query = 'SELECT * FROM Registros ORDER BY Nombre DESC'
        db_rows = self.run_query(query)

        for row in db_rows:
            self.tree.insert('', 0, text = row[0], values = row[1:11])

    def validation(self):
        return len(self.nombre.get()) != 0 and len(self.apellidos.get()) != 0


    def add_product(self): 
        if self.validation():
            query = 'INSERT INTO Registros VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
            parameters = (self.nombre.get(), self.apellidos.get(), self.direccion.get(), self.representante.get(), self.escuela.get(), self.telefono.get(), self.celular.get(), self.dia.get(), self.diaI.get(), self.inscripcion.get())
            self.run_query(query, parameters)
            self.message['text'] = 'Alumno {} fue registrado exitosamente'.format(self.nombre.get())
            self.nombre.delete(0, END)
            self.apellidos.delete(0, END)
        else:
            self.message['text'] = "El nombre y los apellidos son requeridos"

        self.get_product()

    def delete_product(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][1]
        except IndexError as e:
            self.message['text'] = 'Selecciona un registro'
            return
        self.message['text'] = ''
        name = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM Registros WHERE Id = ?'
        self.run_query(query, (name, ))
        self.message['text'] = 'El registro {} ha sido eliminado'.format(name)
        self.get_product()

    def edit_product(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][1]
        except IndexError as e:
            self.message['text'] = 'Selecciona un registro'
            return
        
        self.edit_wind = Toplevel()
        self.edit_wind.title = 'Editar registro'

        
        # nombre
        Label(self.edit_wind, text = 'Nombre: ').grid(row = 1, column = 0)
        newnombre = Entry(self.edit_wind)
        newnombre.focus()
        newnombre.grid(row = 1, column = 1)

        #inscripcion
        Label(self.edit_wind, text = 'Inscripción: ').grid(row = 1, column = 3)
        newinscripcion = Entry(self.edit_wind)
        newinscripcion.grid(row = 1, column = 4)

        # apellido
        Label(self.edit_wind, text = 'Apellidos: ').grid(row = 2, column = 0)
        newapellidos = Entry(self.edit_wind)
        newapellidos.grid(row = 2, column = 1)

        #Fecha de nacimiento
        Label(self.edit_wind, text = 'Fecha de nacimiento: ').grid(row = 3, column = 0)
        newdia = Entry(self.edit_wind)
        newdia.grid(row = 3, column = 1)
        '''
        Label(frame, text = 'de ').grid(row = 3, column = 2)
        self.mes = Entry(frame)
        self.mes.grid(row = 3, column = 3)
        Label(frame, text = 'del ').grid(row = 3, column = 4)
        self.anio = Entry(frame)
        self.anio.grid(row = 3, column = 5)
        '''

        # direccion
        Label(self.edit_wind, text = 'Dirección: ').grid(row = 4, column = 0)
        newdireccion = Entry(self.edit_wind)
        newdireccion.grid(row = 4, column = 1)

        # Representante
        Label(self.edit_wind, text = 'Representante: ').grid(row = 5, column = 0)
        newrepresentante = Entry(self.edit_wind)
        newrepresentante.grid(row = 5, column = 1)

        # Escuela
        Label(self.edit_wind, text = 'Escuela: ').grid(row = 6, column = 0)
        newescuela = Entry(self.edit_wind)
        newescuela.grid(row = 6, column = 1)

        # Telefono
        Label(self.edit_wind, text = 'Teléfono: ').grid(row = 7, column = 0)
        newtelefono = Entry(self.edit_wind)
        newtelefono.grid(row = 7, column = 1)

        # Celular
        Label(self.edit_wind, text = 'Celular: ').grid(row = 7, column = 3)
        newcelular = Entry(self.edit_wind)
        newcelular.grid(row = 7, column = 4)

        #Fecha de ingreso
        Label(self.edit_wind, text = 'Fecha de ingreso: ').grid(row = 8, column = 0)
        newdiaI = Entry(self.edit_wind)
        newdiaI.grid(row = 8, column = 1)

        
        Button(self.edit_wind, text = 'Actualizar', command = lambda: self.edit_records(newnombre.get(), newapellidos.get(), newdireccion.get(), newrepresentante.get(), newescuela.get(), newtelefono.get(), newcelular.get(), newdia.get(), newdiaI.get(), newinscripcion.get())).grid(row = 9, column = 2, sticky = W + E)
        

    def edit_records(self, newnombre, newapellidos, newdireccion, newrepresentante, newescuela, newtelefono, newcelular, newdia, newdiaI, newinscripcion):
        query = 'UPDATE Registros SET Nombre = ?, Apellidos = ?, Direccion = ?, Representante = ?, Escuela = ?, Telefono = ?, Celular = ?, FechaNacimiento = ?, FechaIngreso = ?, Inscripcion = ? WHERE Nombre = ?'
        parameters = (newnombre, newapellidos, newdireccion, newrepresentante, newescuela, newtelefono, newcelular, newdia, newdiaI, newinscripcion, self.tree.item(self.tree.selection())['values'][0])
        print(query)
        self.run_query(query, parameters)
        self.edit_wind.destroy()
        self.message['text'] = 'Registro {} actualizado exitosamente'.format(self.tree.item(self.tree.selection())['text'])
        self.get_product()

    def exportar(self):
        import pandas as pd
        conn = sqlite3.connect(self.dbName)
        df = pd.read_sql_query('SELECT * FROM Registros', conn)
        df.to_csv('registro.csv')
        conn.close()

#https://www.youtube.com/watch?v=W2kAF9pKPPE

        



if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()