from datetime import datetime, timedelta

def obter_tempo_original():
    return float(input("Digite a duração do vídeo em minutos: "))

def obter_velocidade_reproducao():
    return float(input("Digite a velocidade de reprodução: "))

def calcular_tempo_duracao(tempo_original, velocidade_reproducao):
    tempo_total = tempo_original / velocidade_reproducao
    return int(tempo_total), int((tempo_total - int(tempo_total)) * 60)

def calcular_hora_termino(tempo_total):
    return datetime.now() + timedelta(minutes=tempo_total)

def formatar_hora(hora):
    return hora.strftime("%H:%M:%S")

def imprimir_resultados(velocidade_reproducao, tempo_original, tempo_total_minutos, tempo_total_segundos, minutos_ganhos, hora_termino_formatada, termino_semx_formatada):
    print(f"\nSeu vídeo na velocidade: {velocidade_reproducao}X demorará {tempo_total_minutos} minutos e {tempo_total_segundos} segundos.")
    print(f"De: {tempo_original} minutos")
    print(f"Para: {tempo_total_minutos} minutos e {tempo_total_segundos} segundos")
    print(f"Você irá ganhar: {minutos_ganhos} minutos")
    print(f"Você terminará por volta das: {hora_termino_formatada}. Sem {velocidade_reproducao}X, você terminaria às {termino_semx_formatada}.")

def main():
    tempo_original = obter_tempo_original()
    velocidade_reproducao = obter_velocidade_reproducao()

    tempo_total_minutos, tempo_total_segundos = calcular_tempo_duracao(tempo_original, velocidade_reproducao)
    hora_termino = calcular_hora_termino(tempo_total_minutos)
    termino_semx = calcular_hora_termino(tempo_original)

    minutos_ganhos = int(tempo_original - tempo_total_minutos)

    hora_termino_formatada = formatar_hora(hora_termino)
    termino_semx_formatada = formatar_hora(termino_semx)

    imprimir_resultados(velocidade_reproducao, tempo_original, tempo_total_minutos, tempo_total_segundos, minutos_ganhos, hora_termino_formatada, termino_semx_formatada)

if __name__ == "__main__":
    main()