# Launcher — Melhorar o sistema FCE

**Menu FCE.md:** Opção 12

---

## Objetivo

Orientar a IA a **melhorar documentação, workflows ou estrutura** do Franklin Creative Engine — de forma mínima, rastreável e sem proliferar engines desnecessárias.

---

## Ordem de leitura obrigatória

1. [FCE.md](../FCE.md)
2. [AGENTS.md](../AGENTS.md)
3. [PROJECT_STRUCTURE.md](../PROJECT_STRUCTURE.md)
4. [WORKFLOW.md](../WORKFLOW.md)
5. [CHANGELOG.md](../CHANGELOG.md) — evitar duplicar melhoria recente
6. [ROADMAP.md](../ROADMAP.md) — ver se já está planejado
7. Buscar no repo — a solução pode **já existir**

---

## Perguntas que a IA deve fazer ao usuário

1. **Qual melhoria específica?** (docs · workflow · template · track · launcher)
2. **Qual problema resolve?** (1 frase)
3. **Escopo mínimo?** — uma faixa vs álbum vs sistema global
4. **Precisa de nova engine/módulo?** (default: **não**)
5. **Autoriza editar quais arquivos?**
6. **Commit e CHANGELOG?** (só se solicitado)

---

## Arquivos que a IA deve consultar

| Área | Onde buscar |
|------|-------------|
| Regras IA | `AGENTS.md` |
| Paths | `PROJECT_STRUCTURE.md` |
| Pipelines | `WORKFLOW.md` |
| Direção criativa | `library/creative_direction_system/` |
| Vídeo | `library/narrative_engine/`, `library/veo3/` |
| Histórico | `CHANGELOG.md` |
| Launchers | `launcher/` |
| Melhoria similar | `grep` / busca semântica no repo |

---

## Saídas esperadas

1. **Diagnóstico** — o que existe hoje vs o que falta
2. **Proposta mínima** — menor diff que resolve o problema
3. **Arquivos a alterar** — lista explícita
4. **O que NÃO fazer** — evitar over-engineering
5. **Entrada CHANGELOG.md** — seção `[Unreleased]` com motivo da mudança
6. **Explicação do motivo** — por que esta mudança, não outra abordagem
7. **Atualizações cruzadas** — se mudar workflow → AGENTS.md + PROJECT_STRUCTURE se necessário

---

## Checklist de qualidade

- [ ] Melhoria solicitada entendida
- [ ] Verificado se solução já existe no FCE
- [ ] Nenhuma engine nova sem necessidade comprovada
- [ ] Escopo mínimo — não refatorar unrelated code
- [ ] CHANGELOG atualizado (quando aplicável)
- [ ] Links cruzados consistentes
- [ ] Não apagar documentação existente
- [ ] Versão/nome em AGENTS ou WORKFLOW se regra mudou

---

## O que a IA não deve fazer

- ❌ Criar nova engine/módulo/API/automação sem necessidade explícita
- ❌ Reorganizar pastas sem atualizar PROJECT_STRUCTURE
- ❌ Apagar docs existentes
- ❌ Alterar letras definitivas
- ❌ Commit/push sem solicitação
- ❌ Expandir arquitetura quando patch documental basta
- ❌ Duplicar conteúdo entre AGENTS, WORKFLOW e launcher sem motivo

---

## Fluxo recomendado

```
Entender melhoria
    ↓
Buscar solução existente
    ↓
Propor diff mínimo
    ↓
Aplicar (se autorizado)
    ↓
CHANGELOG + links cruzados
    ↓
Explicar motivo ao usuário
```

---

**Exemplos válidos:** novo launcher · correção WORKFLOW · stub campanha · doc Sprint  
**Exemplos inválidos:** nova Video Engine · API Suno · refactor álbum inteiro
