# Luodaan painoindeksin laskentafunktio
def painoindeksi(pituus, paino):
    """Painoindeksi lasketqaan jakamalla paino pituuden neliöllä

    Args:
        pituus (float): henkilön pituus metreinä
        paino (float): henkilön paino kilogrammoina
    """
    bmi = paino / (pituus**2)
    return bmi


mikan_painoindeksi_tanaan = painoindeksi(1.7, 73)
print('Mikan painoideksi on', mikan_painoindeksi_tanaan)
