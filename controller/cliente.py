#carregando as funções em outros arquivos .py
import services.database as db

#função para inserir registro no banco de dados
def incluir(nome, idade, turno, matricula, periodo):
    db.cur.execute("""
                   INSERT into public.alunos (nome, idade, turno, matricula, periodo)
                   VALUES ('%s','%s','%s','%s','%s')
                   """ % (nome, idade, turno, matricula, periodo))
    db.con.commit()
    
#função para inserir registro no banco de dados
def selecionar():
    db.cur.execute("""
                   SELECT * FROM alunos
                   """)
    data = db.cur.fetchall()
    rows = []
    for row in data:
        rows.append(row)
    return rows

def deletar(matricula):
    db.cur.execute("""
                DELETE  from alunos WHERE matricula= '%s';
                """ % (matricula))
    db.con.commit()

   
