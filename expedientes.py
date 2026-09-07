 # Base de dados local temporária (lista de dicionários)
expedientes_db = [
    {
        "id": "1",
        "titulo": "Requerimento de Licença",
        "remetente": "João Silva",
        "estado": "Pendente",
        "destino": "Secretaria",
        "observacao": "Aguardando análise"
    }
]

def criar_expediente(usuario_logado):
    print("\n--- NOVA ENTRADA DE EXPEDIENTE ---")
    titulo = input("Título do Documento: ").strip()
    remetente = input("Remetente / Origem: ").strip()
    
    # Gera um ID automático simples baseado no tamanho da lista
    novo_id = str(len(expedientes_db) + 1)
    
    novo_expediente = {
        "id": novo_id,
        "titulo": titulo,
        "remetente": remetente,
        "estado": "Pendente",
        "destino": "Recepção",
        "observacao": "Expediente registado no sistema."
    }
    
    expedientes_db.append(novo_expediente)
    print(f"\n[+] Expediente #{novo_id} registado com sucesso!")

def listar_expedientes():
    print("\n--- LISTA DE EXPEDIENTES ---")
    if not expedientes_db:
        print("Nenhum expediente encontrado.")
        return
        
    for exp in expedientes_db:
        print(f"ID: {exp.get('id')} | Título: {exp.get('titulo')} | Estado: {exp.get('estado')} | Destino: {exp.get('destino')}")
        print(f"   Remetente: {exp.get('remetente')} | Obs: {exp.get('observacao')}")
        print("-" * 50)

def tramitar_expediente(usuario_logado):
    print("\n--- TRAMITAR EXPEDIENTE ---")
    
    # Solicitação dos dados completos
    id_expediente = input("ID do Expediente: ").strip()
    novo_status = input("Novo Status (ex: Em Análise, Despachado, Arquivado): ").strip()
    destino = input("Departamento / Destino: ").strip()
    observacao = input("Observação / Despacho: ").strip()
    
    encontrado = False
    for expediente in expedientes_db:
        if str(expediente.get("id")) == id_expediente:
            expediente["estado"] = novo_status
            expediente["destino"] = destino
            expediente["observacao"] = observacao
            encontrado = True
            break
            
    if encontrado:
        print("\n[+] Expediente tramitado com sucesso!")
    else:
        print("\n[-] Erro: Expediente não encontrado.")

def despachar_expediente(usuario_logado):
    print("\n--- DESPACHAR EXPEDIENTE (GESTOR/ADMIN) ---")
    id_expediente = input("ID do Expediente a despachar: ").strip()
    parecer = input("Parecer Final / Despacho: ").strip()
    
    encontrado = False
    for expediente in expedientes_db:
        if str(expediente.get("id")) == id_expediente:
            expediente["estado"] = "Despachado"
            expediente["observacao"] = parecer
            encontrado = True
            break
            
    if encontrado:
        print("\n[+] Expediente despachado com sucesso!")
    else:
        print("\n[-] Erro: Expediente não encontrado.")