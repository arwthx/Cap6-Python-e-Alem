import json
import os
import datetime

ARQUIVO_JSON = "colheitas.json"


def exibir_cabecalho():
    print("=" * 60)
    print(" sugarcane ".upper().center(60, "-"))
    print(" Sistema de Monitoramento de Perdas na Colheita ".center(60))
    print("=" * 60)


def menu_principal():
    print("\nMENU PRINCIPAL:")
    print("1. Registrar nova Colheita")
    print("2. Listar todas as Colheitas")
    print("3. Gerar Relatório Analítico de Perdas")
    print("4. Sair")
    return input("Escolha uma opção: ")


def carregar_dados_json():
    if os.path.exists(ARQUIVO_JSON):
        try:
            with open(ARQUIVO_JSON, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []


def salvar_dados_json(registros):
    with open(ARQUIVO_JSON, 'w', encoding='utf-8') as f:
        json.dump(registros, f, indent=4, ensure_ascii=False)
    print("\n[INFO] Dados salvos com sucesso em '{}'.".format(ARQUIVO_JSON))


def validar_float(prompt):
    while True:
        try:
            valor = float(input(prompt).replace(',', '.'))
            if valor >= 0:
                return valor
            else:
                print("[ERRO] O valor não pode ser negativo. Tente novamente.")
        except ValueError:
            print("[ERRO] Entrada inválida. Por favor, digite um número.")


def salvar_simulado_oracle(registro):
    print("\n--- SIMULAÇÃO DE CONEXÃO ORACLE ---")
    print("Conectando ao banco de dados Oracle...")
    sql_command = f"INSERT INTO COLHEITAS (ID, DATA, TALHAO, MAQUINA, OPERADOR, TONELADAS, PERDA_PERC) VALUES ({registro['id']}, '{registro['data']}', '{registro['talhao']}', '{registro['maquina']}', '{registro['operador']}', {registro['toneladas_colhidas']}, {registro['perda_perc']});"
    print(f"Executando comando: {sql_command}")
    print("Registro salvo no banco de dados Oracle com sucesso!")
    print("------------------------------------")


def registrar_colheita(registros):
    print("\n--- REGISTRO DE NOVA COLHEITA ---")

    novo_id = len(registros) + 1
    data_registro = datetime.date.today().strftime("%Y-%m-%d")
    talhao = input("Digite a identificação do Talhão/Área: ")
    maquina = input("Digite o código da colhedora (ex: JD-01, CASE-02): ").upper()
    operador = input("Digite o nome do operador: ")

    toneladas_colhidas = validar_float("Digite as toneladas colhidas: ")
    perda_perc = validar_float("Digite a perda estimada em porcentagem (%): ")

    novo_registro = {
        "id": novo_id,
        "data": data_registro,
        "talhao": talhao,
        "maquina": maquina,
        "operador": operador,
        "toneladas_colhidas": toneladas_colhidas,
        "perda_perc": perda_perc
    }

    registros.append(novo_registro)

    salvar_dados_json(registros)
    salvar_simulado_oracle(novo_registro)


def listar_colheitas(registros):
    print("\n--- LISTA DE COLHEITAS REGISTRADAS ---")
    if not registros:
        print("Nenhum registro encontrado.")
        return

    cabecalho = ("ID", "Data", "Talhão", "Máquina", "Operador", "Toneladas", "Perda (%)")

    print(
        f"{cabecalho[0]:<4} | {cabecalho[1]:<12} | {cabecalho[2]:<15} | {cabecalho[3]:<10} | {cabecalho[4]:<15} | {cabecalho[5]:>10} | {cabecalho[6]:>10}")
    print("-" * 95)

    for reg in registros:
        print(
            f"{reg['id']:<4} | {reg['data']:<12} | {reg['talhao']:<15} | {reg['maquina']:<10} | {reg['operador']:<15} | {reg['toneladas_colhidas']:>10.2f} | {reg['perda_perc']:>10.2f}%")


def gerar_relatorio_analitico(registros):
    print("\n--- GERANDO RELATÓRIO ANALÍTICO DE PERDAS ---")
    if not registros:
        print("Nenhum registro para analisar.")
        return

    total_perda_perc = sum(r['perda_perc'] for r in registros)
    perda_media_geral = total_perda_perc / len(registros)

    pior_registro = max(registros, key=lambda r: r['perda_perc'])

    perdas_por_maquina = {}
    for r in registros:
        maquina = r['maquina']
        if maquina not in perdas_por_maquina:
            perdas_por_maquina[maquina] = []
        perdas_por_maquina[maquina].append(r['perda_perc'])

    media_por_maquina = {m: sum(p) / len(p) for m, p in perdas_por_maquina.items()}
    maquina_maior_perda = max(media_por_maquina, key=media_por_maquina.get)

    conteudo_relatorio = f"""
=================================================
       RELATÓRIO ANALÍTICO - CANA-EFICIENTE
=================================================
Data de Emissão: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

RESUMO GERAL:
- Total de Colheitas Registradas: {len(registros)}
- Perda Média Geral: {perda_media_geral:.2f}%

PONTOS DE ATENÇÃO:
- Maior Perda Registrada: {pior_registro['perda_perc']:.2f}%
  - Talhão: {pior_registro['talhao']}
  - Máquina: {pior_registro['maquina']}
  - Operador: {pior_registro['operador']}

ANÁLISE POR EQUIPAMENTO:
- A máquina com a maior média de perdas é a '{maquina_maior_perda}' com {media_por_maquina[maquina_maior_perda]:.2f}%.
  - Ações sugeridas: Verificar manutenção, calibragem ou treinamento do operador para este equipamento.

=================================================
"""
    nome_arquivo_relatorio = "relatorio_analitico.txt"
    with open(nome_arquivo_relatorio, 'w', encoding='utf-8') as f:
        f.write(conteudo_relatorio)

    print(conteudo_relatorio)
    print(f"\n[INFO] Relatório salvo com sucesso em '{nome_arquivo_relatorio}'.")


def main():
    registros_colheita = carregar_dados_json()
    exibir_cabecalho()

    while True:
        escolha = menu_principal()

        if escolha == '1':
            registrar_colheita(registros_colheita)
        elif escolha == '2':
            listar_colheitas(registros_colheita)
        elif escolha == '3':
            gerar_relatorio_analitico(registros_colheita)
        elif escolha == '4':
            print("\nSaindo do sistema. Até logo!")
            break
        else:
            print("\n[ERRO] Opção inválida. Por favor, tente novamente.")


if __name__ == "__main__":
    main()