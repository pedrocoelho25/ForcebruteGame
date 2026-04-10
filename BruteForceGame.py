import random
import string
import time




def gerar_codigo_secreto(uant_caracteres):
    caracteres = string.ascii_uppercase + string.digits
    
    pool = random.sample(caracteres, uant_caracteres)
    codigo_secreto = "".join(random.sample(pool, uant_caracteres))
    return pool, codigo_secreto


def fase_1():
    pool_caracteres, codigo_secreto = gerar_codigo_secreto(3)

    print(f"\n[INFO] Caracteres identificados na senha:  {'  '.join(pool_caracteres)}")
    print("       Use apenas esses 3 caracteres no seu palpite.")
    print("       Sua missão: descobrir a ordem correta.\n")
    print("-" * 65)
    start_time = time.time()
    tentativas = 0

    while True:
        palpite = input(">> Digite os 3 caracteres na ordem que você acredita: ").strip().upper()
    
        if len(palpite) != 3:
        
            print("   [!] ERRO: O palpite deve ter exatamente 3 caracteres.\n")
            continue
    
    
        if sorted(palpite) != sorted(pool_caracteres):
            print("   [!] ERRO: Use apenas os caracteres informados acima, sem repetir fora do pool.\n")
            continue
    
        tentativas += 1
    
        posicoes_certas = sum(1 for a, b in zip(palpite, codigo_secreto) if a == b)
    
        if posicoes_certas == 3:
            end_time = time.time()                   
            tempo_total = end_time - start_time      
        
            minutos = int(tempo_total // 60)
            segundos = int(tempo_total % 60)
            print("\n" + "="*65)
            print(" ACESSO TOTAL CONCEDIDO! SENHA QUEBRADA COM SUCESSO!")
            print(f"   Senha decifrada: {codigo_secreto}")
            print(f"   Tentativas realizadas: {tentativas}")
            if minutos > 0:
                print(f"   Tempo total: {minutos} minuto(s) e {segundos} segundo(s)")
            else:
                print(f"   Tempo total: {segundos} segundos")
            print("   Excelente trabalho, hacker. O sistema foi comprometido.")
            print("="*65)
            break
        else:
            print(f"   [RESULTADO] → {posicoes_certas} posições corretas.")
            if posicoes_certas == 2:
                print("   Quase lá! Só falta ajustar uma posição.")
        
            print(f"   Tentativa #{tentativas} | Continue o ataque...\n")

def fase_2():
    pool_caracteres, codigo_secreto = gerar_codigo_secreto(4)

    print(f"\n[INFO] Caracteres identificados na senha:  {'  '.join(pool_caracteres)}")
    print("       Use apenas esses 4 caracteres no seu palpite.")
    print("       Sua missão: descobrir a ordem correta.\n")
    print("-" * 65)
    start_time = time.time()
    tentativas = 0

    while True:
        palpite = input(">> Digite os 4 caracteres na ordem que você acredita: ").strip().upper()
    
        if len(palpite) != 4:
        
            print("   [!] ERRO: O palpite deve ter exatamente 4 caracteres.\n")
            continue
    
    
        if sorted(palpite) != sorted(pool_caracteres):
            print("   [!] ERRO: Use apenas os caracteres informados acima, sem repetir fora do pool.\n")
            continue
    
        tentativas += 1
    
        posicoes_certas = sum(1 for a, b in zip(palpite, codigo_secreto) if a == b)
    
        if posicoes_certas == 4:
            end_time = time.time()                   
            tempo_total = end_time - start_time      
        
            minutos = int(tempo_total // 60)
            segundos = int(tempo_total % 60)
            print("\n" + "="*65)
            print(" ACESSO TOTAL CONCEDIDO! SENHA QUEBRADA COM SUCESSO!")
            print(f"   Senha decifrada: {codigo_secreto}")
            print(f"   Tentativas realizadas: {tentativas}")
            if minutos > 0:
                print(f"   Tempo total: {minutos} minuto(s) e {segundos} segundo(s)")
            else:
                print(f"   Tempo total: {segundos} segundos")
            print("   Excelente trabalho, hacker. O sistema foi comprometido.")
            print("="*65)
            break
        else:
            print(f"   [RESULTADO] → {posicoes_certas} posições corretas.")
            if posicoes_certas == 3:
                print("   Quase lá! Só falta ajustar uma posição.")
            elif posicoes_certas == 2:
                print("   Boa! Metade do caminho.")
            print(f"   Tentativa #{tentativas} | Continue o ataque...\n")
    

opcao = 0

while True:
    print("Nivel 1: (3 caracteres para ordenar)")
    print("Nivel 2: (4 caracteres para ordenar)")
    print("digite 3 para sair ")
    opcao = int(input("ual nivel deseja jogar: "))
    
    if opcao == 1:
        jogar_novamente = "s"
        while(jogar_novamente.lower() == "s"):
            fase_1()
            jogar_novamente= input("deseja jogar novamente?(s/n)")
        
    if(opcao == 2):
        jogar_novamente = "s"
        while(jogar_novamente.lower() == "s"):
            fase_2()
            jogar_novamente= input("deseja jogar novamente?(s/n)")
    if(opcao == 3):
        break

    