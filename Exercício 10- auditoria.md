| ID | Falha / Vetor | Código OWASP (2025) | Impacto | Correção Aplicada |
| :--- | :--- | :--- | :--- | :--- |
| **1** | SQL Injection em `/api/usuarios/buscar` | A03:2025 — Injeção | Extração e alteração de dados. | Queries parametrizadas com placeholders (`%s`). |
| **2** | XSS Refletido em `/perfil` | A05:2025 — Insecure Design | Execução de script no browser. | Motor Jinja2 com escape automático ativo. |
| **3** | Falta de Autenticação em `DELETE` *(Ausência 1)* | A01:2025 — Broken Access Control | Destruição de registos sem credenciais. | Validação obrigatória por API Key e restrição de níveis. |
| **4** | Exposição de Stack Trace / Erros | A04:2025 — Security Misconfiguration | Divulgação da arquitetura interna. | Tratamento de exceções devolvendo erros genéricos `500`. |
| **5** | Vazamento de Credenciais em Consultas | A02:2025 — Cryptographic Failures | Exposição de colunas sensíveis (senhas). | Omissão explícita de colunas sensíveis na projeção SQL. |
| **6** | Ausência de Headers de Segurança *(Ausência 2)* | A04:2025 — Security Misconfiguration | Vulnerabilidade a Clickjacking e MIME Sniffing. | Inclusão global de CSP, X-Frame-Options e X-Content-Type-Options. |
