import unicodedata


def separar_palavras(linha):
    """Troca a pontuação por espaços e separa as palavras."""
    linha = unicodedata.normalize("NFC", linha.lower())
    caracteres = []
    for caractere in linha:
        if caractere.isalnum():
            caracteres.append(caractere)
        else:
            caracteres.append(" ")
    return "".join(caracteres).split()


def construir_indice(texto):
    indice = {}

    for numero, linha in enumerate(texto.splitlines(), start=1):
        for palavra in separar_palavras(linha):
            if palavra not in indice:
                indice[palavra] = set()
            indice[palavra].add(numero)

    return indice


def _linhas_da_palavra(indice, palavra):
    termos = separar_palavras(palavra)
    if len(termos) != 1:
        return set()
    return indice.get(termos[0], set())


def buscar(indice, palavra):
    return sorted(_linhas_da_palavra(indice, palavra))


def buscar_e(indice, palavras):
    resultado = None

    for palavra in palavras:
        linhas = _linhas_da_palavra(indice, palavra)
        if resultado is None:
            resultado = linhas
        else:
            resultado = resultado & linhas

        if not resultado:
            return []

    return sorted(resultado) if resultado is not None else []


def buscar_ou(indice, palavras):
    resultado = set()
    for palavra in palavras:
        resultado.update(_linhas_da_palavra(indice, palavra))
    return sorted(resultado)
