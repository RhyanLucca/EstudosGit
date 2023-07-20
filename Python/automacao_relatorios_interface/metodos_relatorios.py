import pandas as pd
import mysql.connector
from datetime import datetime, date


db_dados = []


teste = True
tributacao = False

errorMessage = False
updateLOG = False


if teste == True:
    print("Ambiente de testes: ON")
    directory = r"C:/Users/rhyan.gaudino/Desktop/RhyanLucca/Automações Rhyan/Dados"
    log_directory = r"C:/Users/rhyan.gaudino/Desktop/RhyanLucca/Automações Rhyan/Dados"
else:
    print("Ambiente de testes: OFF")
    directory = r"K:/017 -  TI Desenvolvimento/BI/Dados"
    log_directory = r"X:/017/02 - Bots/AutomacaoRelatoriosEnv"
tributacaoPatchXlsx = f'{directory}/000-Franco/Consulta-Tributação.xlsx'

arquivoLOG = f'{log_directory}/LOG-Relatorios-Automaticos.txt'


#Franco-000

def atualizaTributacao():

    tributacaoPatchXlsx = f'{directory}/000-Franco/Consulta-Tributação.xlsx'
    
    con = mysql.connector.connect(
        user= db_dados[0],
        password= db_dados[1],
        host= db_dados[2],
        database= db_dados[3]
    )

    cursor = con.cursor()

    relatorio_nome = "Consulta-Tributação"

    print(f"Gerando relatório: {relatorio_nome}...")

    x = date.today()

    ano_atual = x.year

    intervalo4 = ano_atual-4

    intervalo3 = ano_atual-3

    intervalo2 = ano_atual-2

    intervalo1 = ano_atual-1

    ano_vig= 1987

    ano_alterado = ano_vig

    df = pd.DataFrame(columns=["Código", "2019", "2020", "2021", "2022", "2023"])

    query = '''SELECT DISTINCT trib.cadEmpresa as "Código"
    FROM tabtributacao as trib
    ORDER BY trib.cadEmpresa
    ;'''

    cursor.execute(query)

    lista = cursor.fetchall()

    print(f'Executando Query`s "{relatorio_nome}"...')


    for empresa in lista:
            
        cadEmpresa = empresa[0]
            
        lista_master = []
            
        lista_emp = []
            
        while ano_alterado < ano_atual+1:  
                    
            query_anual_ = f"""SELECT trib.cadID, trib.cadEmpresa as "Código", trib.cadTributacao, trib.cadVigencia           
            FROM tabtributacao as trib           
            WHERE trib.cadEmpresa= {cadEmpresa}           
            AND trib.cadVigencia LIKE "{ano_alterado}%";"""

            cursor.execute(query_anual_)

            lista_anual_ = cursor.fetchall()

            for r in lista_anual_:                    
                list_resultado = []  

                cadID = r[0]                    
                cadEmpresa = r[1]                    
                cadTributacao = r[2]                    
                cadDTAR = r[3]
                
                DTAR_string = str(cadDTAR)                    
                DTAR_string = DTAR_string[:4]                    
                DTAR_int = int(DTAR_string)
                #print(cadID,cadEmpresa)

            #cadTributacao = lista_anual_[2]

            if not lista_anual_:
            
                if ano_alterado in [intervalo4, intervalo3, intervalo2, intervalo1, ano_atual]:
            
                    lista_master.append(cadTributacao)
                
                else:
                    pass

            else:
                    
                #TRUE
                for r in lista_anual_:                    
                    list_resultado = []  

                    cadID = r[0]                    
                    cadEmpresa = r[1]                    
                    cadTributacao = r[2]                    
                    cadDTAR = r[3]
                    
                    DTAR_string = str(cadDTAR)                    
                    DTAR_string = DTAR_string[:4]                    
                    DTAR_int = int(DTAR_string)                    
                    list_resultado.append(cadID)

                getmax = max(list_resultado)
                    
                query_max_ = f"""SELECT trib.cadID, trib.cadEmpresa as "Código", trib.cadTributacao, trib.cadVigencia FROM tabtributacao as trib WHERE trib.cadID = {getmax};"""
                                        
                cursor.execute(query_max_)
                    
                lista_max = cursor.fetchall()

                for r in lista_max:
                        
                    list_resultado = []

                    cadID = r[0]                        
                    cadEmpresa = r[1]                        
                    cadTributacao = r[2]                        
                    cadDTAR = r[3] 
     
                    DTAR_string = str(cadDTAR)                        
                    DTAR_string = DTAR_string[:4]                        
                    DTAR_int = int(DTAR_string)
                        
                    if ano_alterado in [intervalo4, intervalo3, intervalo2, intervalo1, ano_atual]:                        
                        lista_master.append(cadTributacao)                        
                    else:                                            
                        pass
            
            ano_alterado = ano_alterado +1

        lista_emp.append(cadEmpresa)

        ano_alterado = ano_vig
   
        dfValores = pd.DataFrame([lista_master], columns=["2019", "2020", "2021", "2022", "2023"])
     
        dfEmpresas = pd.DataFrame([lista_emp], columns=["Código"])
        
        dfMERGE = dfEmpresas.join(dfValores)
          
        df = df._append(dfMERGE)

    df.to_excel(tributacaoPatchXlsx, sheet_name='Consulta Tributação', index=False)

    print(f'Convertendo arquivo "{relatorio_nome}"...')

    try:
                
        df.to_excel(tributacaoPatchXlsx, sheet_name='Consulta Tributação', index=False)

        data_dados = datetime.today()

        if errorMessage: #messagebox.showinfo("Relatório atualizado!", 'O relatório "Intranet-TimeSheet" foi atualizado com sucesso!') 
            print(f"Relatório atualizado!", f'O relatório "{relatorio_nome}" foi atualizado com sucesso!')

            if updateLOG:
                with open(arquivoLOG, "a") as arquivo:
                    data_atual = data_dados.strftime("%Y-%m-%d %H:%M")
                    arquivo.write(f'---{data_atual}---\nSUCCESS: Relatório "{relatorio_nome}" atualizado com sucesso.\n \n')

            print(f'O relatório "{relatorio_nome}" foi atualizado com sucesso!')

            print(f'Relatório "{relatorio_nome}" salvo em: {tributacaoPatchXlsx}')

    except PermissionError or FileNotFoundError or NameError as e:
                
        data_dados = datetime.today()

        if errorMessage: #messagebox.showerror("Erro no programa!", f'O relatório "Intranet-TimeSheet" não foi atualizado! {e}')
            print(f'Erro no programa! O relatório "{relatorio_nome}" não foi atualizado! Verifique se o arquivo está aberto {e}')     

        if updateLOG:
            with open(arquivoLOG, "a") as arquivo:
                data_atual = data_dados.strftime("%Y-%m-%d %H:%M")
                arquivo.write(f'---{data_atual}---\nFAILURE: Relatório "{relatorio_nome}" não foi atualizado.\n Erro {e}\n \n')

    except FileNotFoundError or TypeError or SyntaxError or NameError as e:
            
        data_dados = datetime.today()
                
        if errorMessage: #messagebox.showerror("Erro no programa!", f'Relatório "Intranet-TimeSheet" não foi atualizado.\n Erro {e}\n \n')
            print("Erro no programa!", f'Relatório "{relatorio_nome}" não foi atualizado.\n Erro {e}\n \n')

        if updateLOG:
            with open(arquivoLOG, "a") as arquivo:

                arquivo.write(f'---{data_atual}---\nFAILURE: Relatório "{relatorio_nome}" não foi atualizado.\n Erro {e}\n \n')


