# Auditoria de Calçadas com YOLO — CPZÃO (CP2 + CP3)

Detecção de defeitos, obstáculos e elementos de acessibilidade em calçadas com **YOLOv8n**,
rodando em tempo real no celular via **yoloinferApp** (ONNX Runtime Web).

## Integrantes

| Nome | RM |
| :--- | :--- |
| Rodrigo | 550816 |

**Turma:** 4ESPG · **Instituição:** FIAP

## 1. Problema

A qualidade das calçadas e a acessibilidade urbana são desafios em grandes cidades. Este projeto
automatiza parte da auditoria de calçadas detectando, em imagens e em tempo real pela câmera do
celular, itens relevantes para a caminhabilidade e a acessibilidade.

Referência de metodologia: [Auditoria de Calçadas](https://falzoni.com.br/auditoriacalcadas/)

## 2. Classes

| ID | Classe | Descrição |
| :-: | :--- | :--- |
| 0 | `buraco_trinca` | Buracos, rachaduras e pisos danificados |
| 1 | `lixo` | Lixo, entulho e resíduos em circulação |
| 2 | `piso_liso` | Trechos lisos, de difícil aderência ou pavimento irregular |
| 3 | `poste_obstaculo` | Postes, placas, mobiliário ou outros obstáculos na faixa de passagem |

> Os nomes e a ordem dos IDs seguem o `dataset/data.yaml` final do Roboflow.

## 3. Dataset

- Fonte: notebook de aquisição do professor + projeto de referência
- Anotação: Roboflow (formato YOLOv8)
- Split: 70% treino / 20% validação / 10% teste

Estatísticas (saída de `python scripts/dataset_stats.py`):

```
(colar aqui)
```

## 4. Treinamento

- Modelo: `yolov8n.pt` (pré-treinado COCO)
- Hardware: NVIDIA RTX 4060
- Hiperparâmetros: epochs=_, imgsz=192, batch=_, patience=30
- Resolução 192 escolhida por ser a entrada do yoloinferApp, então as métricas refletem o modelo implantado

```bash
python scripts/train.py
python scripts/evaluate.py
```

## 5. Resultados (conjunto de teste)

| Métrica | Valor |
| :--- | :-: |
| mAP@50 | _ |
| mAP@50-95 | _ |
| Precision | _ |
| Recall | _ |

mAP@50 por classe: _(colar)_

### Curvas e matriz de confusão

![Curvas de treino](assets/results.png)
![Matriz de confusão](assets/confusion_matrix.png)
![Curva PR](assets/PR_curve.png)

### Análise

_(Quais classes tiveram melhor/pior desempenho? Quais foram confundidas na matriz e por quê?
Limitações: poucas imagens, resolução 192, variação de iluminação, etc.)_

## 6. Exportação

```bash
python scripts/export_model.py
```

Gera `models/calcadas.onnx` (entrada `[1, 3, 192, 192]`).

## 7. Deploy mobile

O yoloinferApp roda no navegador do celular. Passo a passo completo em [`app/README.md`](app/README.md).

Resumo: copiar `calcadas.onnx` para `public/models/` do app → `npm install && npm run dev` →
abrir o endereço de rede no celular → liberar a câmera traseira.

📹 Demo: _(link do vídeo, se houver)_

## 8. Como reproduzir

```bash
python -m venv .venv
.venv\Scripts\activate            # Windows
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu126
pip install -r requirements.txt
python scripts/check_gpu.py      # deve imprimir CUDA True
```

Baixe o dataset do Roboflow (formato YOLOv8) para `dataset/` e rode os scripts da seção 4 e 6.

## 9. Estrutura

```
calcadas-yolo/
├── README.md
├── requirements.txt
├── app/README.md              # como integrar ao yoloinferApp
├── dataset/data.yaml          # config do dataset (imagens ficam fora do Git)
├── docs/CHECKLIST.md
├── models/                    # best.pt e calcadas.onnx
├── notebooks/treino_exportacao.ipynb
├── scripts/                   # train, evaluate, export_model, predict_test, dataset_stats, check_gpu
└── assets/                    # gráficos e prints para o README
```
