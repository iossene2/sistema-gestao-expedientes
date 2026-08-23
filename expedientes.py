# Módulo de Registo e Gestão de Expedientes
# Desenvolvido por: bentozucule

# Estrutura em memória para armazenar expedientes
expedientes_db = []
contador_id = 1001

def cadastrar_expediente():
    global contador_id
    print("\n--- REGISTO DE NOVO EXPEDIENTE ---")
    remetente = input("Remetente (Entidade/Pessoa): ").strip()
    assunto = input("Assunto do Expediente: ").strip()
    tipo = input("Tipo (Carta, Ofício, Requerimento, Memorando): ").strip()
    
    expediente = {
        "id": contador_id,
        "remetente": remetente,
        "assunto": assunto,
        "tipo": tipo,
        "estado": "Pendente",
        "localizacao": "Secretaria Geral"
    }
    
    expedientes_db.append(expediente)
    print(f"\n[+] Expediente Nº {contador_id} registado com sucesso!")
    contador_id += 1

def listar_expedientes():
    print("\n--- LISTA DE EXPEDIENTES ---")
    if not expedientes_db:
        print("Nenhum expediente registado no sistema.")
        return
        
    for exp in expedientes_db:
        print(f"ID: {exp['id']} | Tipo: {exp['tipo']} | Remetente: {exp['remetente']}")
        print(f"   Assunto: {exp['assunto']}")
        print(f"   Estado: [{exp['estado']}] | Localização Atual: {exp['localizacao']}")
        print("-" * 50)

def atualizar_estado_expediente():
    print("\n--- ATUALIZAR TRAMITAÇÃO DE EXPEDIENTE ---")
    try:
        exp_id = int(input("Digite o ID do Expediente: "))
    except ValueError:
        print("[-] ID inválido!")
        return

    for exp in expedientes_db:
        if exp["id"] == exp_id:
            print(f"Expediente encontrado: {exp['assunto']} (Estado atual: {exp['estado']})")
            print("1. Marcar como Em Análise")
            print("2. Marcar como Despachado")
            print("3. Marcar como Arquivado")
            op = input("Opção: ").strip()
            
            if op == "1":
                exp["estado"] = "Em Análise"
            elif op == "2":
                exp["estado"] = "Despachado"
            elif op == "3":
                exp["estado"] = "Arquivado"
                
            nova_loc = input("Nova Localização/Departamento: ").strip()
            if nova_loc:
                exp["localizacao"] = nova_loc
                
            print(f"[+] Expediente Nº {exp_id} atualizado com sucesso!")
            return
            
    print("[-] Expediente não encontrado!")