def atualizarEmpresas():

    con = mysql.connector.connect(
    user= db_dados[0],
    password= db_dados[1],
    host= db_dados[2],
    database= db_dados[3]
    )

    cursor = con.cursor()

    relatorio_nome = "Intranet-Empresas"

    print(f"Gerando relatório: {relatorio_nome}...")

    queryValorEmpresas = """SELECT emp.cadCodigo,	emp.cadClass1,	emp.cadCNPJ, 

CASE emp.cadPersonalidade  
WHEN '1' THEN 'Fisica' 
when '0' then IF(cadCNPJ LIKE "__________/0001%", 'Matriz', 'Filial' ) 
END AS cadPersonalidade, 

emp.cadTipo,	emp.cadRazaoFull,	grp.cadGrupo,	emp.cadNJuridica, emp.cadPorte,	emp.cadCNAE,	emp.cadCNAESecundario,	emp.cadIE, 
emp.cadIM, emp.cadPais,	emp.cadPaisSigla,	emp.cadCEP,	emp.cadUF, emp.cadCidade,	emp.cadBairro,	emp.cadIBGE,	emp.cadLogradouro, 
emp.cadEndereco, emp.cadNumero,	emp.cadComplemento,	emp.cadTelefone, emp.cadEmail,	emp.cadSite,	emp.cadAtividadeInicio,	
emp.cadRegistroNumero, emp.cadRegistroData,	emp.cadRegistroOrgao,	emp.cadRamo,	emp.cadContratoAlteracao, emp.cadContratoCapital,	
emp.cadContratoCota,	emp.cadReprNome,	emp.cadReprCPF, emp.cadReprCargo,	emp.cadReprNasc,	emp.cadReprRGNumero,	
emp.cadReprRGEmissao, emp.cadReprRGEmissor,	emp.cadReprRGUF,	emp.cadReprTelefone,	emp.cadReprEmail, emp.cadClass2,	
emp.cadAbertura,	emp.cadInicio,	emp.cadDTAR,	emp.cadDesligamento, emp.cadDesligTitulo,	emp.cadDesligMotivo,	 

CASE emp.cadTributacao 
WHEN 'N' THEN 'Não Definida' WHEN 'F' THEN 'Pessoa Física' WHEN 'S' THEN 'Simples' WHEN 'I' THEN 'Inativa' 
WHEN '0' THEN 'Lucro Real Trimestral' WHEN '1' THEN 'Lucro Presumido' WHEN '2' THEN 'Lucro Real Anual' 
WHEN '3' THEN 'SIMPLES-ME' WHEN '4' THEN 'SIMPLES-EPP' WHEN '5' THEN 'Lucro Arbitrado' WHEN '6' THEN 'Imune' 
WHEN '7' THEN 'Isenta' WHEN '8' THEN 'MEI' END AS cadTributacao, emp.cadObs,
	
CASE emp.cadStatus 
WHEN '0' THEN 'Ativa' WHEN '1' THEN 'Desligada' WHEN '2' THEN 'Pendente' END AS cadStatus 

FROM tabsocempresas as emp
LEFT JOIN tabsocgrupo as grp
ON emp.cadGrupo = grp.cadID
;
"""
    empresasPathXlsx = f'{directory}/000-Franco/Intranet-Empresas.xlsx'

    cursor.execute(queryValorEmpresas)

    print(f'Executando Query`s "{relatorio_nome}"...')


    print(f'Convertendo arquivo "{relatorio_nome}"...')

    lista = cursor.fetchall()

    for r in range(0, len(lista)):              
            if r == "NULL":
                    r = (str(''))
                    

    lista = pd.DataFrame(lista, columns=["Código",	"Class.",	"CNPJ/CPF",	"Pers.",	"Tipo",
        "Razão Social",	"Grupo",	"Natureza Jurídica",	"Porte",	"CNAE",	"CNAE Secundario",	"Inscrição Estadual",
        "Inscrição Municipal",	"Código Pais",	"Pais Sigla",	"CEP",	"UF",	"Município",	"Bairro",	"IBGE",	
        "Logradouro",	"Endereço", "Número",	"Complemento",	"Telefone",	"E-mail",	"Site",	"Início Atividade",
        "Registro número",	"Registro data"	,
        "Registro orgão",	"Ramo",	"Contrato alteração",	"Contrato capital",	"Contrato cota",	"Representante Nome",	
        "Representante CPF",	"Representante Cargo",	"Representante Nascimento",	"Representante RG"	,
        "Representante Emissão",	"Representante Emissor",	"Representante UF",	"Representante Telefone",	
        "Representante Email",	"Class2",	"Abertura",	"Início Franco",	"Inclusão",	"Data de desligamento",	
        "Título de desligamento",	"Motivo do desligamento",	"Tributação Atual",	"Observação",	"Status"])
            
    try:
        lista.to_excel(empresasPathXlsx, sheet_name='Empresas', index=False)

        data_dados = datetime.today()

        if errorMessage:

            print(f'O relatório "{relatorio_nome}" foi atualizado com sucesso!')

        if updateLOG:
                    
            with open(arquivoLOG, "a") as arquivo:
                data_atual = data_dados.strftime("%Y-%m-%d %H:%M")
                arquivo.write(f'---{data_atual}---\nSUCCESS: Relatório "{relatorio_nome}" atualizado com sucesso.\n \n')

        print(f'Relatório "{relatorio_nome}" salvo em: {empresasPathXlsx}')

    except PermissionError or FileNotFoundError or NameError as e:
                        
        data_dados = datetime.today()
        print(f'O relatório "{relatorio_nome}" não foi atualizado! {e}')

        if errorMessage: #messagebox.showerror("Erro no programa!", 'O relatório "Intranet Desligamentos" não foi atualizado! Verifique se o arquivo está aberto')
             print(f'Erro no programa! O relatório "{relatorio_nome}" não foi atualizado! Verifique se o arquivo está aberto {e}')     

        if updateLOG:
            with open(arquivoLOG, "a") as arquivo:
                    data_atual = data_dados.strftime("%Y-%m-%d %H:%M")
                    arquivo.write(f'---{data_atual}---\nFAILURE: Relatório "{relatorio_nome}" não foi atualizado.\n Erro {e}\n \n')

    except FileNotFoundError or TypeError or SyntaxError or NameError as e:
        data_atual = datetime.today()

        if errorMessage: #messagebox.showerror("Erro no programa!", f'Relatório "Intranet Desligamentos" não foi atualizado.\n Erro {e}\n \n')
            print(f'Erro no programa! O relatório "{relatorio_nome}" não foi atualizado! Verifique se o arquivo está aberto {e}')     

        if updateLOG:
                with open(arquivoLOG, "a") as arquivo:
                        arquivo.write(f'---{data_atual}---\nFAILURE: Relatório "{relatorio_nome}" não foi atualizado.\n Erro {e}\n \n')

    else:
        pass


