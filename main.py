import openai

# Substitua 'SUA_CHAVE_DE_API' pela sua chave de API do OpenAI
openai.api_key = 'SUA_CHAVE_DE_API'

def enviar_pergunta(pergunta):
    resposta = openai.Completion.create(
        engine="text-davinci-002",
        prompt=pergunta,
        max_tokens=50,  # Ajuste o número de tokens conforme necessário
    )
    return resposta.choices[0].text

while True:
    pergunta = input("Você: ")
    resposta = enviar_pergunta(pergunta)
    print("ChatGPT: " + resposta)
