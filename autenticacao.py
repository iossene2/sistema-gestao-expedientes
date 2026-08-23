 # Módulo de Autenticação e Gestão de Utilizadores (RBAC)
# Desenvolvido por: iossene2 e bentozucule

# Base de dados de utilizadores do grupo
utilizadores_db = {
    "iossene2": {"senha": "123", "perfil": "Administrador"},
    "bentozucule": {"senha": "123", "perfil": "Gestor"}
}

def efetuar_login():
    print("\n" + "="*40)
    print("        LOGIN DO SISTEMA        ")
    print("="*40)
    usuario = input("Nome de Utilizador: ").strip()
    senha = input("Palavra-passe: ").strip()

    if usuario in utilizadores_db and utilizadores_db[usuario]["senha"] == senha:
        perfil = utilizadores_db[usuario]["perfil"]
        print(f"\n[+] Bem-vindo, {usuario}! (Perfil: {perfil})")
        return {"usuario": usuario, "perfil": perfil}
    else:
        print("\n[-] Erro: Utilizador ou palavra-passe incorretos!")
        return None

def cadastrar_utilizador():
    print("\n--- CADASTRO DE NOVO UTILIZADOR ---")
    novo_user = input("Nome do novo utilizador: ").strip()

    if novo_user in utilizadores_db:
        print("[-] Erro: Este utilizador já existe!")
        return

    nova_senha = input("Palavra-passe: ").strip()
    print("\nSelecione o Perfil:")
    print("1. Administrador")
    print("2. Gestor")
    print("3. Técnico")
    opcao = input("Opção: ").strip()

    perfis = {"1": "Administrador", "2": "Gestor", "3": "Técnico"}
    perfil = perfis.get(opcao, "Técnico")

    utilizadores_db[novo_user] = {"senha": nova_senha, "perfil": perfil}
    print(f"\n[+] Utilizador '{novo_user}' cadastrado com sucesso como {perfil}!")