import httpx
from app.core.config import GEMINI_API_KEY

async def gerar_pergunta_gemini(topico: str):
    prompt = (
        f"Crie uma pergunta objetiva sobre {topico}. "
        f"Dê 4 alternativas, indique a correta e forneça feedbacks. "
        f"Responda em JSON com 'pergunta', 'alternativas', 'correta', 'feedbacks'."
    )

    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
    headers = { "Content-Type": "application/json" }
    params = { "key": GEMINI_API_KEY }

    body = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, params=params, json=body)

    if response.status_code == 200:
        try:
            text = response.json()['candidates'][0]['content']['parts'][0]['text']
            return {"resposta": text}
        except Exception as e:
            return {"erro": "Formato inesperado", "detalhes": str(e)}
    else:
        return {"erro": "Erro ao chamar a API do Gemini", "status": response.status_code}
