# dicionarios.py
intensificadores = {
    "muito", "super", "extremamente", "demais", "totalmente", "completamente", "incrivelmente", 
    "absolutamente", "enormemente", "intensamente", "realmente", "impressionantemente", 
    "incontáveis", "surpreendentemente", "radicalmente", "incessantemente", "avassaladoramente", 
    "exageradamente", "excepcionalmente", "fortemente", "incansavelmente", "profundamente", 
    "sustancialmente", "intensivo", "delirantemente", "perfeitamente", "violentamente", 
    "exaltadamente", "inquestionavelmente", "incontestavelmente", "infinitamente", "maravilhosamente",
    "incomensuravelmente", "absolutamente", "infelizmente", "espetacularmente", "absurdamente"
}

palavras_positivas = {
    "bom": 3.5, "ótimo": 4.4, "excelente": 7.1, "maravilhoso": 3.7, "feliz": 2.4, "bem": 3.9,
    "gostei": 2.8, "legal": 1.5, "incrível": 3.1, "positivo": 2.6, "espetacular": 4.3,
    "adoro": 3.5, "encantado": 3.2, "animado": 2.3, "satisfeito": 2.1, "favorável": 1.9,
    "surpreendente": 3.4, "maravilhosa": 4.6, "extraordinário": 4.5, "fantástico": 4.0,
    "adorável": 3.2, "brilhante": 3.03, "vibrante": 2.2, "eficaz": 2.8, "grande": 1.1,
    "formidável": 4.7, "reluzente": 5.6, "agradável": 3.8, "belo": 2.5, "inteligente": 3.1,
    "delicioso": 3.6, "perfeito": 4.9, "deslumbrante": 4.2, "cativante": 3.3, "forte": 2.7,
    "valioso": 3.9, "notável": 3.6, "prodigioso": 4.8, "excepcional": 4.1, "impressionante": 3.2,
    "único": 3.7, "bravo": 3.4, "eficiente": 3.9, "amável": 2.6, "profundo": 3.8, "inesquecível": 4.4,
    "contente": 2.7, "acertado": 3.5, "luminosa": 2.8, "caloroso": 2.3, "fofo": 2.1, "próspero": 3.7,
    "esperançoso": 3.1, "resplandecente": 4.9, "saudável": 2.4, "fabuloso": 3.6,
    "gratificante": 3.1, "acima da média": 3.3, "vencedor": 2.9, "positiva": 2.5,
    "top": 5.1, "massa": 4.2, "da hora": 4.5, "show": 5.6, "maneiro": 4.3, "fera": 5.9, "irado": 5.2,
    "brabo": 5.3, "bombando": 4.7, "pica": 6.1, "bafônico": 6.9, "arrasando": 5.7, "sussa": 2.3,
    "chave": 4.6, "topzera": 6.8, "zica": 5.4, "de boa": 2.8, "poderoso": 5.1,
    "estrela": 5.5, "show de bola": 5.8, "quebrado": 4.9, "fenômeno": 6.7, "divonico": 5.2
}

palavras_negativas = {
    "ruim": -7, "péssimo": -8, "horrível": -9, "triste": -7, "mal": -6, "desagradável": -6, 
    "terrível": -8, "horrendo": -9, "decepcionante": -7, "chato": -5, "frustrante": -6, 
    "horrível": -8, "insuportável": -9, "negativo": -6, "desastroso": -8, "miserável": -9, 
    "desgostoso": -7, "repulsivo": -8, "horripilante": -9, "fúnebre": -7, "deprimente": -8, 
    "desolador": -8, "desolado": -7, "infeliz": -7, "angustiante": -8, "patético": -7, 
    "irritante": -6, "insustentável": -8, "preocupante": -7, "chato": -6, "nocivo": -7, 
    "lamentável": -8, "abominável": -9, "dificuldade": -6, "desagradável": -7,"mau":-6,
    "mermão": -6, "lixado": -7, "decepcionado": -7, "se fudeu": -8, "deu ruim": -7,
    "quebrado": -6, "travado": -5, "sujeira": -8, "vazio": -6, "ferrado": -8, "merda": -9, 
    "bomba": -7, "fudido": -9, "fora": -6, "falido": -7, "acabou": -6, "desapontado": -7, 
    "sem graça": -6, "sinistro": -7, "chato": -5, "sacanagem": -8,  "ralado": -6
}


palavras_neutras = {
    "normal", "tranquilo", "ok", "certo", "de boa", "tá bom", 
    "mais ou menos", "então", "está tudo certo", "não faz diferença", 
    "não importa", "sem problema", "sem estresse", "como preferir", "okey", "sem pressa", 
    "não sei", "não tenho certeza", "não tem importância", "pode ser", "meio a meio", 
    "sem opinião formada", "está tranquilo", "entendi", "isso é ok", "só isso", 
    "fica tranquilo", "nada demais", "decentemente", "por enquanto", 
    "vou ver depois", "não é urgente",
}


palavras_negacao = {
    "não", "nunca", "jamais", "nenhum", "ninguém", "sem", "ausência", "nada", "nenhuma",
    "nunca mais", "sem querer", "não posso", "não mais", "não tem", "não gosto", "não sei",
    "não quero", "nem", "negar", "proibido", "abstinência", "não sou", "não aceito",
    "não espero", "não tenho", "não existe", "não possuo", "não gosto", "não queremos", 
    "sem sucesso", "não entendemos", "não há", "não percebo", "não estamos", "não compreendo"
}

atenuadores = {
    "pouco", "levemente", "ligeiramente", "um pouco", "raramente", "ocasionalmente", 
    "quase", "ligeiro", "delicadamente", "modicamente", "morno", "fraco", "reduzido",
    "parcialmente", "mínimo", "moderadamente", "sutilmente", "nada", "em parte", "quase nada",
    "bem pouco", "pouquíssimo", "quase nada", "algo", "esporadicamente", "meia boca",
    "moderado", "morno", "dificilmente", "relativamente"
}

intensificadores = {
    "muito", "super", "extremamente", "demais", "totalmente", "completamente", "incrivelmente", 
    "absolutamente", "enormemente", "intensamente", "realmente", "impressionantemente", 
    "incontáveis", "surpreendentemente", "radicalmente", "incessantemente", "avassaladoramente", 
    "exageradamente", "excepcionalmente", "fortemente", "incansavelmente", "profundamente", 
    "sustancialmente", "intensivo", "delirantemente", "perfeitamente", "violentamente", 
    "exaltadamente", "inquestionavelmente", "incontestavelmente", "infinitamente", "maravilhosamente",
    "incomensuravelmente", "absolutamente", "infelizmente", "espetacularmente", "absurdamente"
}