def atualizarResponsaveis():
                
    con = mysql.connector.connect(
    user= db_dados[0],
    password= db_dados[1],
    host= db_dados[2],
    database= db_dados[3]
    )

    cursor = con.cursor()

    relatorio_nome = "Intranet-Responsáveis"

    responsaveisPathXlsx= f'{directory}/000-Franco/Intranet-Responsáveis.xlsx'

    queryContador= 0
    queryValorResponsaveis= f"""SELECT 
                distinct resp.cadDepto, emp.cadCodigo as CODEmpresa, emp.cadRazao, emp.cadCNPJ, emp.cadClass1, emp.cadGrupo, 
                '' as Tributação, emp.cadStatus,

                (SELECT usr.cadNick 
                    FROM intranetdb.tabctbresponsaveis AS resp 
                    LEFT JOIN intranetdb.tabusers AS usr 
                    ON resp.cadColaborador = usr.cadID
                    WHERE resp.cadCodigo = emp.cadCodigo 
                    AND resp.cadNivel=1
                    AND resp.cadStatus=0 
                    AND resp.cadDepto ={queryContador}
                    ) as Resp1,
                    
                (SELECT usr.cadNick 
                    FROM intranetdb.tabctbresponsaveis AS resp 
                    LEFT JOIN intranetdb.tabusers AS usr 
                    ON resp.cadColaborador = usr.cadID
                    WHERE resp.cadCodigo = emp.cadCodigo 
                    AND resp.cadNivel=2
                    AND resp.cadStatus=0 
                    AND resp.cadDepto ={queryContador}
                    ) as Resp2,
                    
                (SELECT usr.cadNick 
                    FROM intranetdb.tabctbresponsaveis AS resp 
                    LEFT JOIN intranetdb.tabusers AS usr 
                    ON resp.cadColaborador = usr.cadID
                    WHERE resp.cadCodigo = emp.cadCodigo 
                    AND resp.cadNivel=3
                    AND resp.cadStatus=0 
                    AND resp.cadDepto ={queryContador}
                    ) as Resp3,
                    
                (SELECT usr.cadNick 
                    FROM intranetdb.tabctbresponsaveis AS resp 
                    LEFT JOIN intranetdb.tabusers AS usr 
                    ON resp.cadColaborador = usr.cadID
                    WHERE resp.cadCodigo = emp.cadCodigo 
                    AND resp.cadNivel=4
                    AND resp.cadStatus=0 
                    AND resp.cadDepto ={queryContador}
                    ) as Resp4,
                    
                (SELECT usr.cadNick 
                    FROM intranetdb.tabctbresponsaveis AS resp 
                    LEFT JOIN intranetdb.tabusers AS usr 
                    ON resp.cadColaborador = usr.cadID
                    WHERE resp.cadCodigo = emp.cadCodigo 
                    AND resp.cadNivel=5
                    AND resp.cadStatus=0 
                    AND resp.cadDepto ={queryContador}
                    ) as Resp5

                FROM tabsocempresas as emp
                INNER JOIN tabctbresponsaveis as resp
                ON resp.cadCodigo = emp.cadCodigo
                and resp.cadDepto = {queryContador}
                and emp.cadStatus = 0
                ;"""

    print(f'Executando Query`s "{relatorio_nome}"...')

    print(f'Convertendo arquivo "{relatorio_nome}"...')


    queryCont = queryContador
    queryContador= 0

    lista2 = pd.DataFrame(columns= ["Dpto", "Cód.",	 "Razão Social",	 "CNPJ/CPF",	 "Class",	 "Grupo",	 "Trib.",	 "Status",	 "Resp.1",	 "Resp.2",	 "Resp.3",	 "Resp.4",	 "Resp.5"])

    while queryContador < 10:
               
        try:
            queryValorResponsaveis= f"""SELECT 
                    distinct resp.cadDepto, emp.cadCodigo as CODEmpresa, emp.cadRazao, emp.cadCNPJ, emp.cadClass1, grp.cadGrupo, 
                    '' as Tributação, CASE  
                    when emp.cadStatus = 0 THEN 'Ativa'
                    end as cadStatus,

                    (SELECT usr.cadNick 
                        FROM intranetdb.tabctbresponsaveis AS resp 
                        LEFT JOIN intranetdb.tabusers AS usr 
                        ON resp.cadColaborador = usr.cadID
                        WHERE resp.cadCodigo = emp.cadCodigo 
                        AND resp.cadNivel=1
                        AND resp.cadStatus=0 
                        AND resp.cadDepto ={queryContador}
                        ) as Resp1,
                        
                    (SELECT usr.cadNick 
                        FROM intranetdb.tabctbresponsaveis AS resp 
                        LEFT JOIN intranetdb.tabusers AS usr 
                        ON resp.cadColaborador = usr.cadID
                        WHERE resp.cadCodigo = emp.cadCodigo 
                        AND resp.cadNivel=2
                        AND resp.cadStatus=0 
                        AND resp.cadDepto ={queryContador}
                        ) as Resp2,
                        
                    (SELECT usr.cadNick 
                        FROM intranetdb.tabctbresponsaveis AS resp 
                        LEFT JOIN intranetdb.tabusers AS usr 
                        ON resp.cadColaborador = usr.cadID
                        WHERE resp.cadCodigo = emp.cadCodigo 
                        AND resp.cadNivel=3
                        AND resp.cadStatus=0 
                        AND resp.cadDepto ={queryContador}
                        ) as Resp3,
                        
                    (SELECT usr.cadNick 
                        FROM intranetdb.tabctbresponsaveis AS resp 
                        LEFT JOIN intranetdb.tabusers AS usr 
                        ON resp.cadColaborador = usr.cadID
                        WHERE resp.cadCodigo = emp.cadCodigo 
                        AND resp.cadNivel=4
                        AND resp.cadStatus=0 
                        AND resp.cadDepto ={queryContador}
                        ) as Resp4,
                        
                    (SELECT usr.cadNick 
                        FROM intranetdb.tabctbresponsaveis AS resp 
                        LEFT JOIN intranetdb.tabusers AS usr 
                        ON resp.cadColaborador = usr.cadID
                        WHERE resp.cadCodigo = emp.cadCodigo 
                        AND resp.cadNivel=5
                        AND resp.cadStatus=0 
                        AND resp.cadDepto ={queryContador}
                        ) as Resp5

                    FROM tabsocempresas as emp
                    INNER JOIN tabctbresponsaveis as resp
                    INNER JOIN tabsocgrupo AS grp

                    ON resp.cadCodigo = emp.cadCodigo
                    AND resp.cadDepto = {queryContador}
                    AND emp.cadStatus = 0
                    AND grp.cadID = emp.cadGrupo
                    ;"""

            cursor.execute(queryValorResponsaveis)
                
            lista = cursor.fetchall() 

            queryContador +=1

            lista = pd.DataFrame(lista, columns= ["Dpto", "Cód.",	 "Razão Social",	 "CNPJ/CPF",	 "Class",	 "Grupo",	 "Trib.",	 "Status",	 "Resp.1",	 "Resp.2",	 "Resp.3",	 "Resp.4",	 "Resp.5"])

            lista2 = lista2._append(lista, ignore_index = True)

        except UnboundLocalError as e:
            print(f'No values in {queryContador}')

    try:

        lista2.to_excel(responsaveisPathXlsx, sheet_name='Responsaveis', index=False)

        data_dados = datetime.today()

        if errorMessage:

            print(f'O relatório "{relatorio_nome}" foi atualizado com sucesso!')

        if updateLOG:
                    
            with open(arquivoLOG, "a") as arquivo:
                data_atual = data_dados.strftime("%Y-%m-%d %H:%M")
                arquivo.write(f'---{data_atual}---\nSUCCESS: Relatório "{relatorio_nome}" atualizado com sucesso.\n \n')

                print(f'Relatório "{relatorio_nome}" salvo em: {responsaveisPathXlsx}')

    except PermissionError or FileNotFoundError or NameError as e:
                        
        data_dados = datetime.today()
        print(f'O relatório "{relatorio_nome}" não foi atualizado! {e}')

        if errorMessage: #messagebox.showerror("Erro no programa!", 'O relatório "Intranet Desligamentos" não foi atualizado! Verifique se o arquivo está aberto')
             print(f'Erro no programa! O relatório "{relatorio_nome}" não foi atualizado! Verifique se o arquivo está aberto {e}')     

        if updateLOG:
            with open(arquivoLOG, "a") as arquivo:
                    data_atual = data_dados.strftime("%Y-%m-%d %H:%M")
                    arquivo.write(f'---{data_atual}---\nFAILURE: Relatório "{relatorio_nome}" não foi atualizado.\n Erro {e}\n \n')

    except FileNotFoundError or TypeError or SyntaxError or NameError as e:
        data_atual = datetime.today()

        if errorMessage: #messagebox.showerror("Erro no programa!", f'Relatório "Intranet Desligamentos" não foi atualizado.\n Erro {e}\n \n')
            print(f'Erro no programa! O relatório "{relatorio_nome}" não foi atualizado! Verifique se o arquivo está aberto {e}')     

        if updateLOG:
                with open(arquivoLOG, "a") as arquivo:
                        arquivo.write(f'---{data_atual}---\nFAILURE: Relatório "{relatorio_nome}" não foi atualizado.\n Erro {e}\n \n')


