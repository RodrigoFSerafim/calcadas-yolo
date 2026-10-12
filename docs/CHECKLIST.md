# Checklist CPZÃO — entrega 13/10

## Dataset (4 pts)
- [ ] ≥ 60 imagens rotuladas (ideal 100–150)
- [ ] 4 classes finais, nomes iguais no `data.yaml`
- [ ] Split train/valid/test (70/20/10)
- [ ] `python scripts/dataset_stats.py` rodado e colado no README

## Treino e métricas (6 pts)
- [ ] `python scripts/check_gpu.py` → CUDA True
- [ ] `python scripts/train.py`
- [ ] `python scripts/evaluate.py` (métricas no teste)
- [ ] Copiar para `assets/`: `results.png`, `confusion_matrix.png`, `PR_curve.png`, `val_batch0_pred.jpg`
- [ ] Preencher tabela de métricas e análise da matriz de confusão no README

## Exportação e deploy (6 pts)
- [ ] `python scripts/export_model.py` → `models/calcadas.onnx`
- [ ] Modelo copiado para `public/models/` do yoloinferApp
- [ ] Testado no celular (câmera traseira, caixas aparecendo)
- [ ] Vídeo curto de backup da demo gravado

## GitHub e apresentação (4 pts)
- [ ] README completo, com Nome e RM de todos
- [ ] Notebook limpo (`notebooks/treino_exportacao.ipynb`)
- [ ] Modelo no repositório (ou link, se grande)
- [ ] Repositório público/compartilhado com o professor
- [ ] Roteiro da apresentação ensaiado (problema → dados → métricas → demo)
