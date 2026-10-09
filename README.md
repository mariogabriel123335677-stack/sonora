# SONORA — Music Discovery Lab

Aplicação web Python sem chave de API e sem cadastro. Usa a API pública de busca do iTunes para pesquisar faixas e prévias quando disponíveis. Mantém as 24 músicas iniciais no catálogo.

## Publicar no Render

1. Extraia este ZIP.
2. Envie os quatro arquivos para um repositório no GitHub.
3. No Render, selecione **New + → Blueprint** e conecte o repositório que contém `render.yaml`.
4. Confirme a criação do serviço. O Render usará `render.yaml` e fornecerá um endereço público `onrender.com`.

Alternativa: crie um **Web Service** conectado ao repositório, use `pip install -r requirements.txt` como Build Command e `python sonora_dinamico.py` como Start Command.

## Executar localmente

Requer Python 3.10 ou superior. Execute:

```bash
python sonora_dinamico.py
```

Abra `http://127.0.0.1:5000`. Para pesquisa online, o servidor precisa de acesso à internet.

## Observações

- O serviço lê a porta da variável de ambiente `PORT`, como exigido por plataformas de hospedagem.
- No plano gratuito, a instância pode entrar em suspensão após inatividade.
- As prévias de áudio dependem da disponibilidade do iTunes; nem toda faixa tem prévia.
- Recomendações são calculadas por similaridade simples de artistas e gêneros, não por IA generativa.
