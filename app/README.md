# Deploy mobile (yoloinferApp)

O [yoloinferApp](https://github.com/Mjrovai/yoloinferApp) é um app web (Vanilla JS + Vite) que roda a
inferência **no navegador do celular** com ONNX Runtime Web. Não é app nativo.

- Formato aceito: **ONNX**, entrada `[1, 3, 192, 192]`
- Código do app fica na pasta `Code` do repositório original
- Nomes das classes são lidos do próprio modelo ao carregar

## Passo a passo

1. Gere o modelo: `python scripts/export_model.py` → `models/calcadas.onnx`
2. Clone o app (fora desta pasta ou como submódulo):
   ```bash
   git clone https://github.com/Mjrovai/yoloinferApp
   cd yoloinferApp/Code
   npm install
   ```
3. Copie `calcadas.onnx` para `public/models/`
4. Rode em modo dev (já expõe na rede local com HTTPS):
   ```bash
   npm run dev
   ```
5. No celular (mesma rede Wi-Fi do PC), abra o endereço de rede mostrado no terminal
   (aceite o aviso de certificado) e libere a câmera.
6. Pelo botão **Model** do app, carregue o `calcadas.onnx` (ou ajuste o modelo padrão no código).
7. Confirme que está usando a **câmera traseira**.

## Alternativa: publicar no Netlify (link público, ideal para a demo)

```bash
npm run build
netlify deploy --prod --dir=dist
```

Abrir o link pelo celular dá HTTPS válido sem aviso de certificado.

## Se algo falhar

- Câmera não abre: é preciso HTTPS (o `npm run dev` já usa).
- Sem detecções: baixe o limiar de confiança no app e teste com foto de calçada parecida com o dataset.
- Nomes de classe errados: confira o `names` do `data.yaml` usado no treino.
- Confira o README do app original para detalhes que não constam aqui.
