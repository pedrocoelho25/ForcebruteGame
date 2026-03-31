import random
import string
import time



def gerar_codigo_secreto():

   
    caracteres = string.ascii_uppercase + string.digits
    
    pool = random.sample(caracteres, 4)
    codigo_secreto = "".join(random.sample(pool, 4))
    return pool, codigo_secreto



pool_caracteres, codigo_secreto = gerar_codigo_secreto()

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