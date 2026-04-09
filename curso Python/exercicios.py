# exe 106
def sis(hlp):
    cab = f"Acessando o manual do comando {hlp}"
    print(
        f"""\033[1;37;44m
  {'~'*(len(cab)+2)}  
  {cab.center((len(cab))+2)}  
  {'~'*(len(cab)+2)}  \033[m"""
    )
    return help(hlp)


cab = "SISTEMA DE AJUDA PyHELP"
tam = len(cab)
print(
    f"""\033[1;37;42m
 {'~'*(len(cab)+2)}  
 {cab.center((len(cab))+2)}  
 {'~'*(len(cab)+2)}  \033[m"""
)
resp = sis(str(input("Função ou biblioteca > ")))
# print(resp)
