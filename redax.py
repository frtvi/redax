import openai
openai.api_key = "sua-API-key-openai"

def gerar_texto(pergunta):
    model_engine = "text-davinci-002"
    # modelo GPT-3 que será utilizado, davinci é o mais confiável    
    prompt = f"Por favor, escreva um texto do tipo {tipotexto} sobre o tema: {pergunta}\nResposta: "
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1250,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text.strip()
    return message

# exemplo de uso
tipotexto = input("Digite o tipo do texto: ")
pergunta = input("Digite um tema: ")
resposta = gerar_texto(pergunta)
print("Resposta: ", resposta)

input() 
