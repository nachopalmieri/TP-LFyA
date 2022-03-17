import re
def add_sub (exp): #Calcular suma y resta
    ret = re.findall('([-+]?\d+)([-+])(\d+)', exp)  
         # Usar expresiones regulares para hacer coincidir cada número con signo en la fórmula y devolver una lista
    exp_sum = 0
         # Completa la suma o resta en este ciclo
    for i in ret:
        exp_sum += float (i) #Suma cada elemento de la lista
    return exp_sum

def atom_cal(exp):
    if '*' in exp: #Calcular una sola multiplicación
        a, b = exp.split ('*') #split () se usa para dividir caracteres;
        return str(float(a) * float(b))
    elif '**' or '* *' in exp:
        a,b = exp.split('**') or exp.split('* *')
        return str(float(a))**float(b)
    elif '/' in exp: #Calcular una sola división
        a, b = exp.split('/')
        return str(float(a) / float(b))


def mul_div (exp): #Calcular multiplicación y división
    while True:
        ret = re.search ('([-+]?\d+)([/*%])([-+]?\d+)', exp) #Utilice expresiones regulares para hacer coincidir multiplicaciones o divisiones
        if ret: #Si coincide
            atom_exp = ret.group () # Saque este valor, group () se usa para obtener una o más cadenas coincidentes agrupadas
            res = atom_cal (atom_exp) # llame al cálculo atom_cal anterior
            exp = exp.replace (atom_exp, res) # El resultado calculado se reemplaza por el original
        else: 
            return exp # Si no coincide, significa que el cálculo de multiplicación y división se completó y se devuelve el resultado del cálculo

def cal (exp): # Calcula la operación mixta de suma, resta, multiplicación y división
    exp = mul_div (exp) # Llame a la función mul_div para calcular la multiplicación y la división primero, y ejecute el siguiente método si no hay coincidencia
    exp_sum = add_sub (exp) # llame a add_sub para calcular la suma y la resta
    return exp_sum # float #Return resultado del cálculo

a = input ("Por favor ingrese:")
b = cal(a)
print(b)

# otra alternativa: https://saintuszephir.com/programacion/python/calculadora-en-python-usando-expresiones-regulares-desde-cero/