def atualizarWorkFlow():

    workFlowPathCsv= f'{directory}/000-Franco/Intranet-Workflow Porcentagem.csv'

    queryValorWorkFlow= """select * from tabctbworkflowporcentagem
    WHERE cadAno
    > "2021";"""

    con = mysql.connector.connect(
    user= db_dados[0],
    password= db_dados[1],
    host= db_dados[2],
    database= db_dados[3]
    )

    cursor = con.cursor()
            
    relatorio_nome = "Intranet-Workflow Porcentagem"
     
    print(f"Gerando relatório: {relatorio_nome}...")

    workFlowPathCsv= f'{directory}/000-Franco/Intranet-Workflow Porcentagem.csv'

    queryValorWorkFlow= """select * from tabctbworkflowporcentagem
    WHERE cadAno
    > "2021";"""
        
    cursor.execute(queryValorWorkFlow)

    print(f"Executando Query`s {relatorio_nome}...")

    

    print(f"Convertendo arquivo {relatorio_nome}...")

    lista = cursor.fetchall()

    for r in range(0, len(lista)):               
        if r == "NULL":
            r = (str(''))

        lista = pd.DataFrame(lista, columns=["cadID","cadCodigo","cadDepto","cadAno",
                                                       "cadWF01","cadWF02","cadWF03","cadWF04","cadWF05","cadWF06","cadWF07","cadWF08","cadWF09","cadWF10",
                                                       "cadWF11","cadWF12","cadUpdate"])
        #lista = pd.DataFrame(lista, columns=["cadCodigo","cadDepto","cadUserR","cadStatus","cadAcao","cadDescricao","cadPeriodo","cadID"])

    try:
        lista.to_csv(workFlowPathCsv, sep=";", index=False, encoding="latin-1")

        data_dados = datetime.today()

        if errorMessage: #messagebox.showinfo("Relatório atualizado!", 'O relatório "Suporte Infra" foi atualizado com sucesso!') 
            print(f'O relatório "{relatorio_nome}" foi atualizado com sucesso!')
            
        if updateLOG:
                        with open(arquivoLOG, "a") as arquivo:
                                data_atual = data_dados.strftime("%Y-%m-%d %H:%M")
                                arquivo.write(f'---{data_atual}---\nSUCCESS: Relatório "{relatorio_nome}" atualizado com sucesso.\n \n')

                                print(f'Relatório "{relatorio_nome}" salvo em: {workFlowPathCsv}')


    except PermissionError or FileNotFoundError or NameError as e:
                        
        data_dados = datetime.today()
        print(f'O relatório "{relatorio_nome}" não foi atualizado! {e}')
        if errorMessage: #messagebox.showerror("Erro no programa!", 'O relatório "Suporte Infra" não foi atualizado! Verifique se o arquivo está aberto')
            print(f'Erro no programa! O relatório "{relatorio_nome}" não foi atualizado! Verifique se o arquivo está aberto {e}')     

        if updateLOG:
            with open(arquivoLOG, "a") as arquivo:
                    data_atual = data_dados.strftime("%Y-%m-%d %H:%M")
                    arquivo.write(f'---{data_atual}---\nFAILURE: Relatório "{relatorio_nome}" não foi atualizado.\n Erro {e}\n \n')


    except FileNotFoundError or TypeError or SyntaxError or NameError as e:
                
        data_atual = datetime.today()
                
        if errorMessage: #messagebox.showerror("Erro no programa!", f'Relatório "Suporte Infra TI" não foi atualizado.\n Erro {e}\n \n')
            print(f'Erro no programa! O relatório "{relatorio_nome}" não foi atualizado! Verifique se o arquivo está aberto {e}')     
                

        if updateLOG:
            with open(arquivoLOG, "a") as arquivo:
                    arquivo.write(f'---{data_atual}---\nFAILURE: Relatório "{relatorio_nome}" não foi atualizado.\n Erro {e}\n \n')


#Comercial-006

