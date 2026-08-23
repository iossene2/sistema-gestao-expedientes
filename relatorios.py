# Módulo de Emissão de Relatórios e Estatísticas
# Desenvolvido por: bentozucule

import expedientes

def menu_relatorios():
    print("\n--- RELATÓRIOS E ESTATÍSTICAS DO SISTEMA ---")
    total = len(expedientes.expedientes_db)
    
    if total == 0:
        print("Não há dados suficientes para gerar relatórios.")
        return

    pendentes = sum(1 for e in expedientes.expedientes_db if e["estado"] == "Pendente")
    em_analise = sum(1 for e in expedientes.expedientes_db if e["estado"] == "Em Análise")
    despachados = sum(1 for e in expedientes.expedientes_db if e["estado"] == "Despachado")
    arquivados = sum(1 for e in expedientes.expedientes_db if e["estado"] == "Arquivado")

    print(f"Total de Expedientes Registados: {total}")
    print(f" - Pendentes  : {pendentes}")
    print(f" - Em Análise : {em_analise}")
    print(f" - Despachados: {despachados}")
    print(f" - Arquivados : {arquivados}")
    print("=" * 40)
    