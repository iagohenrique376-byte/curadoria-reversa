import sqlite3

def criar_banco():
    # Conecta ou cria o ficheiro do banco de dados na mesma pasta
    conexao = sqlite3.connect('curadoria.db')
    cursor = conexao.cursor()

    # 1. Tabela USU_USUARIO
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS USU_USUARIO (
        USU_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        USU_NOME TEXT NOT NULL,
        USU_EMAIL TEXT NOT NULL UNIQUE,
        USU_DATA_CADASTRO DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    ''')

    # 2. Tabela CATEGORIA
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS CATEGORIA (
        id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_categoria TEXT NOT NULL
    );
    ''')

    # 3. Tabela APP_CONTEUDO
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS APP_CONTEUDO (
        id_conteudo INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT NOT NULL,
        titulo TEXT NOT NULL,
        descricao TEXT,
        tipo_midia TEXT NOT NULL,
        data_salvamento DATETIME DEFAULT CURRENT_TIMESTAMP,
        idUSU_USUARIO INTEGER NOT NULL,
        id_categoria INTEGER,
        FOREIGN KEY (idUSU_USUARIO) REFERENCES USU_USUARIO(USU_ID) ON DELETE CASCADE,
        FOREIGN KEY (id_categoria) REFERENCES CATEGORIA(id_categoria) ON DELETE SET NULL
    );
    ''')

    # 4. Tabela FILA_ESPERA
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS FILA_ESPERA (
        id_fila INTEGER PRIMARY KEY AUTOINCREMENT,
        data_expiracao DATETIME NOT NULL,
        status TEXT DEFAULT 'Em Espera',
        justificativa_importancia TEXT,
        idAPP_CONTEUDO INTEGER NOT NULL UNIQUE,
        FOREIGN KEY (idAPP_CONTEUDO) REFERENCES APP_CONTEUDO(id_conteudo) ON DELETE CASCADE
    );
    ''')

    conexao.commit()
    conexao.close()
    print("Base de dados 'curadoria.db' e tabelas criadas com sucesso!")

if __name__ == '__main__':
    criar_banco()