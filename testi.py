# Esimerkkejä muuttujista

etunimi = 'Mika' # Merkkijono (string)
sukunimi = "Hakala" # Toinen tapa tehdä merkkijono
kengan_koko = 45 # kaksiosainen nimi: snake case suositeltu tapa
kenganKoko = 44.5 # kaksiosainen nimi: dromedare case, ei suositella
KenganKoko = 47 # kaksiosainen nimi: camel case, ei suositella
opettaja = True

# Esimerkkejä rakenteista ja komennoista

# Ruudulle tulostaminen
print('Opettajana on tänään', etunimi, sukunimi)

print('Mikan kengän koko on', kengan_koko)

print(opettaja)

print(sukunimi)

print(sukunimi, 'kengän koko on', kengan_koko, '\n')

# Kysytään käyttäjältä tietoja (koko nimi)
koko_nimi = input('Kirjoita nimesi ')

# Tekstien yhdistäminen (katenointi, concatenation)
tervehdys = 'Morjensta ' + koko_nimi + ', tervetuloa Tampereelle'

print(tervehdys, '\n')

print('Morjensta', koko_nimi + ',', 'tervetuloa Tampereelle')

# Luetaan numeerista tietoa näppäimistöstä
markat = input('Kuinka monta markkaa sait kakarana viikkorahaa? ')
eurot = float(markat) / 6
print('Se olisi nykyään', eurot, 'euroa')

# Funktiot pythonissa, esim funktio, joka muuttaa markat euroiksi
def euroa(markkaa)

    """Funktio palauttaaa markkoina annetun arvon europina

    Args:
        markkaa (float): rahamäärä markkoina

    Returns:
        float: rahan määrä euroina
    """

    return markkaa / 6

viikkoraha = euroa(100)

print('Se on nykyisin euroina', viikkoraha )
