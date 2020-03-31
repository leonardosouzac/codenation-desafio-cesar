
import hashlib

caracteres = 'abcdefghijklmnopqrstuvwxyz'
encriptar = []
cesar=''
enc_sha1=''

#texto
print("Insira a frase a qual deseja aplicar a Cifra de Cesar:")
texto = input().lower()
texto_list = list(texto)

#chave
print("Insira uma chave menor que 26:")
inp_chave = input()
chave = int(inp_chave)
while chave > 26:
	chave -= 26

#selecionar modo
print("Digite 1 para criptografar e 2 para descriptografar")
modo = input()

#dados de localização
tamanho = len(texto)-1
local = 0


if (modo == "1"):
#início Criptografar
	while (local <= tamanho):
		if texto_list[local] in caracteres:
			modificador = chave
			posicao = caracteres.index(texto_list[local])
			modificador += posicao
			if modificador > 26-1:
				modificador -= 26
			encriptar.append(caracteres[modificador])
		else:
			encriptar.append(texto_list[local])
		local+=1

#início Descriptografar
else:
	while (local <= tamanho):
		if texto_list[local] in caracteres:
			modificador = -chave
			posicao = caracteres.index(texto_list[local])
			modificador += posicao
			if modificador < 0:
				modificador += 26
			encriptar.append(caracteres[modificador])
		else:
			encriptar.append(texto_list[local])
		local+=1

encriptado = ''.join(encriptar)
enc_sha1 = hashlib.sha1(encriptado.encode('utf-8')).hexdigest()
print("\n\nFrase original: " + texto + "\nChave: " + str(chave) + "\nCifra de Cesar: " + encriptado + "\nSHA1: " + enc_sha1)
input()
