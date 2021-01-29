# Toistorakenteet
# FOR-silmukka
lista = ['Mika', 'Mikko', 'Markku', 'Harttu']
for opettaja in lista:
    print ('Hyvää huomenta', opettaja, '\n')
    if opettaja == 'Markku':
        break
print('Tervetuloa töihin')

# Kertoma
kertoma = 1
for luku in range(1, 5):
    kertoma = kertoma * luku
    print('kertoma on', kertoma)
print('kertoma on', kertoma)

# While-silmukka
kierroslaskuri = 0
while kierroslaskuri < 5:
    print('Tänään kaikki menee pieleen!')
    kierroslaskuri = kierroslaskuri + 1
print('Silmukka on päättynyt')