def atualizarDesligamentos():

    con = mysql.connector.connect(
    user= db_dados[0],
    password= db_dados[1],
    host= db_dados[2],
    database= db_dados[3]
    )

    cursor = con.cursor()

    relatorio_nome = "Intranet-Desligamentos"

    print(f'Gerando relatório: "{relatorio_nome}"...')

    desligamentoPathCsv= f'{directory}/006-Comercial/Intranet-Desligamentos.csv'
    queryValorDesligamento= """SELECT  tabsocempresas.cadCodigo, tabcomdesligamento.cadTipo, 
tabcomdesligamento.cadSubTipo FROM intranetdb.tabcomdesligamento INNER JOIN intranetdb.tabsocempresas ON 
intranetdb.tabcomdesligamento.cadGrupo = intranetdb.tabsocempresas.cadGrupo  AND  
intranetdb.tabcomdesligamento.cadDesligamento = intranetdb.tabsocempresas.cadDesligamento; """
                
                
    cursor.execute(queryValorDesligamento)

    print(f'Executando Query`s "{relatorio_nome}"...')
            
    print(f'Convertendo arquivo "{relatorio_nome}"...')

    lista = cursor.fetchall()

    for r in range(0, len(lista)):
        if r == "NULL":
                r = (str(''))


    lista = pd.DataFrame(lista, columns=["cadCodigo",	"cadTipo",	"cadSubTipo"])

            
    try:

        lista.to_csv(desligamentoPathCsv, sep=";", index=False, encoding="latin-1")

        data_dados = datetime.today()

        if errorMessage: #messagebox.showinfo("Relatório atualizado!", 'O relatório "Intranet Desligamentos" foi atualizado com sucesso!') 

            print(f'O relatório "{relatorio_nome}" foi atualizado com sucesso!')

        if updateLOG:

                with open(arquivoLOG, "a") as arquivo:
                    data_atual = data_dados.strftime("%Y-%m-%d %H:%M")
                    arquivo.write(f'---{data_atual}---\nSUCCESS: Relatório "{relatorio_nome}" atualizado com sucesso.\n \n')

        print(f'Relatório "{relatorio_nome}" salvo em: {desligamentoPathCsv}')

    except PermissionError or FileNotFoundError or NameError as e:
                                
        data_dados = datetime.today()
        print(f'O relatório "{relatorio_nome}" não foi atualizado! {e}')
        if errorMessage: #messagebox.showerror("Erro no programa!", 'O relatório "Intranet Desligamentos" não foi atualizado! Verifique se o arquivo está aberto')
             print(f'Erro no programa! O relatório "{relatorio_nome}" não foi atualizado! Verifique se o arquivo está aberto {e}')     

        if updateLOG:
            with open(arquivoLOG, "a") as arquivo:
                    data_atual = data_dados.strftime("%Y-%m-%d %H:%M")
                    arquivo.write(f'---{data_atual}---\nFAILURE: Relatório "{relatorio_nome}" não foi atualizado.\n Erro {e}\n \n')




    except FileNotFoundError or TypeError or SyntaxError or NameError as e:
        data_atual = datetime.today()

        if errorMessage: #messagebox.showerror("Erro no programa!", f'Relatório "Intranet Desligamentos" não foi atualizado.\n Erro {e}\n \n')
            print(f'Erro no programa! O relatório "{relatorio_nome}" não foi atualizado! Verifique se o arquivo está aberto {e}')     

        if updateLOG:
                with open(arquivoLOG, "a") as arquivo:
                        arquivo.write(f'---{data_atual}---\nFAILURE: Relatório "{relatorio_nome}" não foi atualizado.\n Erro {e}\n \n')


#007-TI Infra

def atualizarDescarte():
            
    con = mysql.connector.connect(
    user= db_dados[0],
    password= db_dados[1],
    host= db_dados[2],
    database= db_dados[3]
    )

    cursor = con.cursor()

    relatorio_nome = "Intranet-Descarte"
            
    print(f"Gerando relatório: {relatorio_nome}...")

    descartePathXlsx= f'{directory}/007-TI Infra/Intranet-Descarte.xlsx'
    queryValorDescarte= """SELECT descarte.cadId as "ID",
    descarte.cadNome AS "Nome",
    descarte.cadTipo AS "Tipo",
    descarte.cadMarca AS "Marca",
    descarte.cadModelo AS "Modelo",
    descarte.cadDescarte AS "Descarte",
    descarte.cadPersonalidade AS "Pers.",
    descarte.cadTerceiro AS "Terceiro",
    descarte.cadValor AS "Valor",
    cadIDRegistro AS "Registrado por",
    descarte.cadDTar AS "Registrado em",
    CASE
    WHEN descarte.cadStatus = 0 THEN "Descartado"
    END AS "Status" 
    from tabcpddescarte AS descarte
    ;
    """

    cursor.execute(queryValorDescarte)

    print(f"Executando Query`s {relatorio_nome}...")


    print(f"Convertendo arquivo {relatorio_nome}")

    lista = cursor.fetchall()

    for r in range(0, len(lista)):              
            if r == "NULL":
                    r = (str(''))
                    

    lista = pd.DataFrame(lista, columns=["ID",	
                                                   "Nome",	
                                                   "Tipo",
                                                   "Marca",	
                                                   "Modelo",	
                                                   "Descarte",
                                                   "Pers.",
                                                   "Terceiro",
                                                   "Valor",
                                                   "Registrado por",
                                                   "Registrado em",
                                                   "Status"
])
            
    try:
        lista.to_excel(descartePathXlsx, sheet_name='Descarte', index=False)

        data_dados = datetime.today()

        if errorMessage:

            print(f'O relatório "{relatorio_nome}" foi atualizado com sucesso!')

        if updateLOG:
                    
            with open(arquivoLOG, "a") as arquivo:
                data_atual = data_dados.strftime("%Y-%m-%d %H:%M")
                arquivo.write(f'---{data_atual}---\nSUCCESS: Relatório "{relatorio_nome}" atualizado com sucesso.\n \n')

                print(f'Relatório "{relatorio_nome}" salvo em: {descartePathXlsx}')

    except PermissionError or FileNotFoundError or NameError as e:
                        
        data_dados = datetime.today()
        print(f'O relatório "{relatorio_nome}" não foi atualizado! {e}')

        if errorMessage: #messagebox.showerror("Erro no programa!", 'O relatório "Intranet Desligamentos" não foi atualizado! Verifique se o arquivo está aberto')
             print(f'Erro no programa! O relatório "{relatorio_nome}" não foi atualizado! Verifique se o arquivo está aberto {e}')     

        if updateLOG:
            with open(arquivoLOG, "a") as arquivo:
                    data_atual = data_dados.strftime("%Y-%m-%d %H:%M")
                    arquivo.write(f'---{data_atual}---\nFAILURE: Relatório "{relatorio_nome}" não foi atualizado.\n Erro {e}\n \n')

    except FileNotFoundError or TypeError or SyntaxError or NameError as e:
        data_atual = datetime.today()

        if errorMessage: #messagebox.showerror("Erro no programa!", f'Relatório "Intranet Desligamentos" não foi atualizado.\n Erro {e}\n \n')
            print(f'Erro no programa! O relatório "{relatorio_nome}" não foi atualizado! Verifique se o arquivo está aberto {e}')     

        if updateLOG:
                with open(arquivoLOG, "a") as arquivo:
                        arquivo.write(f'---{data_atual}---\nFAILURE: Relatório "{relatorio_nome}" não foi atualizado.\n Erro {e}\n \n')


