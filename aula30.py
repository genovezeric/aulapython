"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)

    <- Contagem de complexidade (ruim)
"""

velocidade = 70 # velocidade atual do carro
local_carro = 101 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está 
RADAR_RANGE = 1 # a distancia onde o radar pega

velocidade_passou = velocidade > RADAR_1
carro_passou_radar1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar1 = carro_passou_radar1 and velocidade_passou

if velocidade_passou:
    print('Velocidade do carro foi maior que o radar 1')
if carro_passou_radar1:
    print('Carro passou no radar 1')
if carro_multado_radar1:
    print('Carro multado no radar 1')
