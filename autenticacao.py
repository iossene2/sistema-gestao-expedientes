# Módulo de Autenticação e Gestão de Utilizadores
# Desenvolvido por: iossene2

utilizadores_db = {
    "admin": {"senha": "123", "perfil": "Administrador"},
    "funcionario": {"senha": "123", "perfil": "Funcionario"}
}

def efetuar_login():
    print("\n" + "="*40)
    print("      SISTEMA DE GESTÃO DE EXPEDIENTES")
    print("="*40)
    print("--- LOGIN DO SISTEMA ---")
    
    usuario = input("Nome de Utilizador: ").strip()
    senha = input("Palavra-passe: ").strip()
    
    if usuario in utilizadores_db and utilizadores_db[usuario]["senha"] == senha:
        print(f"\n[+] Login bem-sucedido! Bem-vindo(a), {usuario} ({utilizadores_db[usuario]['perfil']}).")
        return {"usuario": usuario, "perfil": utilizadores_db[usuario]["perfil"]}
    else:
        print("\n[-] Erro: Utilizador ou palavra-passe incorretos!")
        return None

def cadastrar_utilizador():
    print("\n--- CADASTRO DE NOVO UTILIZADOR ---")
    novo_user = input("Novo nome de utilizador: ").strip()
    if novo_user in utilizadores_db:
        print("[-] Erro: Este utilizador já existe!")
        return
        
    nova_senha = input("Palavra-passe: ").strip()
    print("Selecione o Perfil:")
    print("1. Administrador")
    print("2. Funcionário")
    opcao = input("Opção: ").strip()
    
    perfil = "Administrador" if opcao == "1" else "Funcionario"
    utilizadores_db[novo_user] = {"senha": nova_senha, "perfil": perfil}
    print(f"[+] Utilizador '{novo_user}' cadastrado com sucesso como {perfil}!")