def atualizarMaquinas():

    con = mysql.connector.connect(
    user= db_dados[0],
    password= db_dados[1],
    host= db_dados[2],
    database= db_dados[3]
    )

    cursor = con.cursor()

    relatorio_nome = "Intranet-Maquinas"

    print(f"Gerando relatório: {relatorio_nome}")

    maquinasPathXlsx= f'{directory}/007-TI Infra/Intranet-Maquinas.xlsx'
    queryValorMaquinas = """SELECT 
	cadID as "ID",
	cadLocal as "Local",
    cadMAQ as "Maquina",
    cadTipo as "Tipo",
    cadDepto as "Depto",
    #cadColaborador as "Colaborador Atual",
    case 
    when cadColaborador = 0 then "VAGO"
    when cadColaborador != 0 then cadColaborador
    END AS "Colaborador Atual",
    cadSO as "S.O.",
    cadCPU as "Processador",
    cadModelo as "Modelo",
    cadRAM as "RAM",
    cadDiscoRigido as "Disco Rigido",
    cadHDD as "Capacidade",
    cadAntiVirus as "Antivirus",
    cadNF as "NF",
    cadFornecedor as "Fornecedor",
    cadLw as "Licença Windows",
    cadLo as "Licença Office",
    cadAquisicao as "Aquisição",
    cadDTAR as "Alteração"
FROM intranetdb.tabcpdmaquinas;"""

            
    cursor.execute(queryValorMaquinas)

    print(f"Executando Query`s {relatorio_nome}...")

    print(f"Convertendo arquivo {relatorio_nome}")

    lista = cursor.fetchall()

    for r in range(0, len(lista)):              
            if r == "NULL":
                    r = (str(''))
                    

    lista = pd.DataFrame(lista, columns=["ID",	
                                                   "Local",	
                                                   "Maquina",	
                                                   "Tipo",	
                                                   "Depto",	
                                                   "Colaborador Atual",
                                                   "S.O.",	
                                                   "Processador",	
                                                   "Modelo",	
                                                   "RAM",	
                                                   "Disco Rigido",	
                                                   "Capacidade",	
                                                   "Antivirus",	
                                                   "NF",	
                                                   "Fornecedor",	
                                                   "Licença Windows",	
                                                   "Licença Office",	
                                                   "Aquisição",	
                                                   "Alteração",
])
            
    try:
        lista.to_excel(maquinasPathXlsx, sheet_name='Maquinas', index=False)

        data_dados = datetime.today()

        if errorMessage:

            print(f'O relatório "{relatorio_nome}" foi atualizado com sucesso!')

        if updateLOG:
                    
            with open(arquivoLOG, "a") as arquivo:
                data_atual = data_dados.strftime("%Y-%m-%d %H:%M")
                arquivo.write(f'---{data_atual}---\nSUCCESS: Relatório "{relatorio_nome}" atualizado com sucesso.\n \n')

        print(f'Relatório "{relatorio_nome}" salvo em: {maquinasPathXlsx}')

    except PermissionError or FileNotFoundError or NameError as e:
                        
        data_dados = datetime.today()
        print(f'O relatório "{relatorio_nome}" não foi atualizado! {e}')

        if errorMessage: #messagebox.showerror("Erro no programa!", 'O relatório "Intranet Desligamentos" não foi atualizado! Verifique se o arquivo está aberto')
             print(f'Erro no programa! O relatório "{relatorio_nome}" não foi atualizado! Verifique se o arquivo está aberto {e}')     

        if updateLOG:
            with open(arquivoLOG, "a") as arquivo:
                    data_atual = data_dados.strftime("%Y-%m-%d %H:%M")
                    arquivo.write(f'---{data_atual}---\nFAILURE: Relatório "{relatorio_nome}" não foi atualizado.\n Erro {e}\n \n')

    except FileNotFoundError or TypeError or SyntaxError or NameError as e:
        data_atual = datetime.today()

        if errorMessage: #messagebox.showerror("Erro no programa!", f'Relatório "Intranet Desligamentos" não foi atualizado.\n Erro {e}\n \n')
            print(f'Erro no programa! O relatório "{relatorio_nome}" não foi atualizado! Verifique se o arquivo está aberto {e}')     

        if updateLOG:
                with open(arquivoLOG, "a") as arquivo:
                        arquivo.write(f'---{data_atual}---\nFAILURE: Relatório "{relatorio_nome}" não foi atualizado.\n Erro {e}\n \n')


def atualizarServidores():

    con = mysql.connector.connect(
    user= db_dados[0],
    password= db_dados[1],
    host= db_dados[2],
    database= db_dados[3]
    )

    cursor = con.cursor()
            
    relatorio_nome = "Intranet-Servidores"

    print(f"Gerando relatório: {relatorio_nome}")

    servidoresPathXlsx= f'{directory}/007-TI Infra/Intranet-Servidores.xlsx'
    queryValorServidores = """SELECT cadID as ID, 
cadNome as "Nome", 
cadMarca as "Marca",
cadModelo as "Modelo", 
cadSerie as "Série", 
cadSO as "S.O", 
cadHDD as "Disco Rigido", 
cadMemoria as "RAM",
cadIPExterno as "IP Externo",
cadIPFixo as "IP Fixo",
cadAquisicao as "Aquisição",
cadGarantia as "Garantia",
cadEstacoes as "Estações",
cadInternet as "Internet",
cadLW as "Licença Windows",
cadLSB as "Licença LSB",
cadPreventiva as "Preventivo",
cadObs as "Observação" 
from tabcpdservidores
WHERE cadStatus =0;"""


            
    cursor.execute(queryValorServidores)

    print(f"Executando Query`s {relatorio_nome}...")

    print(f"Convertendo arquivo {relatorio_nome}")

    lista = cursor.fetchall()

    for r in range(0, len(lista)):              
            if r == "NULL":
                    r = (str(''))
                    

    lista = pd.DataFrame(lista, columns=["ID",	
                                                   "Nome",	
                                                   "Marca",	
                                                   "Modelo",	
                                                   "Série",	
                                                   "S.O",
                                                   "Disco Rigido",	
                                                   "RAM",	
                                                   "IP Externo",	
                                                   "IP Fixo",	
                                                   "Aquisição",	
                                                   "Garantia",	
                                                   "Estações",	
                                                   "Internet",	
                                                   "Licença Windows",	
                                                   "Licença LSB",	
                                                   "Preventivo",	
                                                   "Observação",
])
            
    try:
        lista.to_excel(servidoresPathXlsx, sheet_name='Servidores', index=False)

        data_dados = datetime.today()

        if errorMessage:

            print(f'O relatório "{relatorio_nome}" foi atualizado com sucesso!')

        if updateLOG:
                    
            with open(arquivoLOG, "a") as arquivo:
                data_atual = data_dados.strftime("%Y-%m-%d %H:%M")
                arquivo.write(f'---{data_atual}---\nSUCCESS: Relatório "{relatorio_nome}" atualizado com sucesso.\n \n')

        print(f'Relatório "{relatorio_nome}" salvo em: {servidoresPathXlsx}')

    except PermissionError or FileNotFoundError or NameError as e:
                        
        data_dados = datetime.today()
        print(f'O relatório "{relatorio_nome}" não foi atualizado! {e}')

        if errorMessage: #messagebox.showerror("Erro no programa!", 'O relatório "Intranet Desligamentos" não foi atualizado! Verifique se o arquivo está aberto')
             print(f'Erro no programa! O relatório "{relatorio_nome}" não foi atualizado! Verifique se o arquivo está aberto {e}')     

        if updateLOG:
            with open(arquivoLOG, "a") as arquivo:
                    data_atual = data_dados.strftime("%Y-%m-%d %H:%M")
                    arquivo.write(f'---{data_atual}---\nFAILURE: Relatório "{relatorio_nome}" não foi atualizado.\n Erro {e}\n \n')

    except FileNotFoundError or TypeError or SyntaxError or NameError as e:
        data_atual = datetime.today()

        if errorMessage: #messagebox.showerror("Erro no programa!", f'Relatório "Intranet Desligamentos" não foi atualizado.\n Erro {e}\n \n')
            print(f'Erro no programa! O relatório "{relatorio_nome}" não foi atualizado! Verifique se o arquivo está aberto {e}')     

        if updateLOG:
                with open(arquivoLOG, "a") as arquivo:
                        arquivo.write(f'---{data_atual}---\nFAILURE: Relatório "{relatorio_nome}" não foi atualizado.\n Erro {e}\n \n')


