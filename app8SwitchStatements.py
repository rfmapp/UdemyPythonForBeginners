__author__ = 'rafael'

# Estruturas de controle com Switch.
# Variáveis para os exemplos.
dia_semana = "sab";
# Pythpn não possui o controle switch como as outras linguagens. Para usa-lo, precisamos da ajuda de um array.
switch = dict(
    dom = 'Domingo',
    seg = 'Segunda',
    ter = 'Terça',
    qua = 'Quarta',
    qui = 'Quinta',
    sex = 'Sexta',
    sab = 'Sábado'
);

# Aqui usamos uma função para garantir que se a opção escolhida não estiver dentro do array, um valor padrão será utilizado.
print(switch.get(dia_semana, "Não temos esse dia em nossa base de dados!"));
