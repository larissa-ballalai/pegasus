###########################################################################################################################################################################
# CNES_EQ CNES_EQ CNES_EQ CNES_EQ CNES_EQ CNES_EQ CNES_EQ CNES_EQ CNES_EQ CNES_EQ CNES_EQ CNES_EQ CNES_EQ CNES_EQ CNES_EQ CNES_EQ CNES_EQ CNES_EQ CNES_EQ CNES_EQ CNES_EQ #
###########################################################################################################################################################################

import psycopg2


"""
Cria o schema do sub banco de dados do CNES_EQ (Equipamentos) para atender ao formato do SGBD postgreSQL.
Na verdade o schema abaixo deve atender ao formato dos SGBD Oracle e SQL Server com no máximo pequenas modificações.

"""

# Função de criação das tabelas do sub banco de dados cnes_eq
def create_tables(connection_data, child_db):
    conn = psycopg2.connect(dbname=connection_data[0],
                            host=connection_data[1],
                            port=connection_data[2],
                            user=connection_data[3],
                            password=connection_data[4])

    cursor = conn.cursor()

    cursor.execute(f'''/*Tabela Equipamentos (tabela principal do sub banco de dados cnes_eq)*/
                       CREATE TABLE IF NOT EXISTS {child_db}.eqbr("CNES_ID"                 VARCHAR(7),
                                                                  "UF_EQ"                   VARCHAR(2),
                                                                  "ANO_EQ"                  INTEGER,
                                                                  "MES_EQ"                  VARCHAR(2),
                                                                  "CODUFMUN_ID"             VARCHAR(6),
                                                                  "TIPEQUIP_ID"             VARCHAR(2),
                                                                  "CODEQUIP_ID"             VARCHAR(2),
                                                                  "QT_EXIST"                FLOAT,
                                                                  "QT_USO"                  FLOAT,
                                                                  "IND_SUS"                 NUMERIC,
                                                                  "ND_NSUS"                 NUMERIC);

                       /*Tabela dos estabelecimentos de saúde*/
                       CREATE TABLE IF NOT EXISTS {child_db}.cnes("ID"                      VARCHAR(7),
                                                                  "DESCESTAB"               VARCHAR(66),
                                                                  "RSOC_MAN"                VARCHAR(66),
                                                                  "CPF_CNPJ"                VARCHAR(14),
                                                                  "EXCLUIDO"                NUMERIC,
                                                                  "DATAINCL"                DATE,
                                                                  "DATAEXCL"                DATE);

                       /*Tabela dos municípios de localização de estabelecimentos*/
                       CREATE TABLE IF NOT EXISTS {child_db}.codufmun("ID"                  VARCHAR(6),
                                                                      "MUNNOME"	            VARCHAR(66),
                                                                      "MUNNOMEX"            VARCHAR(66),
                                                                      "MUNCODDV"            VARCHAR(7),
                                                                      "OBSERV"              VARCHAR(66),
                                                                      "SITUACAO"            VARCHAR(66),
                                                                      "MUNSINP"	            VARCHAR(66),
                                                                      "MUNSIAFI"            VARCHAR(66),
                                                                      "UFCOD_ID"            VARCHAR(2),
                                                                      "AMAZONIA"            VARCHAR(66),
                                                                      "FRONTEIRA"           VARCHAR(66),
                                                                      "CAPITAL"             VARCHAR(66),
                                                                      "LATITUDE"            FLOAT,
                                                                      "LONGITUDE"           FLOAT,
                                                                      "ALTITUDE"            FLOAT,
                                                                      "AREA"                FLOAT,
                                                                      "ANOINST"             VARCHAR(66),
                                                                      "ANOEXT"              VARCHAR(66),
                                                                      "SUCESSOR"            VARCHAR(66));

                       /*Tabela dos tipos de equipamentos*/
                       CREATE TABLE IF NOT EXISTS {child_db}.tipequip("ID"                  VARCHAR(2),
                                                                      "TIPO"                VARCHAR(66));

                       /*Tabela dos nomes dos equipamentos*/
                       CREATE TABLE IF NOT EXISTS {child_db}.codequip("ID"                  VARCHAR(2),
                                                                      "DENOMINACAO"         VARCHAR(66));

                       /*Tabela dos Estados da RFB*/
                       CREATE TABLE IF NOT EXISTS {child_db}.ufcod("ID"                     VARCHAR(2),
                                                                   "ESTADO"                 VARCHAR(66),
                                                                   "SIGLA_UF"               VARCHAR(66));

                       /*Tabela de Arquivos*/
                       CREATE TABLE IF NOT EXISTS {child_db}.arquivos("NOME"                VARCHAR(15),
                                                                      "DIRETORIO"           VARCHAR(66),
                                                                      "DATA_INSERCAO_FTP"   DATE,
                                                                      "DATA_HORA_CARGA"     TIMESTAMP,
                                                                      "QTD_REGISTROS"       INTEGER);

                ''')
    conn.commit()
    # Encerra o cursor
    cursor.close()
    # Encerra a conexão
    conn.close()
