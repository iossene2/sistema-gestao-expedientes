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

        print(f"\n==========================================")
        print(f" PAINEL PRINCIPAL ({usuario_logado['usuario']} - {usuario_logado['perfil']})")
        print(f"==========================================")
        print("1. Criar Expediente")
        print("2. Listar Expedientes")
        print("3. Tramitar Expediente")
        print("4. Despachar Expediente (Gestor/Admin)")
        print("5. Gerar Relatório / Auditoria")
        print("6. Cadastrar Novo Utilizador")
        print("7. Terminar Sessão (Logout)")
        print("0. Sair")
        
        opcao = input("Opção: ").strip()

        if opcao == "1":
            expedientes.criar_expediente(usuario_logado)
        elif opcao == "2":
            expedientes.listar_expedientes()
        elif opcao == "3":
            expedientes.tramitar_expediente(usuario_logado)
        elif opcao == "4":
            expedientes.despachar_expediente(usuario_logado)
        elif opcao == "5":
            relatorios.menu_relatorios()
        elif opcao == "6":
            autenticacao.cadastrar_utilizador()
        elif opcao == "7":
            usuario_logado = None
            print("\n[+] Sessão terminada com sucesso.")
        elif opcao == "0":
            print("\nEncerrando o sistema...")
            break
        else:
            print("\n[-] Opção inválida!")

if __name__ == "__main__":
    menu_principal()