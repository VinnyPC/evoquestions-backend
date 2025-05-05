import httpx
from app.core.config import GEMINI_API_KEY

async def gerar_pergunta_gemini(topico: str):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
    headers = {
        "Content-Type": "application/json"
    }

    prompt = (
        f"Crie 10 perguntas objetivas de múltipla escolha sobre {topico}. "
        "Responda apenas como um array JSON com 10 objetos, onde cada objeto contém os campos: "
        "'pergunta', 'alternativas' (com 4 opções), 'correta' (como texto igual a uma das alternativas), e 'feedbacks' (dando explicação para cada alternativa)."
    )

    body = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    async with httpx.AsyncClient(timeout=60.0) as client:
        response = await client.post(url, headers=headers, json=body)

    if response.status_code == 200:
        try:
            resposta = response.json()['candidates'][0]['content']['parts'][0]['text']
            return {"resposta": resposta}
        except Exception as e:
            return {"erro": "Erro ao extrair conteúdo", "detalhes": str(e)}
    else:
        return {"erro": "Erro ao chamar a API Gemini", "status": response.status_code, "body": response.text}
