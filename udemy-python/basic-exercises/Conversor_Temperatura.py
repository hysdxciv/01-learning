#Conversor de Temperatura - Celsius p/ Fahrenheit
#( °C × 9/5) + 32 = °F


print('------ Celsius -> Fahrenheit------\n')

celsius = float(input('Informe a temperatura em °C: '))
fahrenheit = (celsius * (9/5)) + 32
print(f'A temperatura em Fahrenheit é {fahrenheit} °F')