def atualizarSuporteInfra():

    con = mysql.connector.connect(
    user= db_dados[0],
    password= db_dados[1],
    host= db_dados[2],
    database= db_dados[3]
    )

    cursor = con.cursor()
            
    relatorio_nome = "Intranet-Suporte"
            
    print(f"Gerando relatório: {relatorio_nome}...")

    suportePathCsv= f'{directory}/007-TI Infra/Intranet-Suporte.csv'
    queryValorInfra= """SELECT  cadID, cadTitulo, cadUserR, cadNome, cadDTAR, cadDepto, cadStatus, cadDTecnica, 
    cadDData, cadDUser, cadDNome, cadPrioridade, cadRating, cadComentario, cadDTAvaliar, cadUpload FROM 
    intranetdb.tabcpdsolicitacoes; """

                
    cursor.execute(queryValorInfra)

    print(f"Executando Query`s {relatorio_nome}...")


    print(f"Convertendo arquivo {relatorio_nome}...")

    lista = cursor.fetchall()

    for r in range(0, len(lista)):              
        if r == "NULL":
                r = (str(''))

    lista = pd.DataFrame(lista, columns=["cadID",	"cadTitulo",	"cadUserR",	"cadNome", "cadDTAR",	
        "cadDepto",	"cadStatus",	"cadDTecnica",	"cadDData",	
        "cadDUser",	"cadDNome",	"cadPrioridade",	"cadRating",	
        "cadComentario", "cadDTAvaliar", "cadUpload"])


    try:
        lista.to_csv(suportePathCsv, sep=";", index=False, encoding="latin-1")

        data_dados = datetime.today()

        if errorMessage: #messagebox.showinfo("Relatório atualizado!", 'O relatório "Suporte Infra" foi atualizado com sucesso!') 
            print(f'O relatório {relatorio_nome} foi atualizado com sucesso!')
            
        if updateLOG:
            with open(arquivoLOG, "a") as arquivo:
                    data_atual = data_dados.strftime("%Y-%m-%d %H:%M")
                    arquivo.write(f'---{data_atual}---\nSUCCESS: Relatório {relatorio_nome} atualizado com sucesso.\n \n')

                    print(f'Relatório {relatorio_nome} salvo em: {suportePathCsv}')


    except PermissionError or FileNotFoundError or NameError as e:
                        
        data_dados = datetime.today()
        print(f'O relatório {relatorio_nome} não foi atualizado! {e}')
        if errorMessage: #messagebox.showerror("Erro no programa!", 'O relatório "Suporte Infra" não foi atualizado! Verifique se o arquivo está aberto')
            print(f'Erro no programa! O relatório {relatorio_nome} não foi atualizado! Verifique se o arquivo está aberto {e}')     

        if updateLOG:
            with open(arquivoLOG, "a") as arquivo:
                    data_atual = data_dados.strftime("%Y-%m-%d %H:%M")
                    arquivo.write(f'---{data_atual}---\nFAILURE: Relatório {relatorio_nome} não foi atualizado.\n Erro {e}\n \n')


    except FileNotFoundError or TypeError or SyntaxError or NameError as e:
                
        data_atual = datetime.today()
                
        if errorMessage: #messagebox.showerror("Erro no programa!", f'Relatório "Suporte Infra TI" não foi atualizado.\n Erro {e}\n \n')
            print(f'Erro no programa! O relatório {relatorio_nome} não foi atualizado! Verifique se o arquivo está aberto {e}')     
                        

        if updateLOG:
            with open(arquivoLOG, "a") as arquivo:
                    arquivo.write(f'---{data_atual}---\nFAILURE: Relatório {relatorio_nome} não foi atualizado.\n Erro {e}\n \n')


#014 - Auditoria

