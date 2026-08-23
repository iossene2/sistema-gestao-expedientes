# Ficheiro Principal do Sistema
# Desenvolvido por: iossene2 e bentozucule

import autenticacao
import expedientes
import relatorios

def menu_principal():
    usuario_logado = None
    
    while True:
        if not usuario_logado:
            usuario_logado = autenticacao.efetuar_login()
            if not usuario_logado:
                continuar = input("\nDeseja tentar novamente? (s/n): ").lower()
                if continuar != 's':
                    print("\nEncerrando o sistema...")
                    break
                continue

        print("\n" + "="*40)
        print(f" MENU PRINCIPAL | Utilizador: {usuario_logado['usuario']}")
        print("="*40)
        print("1. Cadastrar Novo Expediente")
        print("2. Listar / Pesquisar Expedientes")
        print("3. Atualizar Estado / Tramitação")
        print("4. Gerar Relatórios do Sistema")
        
        if usuario_logado["perfil"] == "Administrador":
            print("5. Cadastrar Novo Utilizador (Admin)")
            
        print("0. Sair / Terminar Sessão")
        print("="*40)
        
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            expedientes.cadastrar_expediente()
        elif opcao == "2":
            expedientes.listar_expedientes()
        elif opcao == "3":
            expedientes.atualizar_estado_expediente()
        elif opcao == "4":
            relatorios.menu_relatorios()
        elif opcao == "5" and usuario_logado["perfil"] == "Administrador":
            autenticacao.cadastrar_utilizador()
        elif opcao == "0":
            print(f"\n[+] Sessão terminada para {usuario_logado['usuario']}.")
            usuario_logado = None
            break
        else:
            print("[-] Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu_principal()