import logging
import sys

nivel_log = logging.ERROR
#nivel_log = logging.DEBUG
logger_cagada = None

def kakatsuki_bitch_test(maskara, posicion):
    return maskara & (1 << posicion)

def kakatsuki_bitch_anadido(maskara, posicion):
    return maskara | (1 << posicion)

def kakatsuki_bitch_count(maskara):
    cagada = 0
    mamada = maskara
    while mamada:
        mamada &= ~(mamada & (-mamada))
        cagada += 1
    return cagada

def kakatsuki_obten_distancia(puto1, puto2):
    return abs(puto2[0] - puto1[0]) + abs(puto2[1] - puto1[1])

def kakatsuki_obten_distancia_idx(matrix_chostos, akatsuki, konoha, idx1, idx2):
    logger_cagada.debug("idx1 {} idx2 {}".format(idx1, idx2))
    if(matrix_chostos[idx1][idx2] == -1):
        matrix_chostos[idx1][idx2] = kakatsuki_obten_distancia(akatsuki[idx1], konoha[idx2])
    return matrix_chostos[idx1][idx2]

def kakatsuki_core(num_pendejos, matrix_chostos, akatsuki, konoha):
    mierdas = [sys.maxsize] * (1 << num_pendejos)
    mierdas[0] = 0
    for mascara in range(1 << num_pendejos):
        logger_cagada.debug("everubodu stand up {}".format(mascara))
        num_bitchs = kakatsuki_bitch_count(mascara)
        logger_cagada.debug("num bitchs {}".format(num_bitchs))
        for pos_bitch in range(num_pendejos):
            logger_cagada.debug("en pos bitch {}".format(pos_bitch))
            if(not kakatsuki_bitch_test(mascara, pos_bitch)):
                mamadascara = kakatsuki_bitch_anadido(mascara, pos_bitch)
                mierdas[mamadascara] = min(mierdas[mamadascara], mierdas[mascara] + kakatsuki_obten_distancia_idx(matrix_chostos, akatsuki, konoha, num_bitchs, pos_bitch))
    caca = mierdas[(1 << num_pendejos) - 1]
    return caca

def kakatsuki_main():
    lineas = list(sys.stdin)
    
    num_pendejos = int(lineas[0])
    akatsuki = []
    konoha = []
    matrix_chostos = [[-1] * num_pendejos]
    
    for _ in range(1, num_pendejos):
        matrix_chostos.append([-1] * num_pendejos)
    
    logger_cagada.debug("la matrix de chostos {}".format(matrix_chostos))
    
    for linea in lineas[1:num_pendejos + 1]:
        caca_x, caca_y = [int(x) for x in linea.strip().split(" ")]
        akatsuki.append((caca_x, caca_y))
    for linea in lineas[num_pendejos + 1:num_pendejos + 1 + num_pendejos ]:
        caca_x, caca_y = [int(x) for x in linea.strip().split(" ")]
        konoha.append((caca_x, caca_y))
    
    logger_cagada.debug("akatsuki {} konoha {}".format(akatsuki, konoha))
    cagada = kakatsuki_core(num_pendejos, matrix_chostos, akatsuki, konoha)
    
    print(cagada)


if __name__ == '__main__':
        FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
        logging.basicConfig(level=nivel_log, format=FORMAT)
        logger_cagada = logging.getLogger("asa")
        logger_cagada.setLevel(nivel_log)
        kakatsuki_main()
