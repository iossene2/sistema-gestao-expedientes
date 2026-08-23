 # Módulo de Gestão de Expedientes
# Desenvolvido por: iossene2 e bentozucule

expedientes_db = []
contador_id = 1

def criar_expediente(usuario_logado):
    global contador_id
    print("\n--- NOVA ENTRADA DE EXPEDIENTE ---")
    titulo = input("Título do Documento: ").strip()
    remetente = input("Remetente/Origem: ").strip()
    
    expediente = {
        "id": contador_id,
        "titulo": titulo,
        "remetente": remetente,
        "estado": "Entrada",
        "criado_por": usuario_logado["usuario"]
    }
    expedientes_db.append(expediente)
    print(f"\n[+] Expediente #{contador_id} registado com sucesso por {usuario_logado['usuario']}!")
    contador_id += 1

def listar_expedientes():
    print("\n--- LISTA DE EXPEDIENTES ---")
    if not expedientes_db:
        print("Nenhum expediente registado.")
        return

    for exp in expedientes_db:
        print(f"ID: {exp['id']} | Título: {exp['titulo']} | Estado: {exp['estado']} | Criador: {exp['criado_por']}")

def tramitar_expediente(usuario_logado):
    print("\n--- TRAMITAÇÃO DE EXPEDIENTE ---")
    listar_expedientes()
    if not expedientes_db:
        return
        
    try:
        exp_id = int(input("\nDigite o ID do expediente a tramitar: "))
        for exp in expedientes_db:
            if exp["id"] == exp_id:
                exp["estado"] = "Em Tramitação"
                print(f"[+] Expediente #{exp_id} alterado para 'Em Tramitação' por {usuario_logado['usuario']}.")
                return
        print("[-] ID não encontrado.")
    except ValueError:
        print("[-] Entrada inválida.")

def despachar_expediente(usuario_logado):
    # Restrição RBAC: Apenas Gestor ou Administrador podem despachar
    if usuario_logado["perfil"] not in ["Administrador", "Gestor"]:
        print("\n[-] Acesso Negado: O seu perfil não tem permissão para despachar expedientes!")
        return

    print("\n--- DESPACHO DE EXPEDIENTE ---")
    listar_expedientes()
    if not expedientes_db:
        return

    try:
        exp_id = int(input("\nDigite o ID do expediente a despachar: "))
        for exp in expedientes_db:
            if exp["id"] == exp_id:
                exp["estado"] = "Despachado / Arquivado"
                print(f"[+] Expediente #{exp_id} foi despachado e arquivado por {usuario_logado['usuario']}!")
                return
        print("[-] ID não encontrado.")
    except ValueError:
        print("[-] Entrada inválida.")