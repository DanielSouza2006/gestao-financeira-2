# TODO - Correções do Controle Financeiro

- [ ] Levantar e alinhar schema do SQLite (users, transacoes) no `gestao_financeira.db`
- [ ] Atualizar `api.py`:
  - [ ] Criar tabelas no SQLite
  - [ ] Implementar `POST /register`
  - [ ] Implementar `POST /login` com token
  - [ ] Implementar `GET /transacoes` e `POST /transacoes` protegidos por token
- [ ] Atualizar `app.py` (Streamlit):
  - [ ] Ler token via query param
  - [ ] Bloquear UI sem token
  - [ ] Buscar e salvar transações via API
- [ ] Atualizar `index.html` e `script.js`:
  - [ ] Corrigir cadastro (inputs e submit)
  - [ ] Implementar chamada ao endpoint de registro
  - [ ] Guardar token e redirecionar para Streamlit com `?token=`
- [ ] Validar manualmente:
  - [ ] Register → Login → adicionar transação → recarregar página mantém histórico
- [ ] Executar `python api.py` e Streamlit (8501) e verificar fluxo completo