def atualizarObrigacoes():
           
    con = mysql.connector.connect(
    user= db_dados[0],
    password= db_dados[1],
    host= db_dados[2],
    database= db_dados[3]
    )

    cursor = con.cursor()

    relatorio_nome = "Consulta-Obrigações"
            
    print(f"Gerando relatório: {relatorio_nome}...")

    obrigacoesPathCsv= f'{directory}/014-Auditoria/Consulta-Obrigações.csv'
    queryValorObrigacoes= """SELECT
TobgComp.cadEmpresa, 
Tobg.cadID as "ID Obriogação", 
Tobg.cadSigla "Obrigação", 
TobgComp.cadInicio, 
TobgComp.cadTermino, 
TobgPr.cadPrazo, 
TobgComp.cadTipo, 
TobgComp.cadDTAR, 
TobgComp.cadUserR, 
TobgComp.cadStatus, 
TobgComp.cadFolder 

FROM intranetdb.tabtriobrigacaocompetencia AS TobgComp
LEFT JOIN 
intranetdb.tabtriobrigacao AS Tobg 
ON TobgComp.cadObrigacao = Tobg.cadID 
LEFT JOIN 
intranetdb.tabtriobrigacaoprazo AS TobgPr 
ON TobgComp.cadObrigacao = TobgPr.cadIDRegistro 
AND TobgComp.cadInicio = TobgPr.cadInicio
;
"""

            
    cursor.execute(queryValorObrigacoes)

    print(f"Executando Query`s {relatorio_nome}...")

    print(f"Convertendo arquivo {relatorio_nome}...")

    lista = cursor.fetchall()

    for r in range(0, len(lista)):               
        if r == "NULL":
                r = (str(''))

    lista = pd.DataFrame(lista, columns=["cadEmpresa",
"ID Obrigação",
"Obrigação",
"cadInicio",
"cadTermino",
"cadPrazo",
"cadTipo",
"cadDTAR",
"cadUserR",
"cadStatus",
"cadFolder"])
                #lista = pd.DataFrame(lista, columns=["cadCodigo","cadDepto","cadUserR","cadStatus","cadAcao","cadDescricao","cadPeriodo","cadID"])

    try:
        lista.to_csv(obrigacoesPathCsv, sep=";", index=False, encoding="latin-1")

        data_dados = datetime.today()

        if errorMessage: #messagebox.showinfo("Relatório atualizado!", 'O relatório "Suporte Infra" foi atualizado com sucesso!') 
            print(f'O relatório "{relatorio_nome}" foi atualizado com sucesso!')
            
        if updateLOG:
            with open(arquivoLOG, "a") as arquivo:
                    data_atual = data_dados.strftime("%Y-%m-%d %H:%M")
                    arquivo.write(f'---{data_atual}---\nSUCCESS: Relatório "{relatorio_nome}" atualizado com sucesso.\n \n')

                    print(f'Relatório "{relatorio_nome}" salvo em: {obrigacoesPathCsv}')


    except PermissionError or FileNotFoundError or NameError as e:
                        
        data_dados = datetime.today()
        print(f'O relatório "{relatorio_nome}" não foi atualizado! {e}')
        if errorMessage: #messagebox.showerror("Erro no programa!", 'O relatório "Suporte Infra" não foi atualizado! Verifique se o arquivo está aberto')
            print(f'Erro no programa! O relatório "{relatorio_nome}" não foi atualizado! Verifique se o arquivo está aberto {e}')     

        if updateLOG:
            with open(arquivoLOG, "a") as arquivo:
                data_atual = data_dados.strftime("%Y-%m-%d %H:%M")
                arquivo.write(f'---{data_atual}---\nFAILURE: Relatório "{relatorio_nome}" não foi atualizado.\n Erro {e}\n \n')


    except FileNotFoundError or TypeError or SyntaxError or NameError as e:
                
        data_atual = datetime.today()
                
        if errorMessage: #messagebox.showerror("Erro no programa!", f'Relatório "Suporte Infra TI" não foi atualizado.\n Erro {e}\n \n')
            print(f'Erro no programa! O relatório "{relatorio_nome}" não foi atualizado! Verifique se o arquivo está aberto {e}')     
                

        if updateLOG:
            with open(arquivoLOG, "a") as arquivo:
                    arquivo.write(f'---{data_atual}---\nFAILURE: Relatório "{relatorio_nome}" não foi atualizado.\n Erro {e}\n \n')


#015 - Recursos Humanos

def atualizarTimeSheet():

    con = mysql.connector.connect(
    user= db_dados[0],
    password= db_dados[1],
    host= db_dados[2],
    database= db_dados[3]
    )

    cursor = con.cursor()

    relatorio_nome = "Intranet-TimeSheet"

    print(f"Gerando relatório: {relatorio_nome}...")

    timeSheetPathXlsx = f'{directory}/015-Recursos Humanos/Intranet-TimeSheet.xlsx'
    queryValorTimeSheet = '''SELECT  intranetdb.tabgrhtimesheet.cadID, intranetdb.tabgrhtimesheet.cadAtividade, 
intranetdb.tabgrhtimesheet.cadEmpresa, intranetdb.tabgrhtimesheetatividades.cadPeso, 
intranetdb.tabgrhtimesheet.cadCompetencia, intranetdb.tabgrhtimesheet.cadProjeto, 
intranetdb.tabgrhtimesheet.cadInicio, intranetdb.tabgrhtimesheet.cadTermino, 
intranetdb.tabgrhtimesheet.cadTempo, intranetdb.tabgrhtimesheet.cadDepto, 
intranetdb.tabgrhtimesheet.cadStatus, intranetdb.tabgrhtimesheet.cadUserR FROM intranetdb.tabgrhtimesheet 
INNER JOIN intranetdb.tabgrhtimesheetatividades ON intranetdb.tabgrhtimesheetatividades.cadID =  
intranetdb.tabgrhtimesheet.cadAtividadeID WHERE intranetdb.tabgrhtimesheet.cadTermino  BETWEEN 
"2022-01-01 00:00:00"  AND now();'''

    cursor.execute(queryValorTimeSheet)

    print(f'Executando Query`s "{relatorio_nome}"...')

        
    print(f'Convertendo arquivo "{relatorio_nome}"...')

    lista = cursor.fetchall()

    for r in range(0, len(lista)):
        if r == "NULL":
                r = (str(''))

    lista = pd.DataFrame(lista, columns=['cadID','cadAtividade', 'cadEmpresa','cadPeso','cadCompetencia',
                                        'cadProjeto','cadInicio','cadTermino','cadTempo','cadDepto',
                                        'cadStatus','cadUserR'])


    try:
        
        lista.to_excel(timeSheetPathXlsx, sheet_name='Intranet-TimeSheet', index=False)

        data_dados = datetime.today()

        if errorMessage: #messagebox.showinfo("Relatório atualizado!", 'O relatório "Intranet-TimeSheet" foi atualizado com sucesso!') 
            print(f"Relatório atualizado!", 'O relatório "{relatorio_nome}" foi atualizado com sucesso!')

        if updateLOG:
            with open(arquivoLOG, "a") as arquivo:
                data_atual = data_dados.strftime("%Y-%m-%d %H:%M")
                arquivo.write(f'---{data_atual}---\nSUCCESS: Relatório "{relatorio_nome}" atualizado com sucesso.\n \n')

        print(f'O relatório "{relatorio_nome}" foi atualizado com sucesso!')

        print(f'Relatório "{relatorio_nome}" salvo em: {timeSheetPathXlsx}')

    except PermissionError or FileNotFoundError or NameError as e:
        
        data_dados = datetime.today()

        if errorMessage: #messagebox.showerror("Erro no programa!", f'O relatório "Intranet-TimeSheet" não foi atualizado! {e}')
            print(f'Erro no programa! O relatório "{relatorio_nome}" não foi atualizado! Verifique se o arquivo está aberto {e}')     

        if updateLOG:
            with open(arquivoLOG, "a") as arquivo:
                data_atual = data_dados.strftime("%Y-%m-%d %H:%M")
                arquivo.write(f'---{data_atual}---\nFAILURE: Relatório "{relatorio_nome}" não foi atualizado.\n Erro {e}\n \n')

    except FileNotFoundError or TypeError or SyntaxError or NameError as e:
    
        data_dados = datetime.today()
        
        if errorMessage: #messagebox.showerror("Erro no programa!", f'Relatório "Intranet-TimeSheet" não foi atualizado.\n Erro {e}\n \n')
            print("Erro no programa!", f'Relatório "{relatorio_nome}" não foi atualizado.\n Erro {e}\n \n')

        if updateLOG:
                with open(arquivoLOG, "a") as arquivo:

                    arquivo.write(f'---{data_atual}---\nFAILURE: Relatório "{relatorio_nome}" não foi atualizado.\n Erro {e}\n \n')

    


#atualizaTributacao()
# atualizarEmpresas()
#atualizarResponsaveis()
#atualizarWorkFlow()
#atualizarDesligamentos()
#atualizarDescarte()
#atualizarMaquinas()
#atualizarServidores()
#atualizarSuporteInfra()
#atualizarObrigacoes()
#atualizarTimeSheet()