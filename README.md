<p align="center">
  <img src="Github-Assets/banner.png" alt="Banner do Project LUMI" width="100%" />
</p>

<h1 align="center">🤖 Project LUMI</h1>

<p align="center">
  <b>Assistente Culinário Inteligente com IA, Interação por Voz e Robô Físico</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/status-em%20desenvolvimento-yellow" />
  <img src="https://img.shields.io/badge/version-0.1.0-blue" />
  <img src="https://img.shields.io/badge/python-3.11+-blue?logo=python" />
  <img src="https://img.shields.io/badge/FastAPI-Backend-green?logo=fastapi" />
  <img src="https://img.shields.io/badge/IA-OpenAI-orange" />
  <img src="https://img.shields.io/badge/Plataforma-Raspberry%20Pi-red?logo=raspberrypi" />
</p>

---

## 🎯 Sobre o Projeto

O **Project LUMI** é um assistente culinário inteligente projetado para acompanhar o usuário durante **todo o processo de preparo de receitas**.  
Ele interage principalmente por **voz**, mantém **memória contextual**, gerencia **fluxos culinários** e integra um **robô físico** como sua principal interface.

Diferente dos assistentes tradicionais, a LUMI foi arquitetada utilizando um **sistema cognitivo híbrido**, onde:

> **A Inteligência Artificial é utilizada apenas quando realmente agrega valor.**  
> A maior parte do processamento é realizada através de **lógica determinística, reconhecimento de padrões e respostas programadas**, garantindo:
>
> - ⚡ Baixa latência  
> - 💸 Baixo custo operacional  
> - 🧠 Alta confiabilidade  
> - 🤖 Interação natural  

---

## ✨ Funcionalidades Principais

- 🎙️ Interação por voz (Speech-to-Text & Text-to-Speech)
- 🧠 Memória contextual do preparo
- ⏱️ Timers inteligentes e controle de etapas
- 🤖 Interface por robô físico
- 🎭 Sistema de emoções no display
- 🧩 Processamento híbrido (IA + lógica determinística)
- 🧠 Roteamento inteligente de intenções
- 📷 Análise de imagens sob demanda
- 🔄 Monitoramento ativo do preparo ("prova de vida")

---

## 🧠 Arquitetura Cognitiva

A LUMI processa comandos através de um **pipeline cognitivo em três camadas**:

| Camada | Descrição | Uso de IA |
|-----------|--------------|-------------|
| 🟢 Motor Scriptado | Timers, alarmes, comandos, respostas rápidas, piadas, status | 0% |
| 🟡 Motor Híbrido | Sugestões, explicações, avaliação de imagens | Parcial |
| 🔴 Motor IA | Conversa livre, criatividade, raciocínio complexo | Total |

### Fluxo de Processamento

        Entrada do Usuário (Voz / Texto)
                      ↓
           Speech-to-Text (se voz)
                      ↓
                 Roteador de Intenção
                      ↓
    ┌────────────┬──────────────┬─────────────┐
    │  Motor     │    Motor     │    Motor    │
    │ Scriptado  │   Híbrido    │      IA     │
    └────────────┴──────────────┴─────────────┘
                      ↓
            Motor Emocional → Display
                      ↓
           Motor de Resposta → Voz / Texto



---

## 🎭 Sistema de Emoções

A LUMI utiliza uma **máquina de estados simples** para exibir emoções em seu display:

| Estado | Emoção |
|-----------|----------|
| Idle | 😴 |
| Ouvindo | 🎙️ |
| Processando | 🤔 |
| Falando | 🙂 |
| Feliz | 😄 |
| Brincando | 😆 |
| Erro | 😵 |

---

## ⏱️ Monitoramento Ativo do Preparo

A LUMI acompanha a interação do usuário e realiza **check-ins automáticos inteligentes**:

| Tempo Sem Interação | Ação |
|----------------------|--------|
| 5 minutos | "Está tudo bem por aí?" |
| 10 minutos | "Como está indo a receita?" |
| Sensível ao contexto | Perguntas inteligentes baseadas no estado atual |

---

## 🛠️ Stack Tecnológica

### Backend

| Tecnologia | Finalidade |
|--------------|---------------|
| Python 3.11+ | Linguagem principal |
| FastAPI | Framework REST |
| PostgreSQL / SQLite | Persistência |
| Redis | Cache & memória |
| OpenAI API | Raciocínio com IA |
| Docker (futuro) | Deploy |

---

### Robô Físico

| Componente | Finalidade |
|----------------|---------------|
| Raspberry Pi | Controlador central |
| Microfone | Captura de voz |
| Alto-falantes | Reprodução de voz |
| Display OLED / LCD | Emoções |
| Carcaça 3D | Estrutura física |

---

## 🏗️ Arquitetura do Sistema

    🤖 Robô Físico
             ↓
      Backend Central
    (Python + FastAPI)
             ↓
    IA + Memória + Lógica
             ↓
    Banco de Dados & Cache


---

## 🗺️ Roadmap do Projeto

| Fase | Nome | Objetivo | Principais Entregas | Status |
|--------|-------|-------------|------------------------|----------|
| 0 | Fundação | Definir identidade, arquitetura e visão do projeto | Conceito, arquitetura, diagramas, README, estrutura dos repositórios | ✅ Concluída |
| 1 | Backend Core (MVP Cognitivo) | Construir o núcleo inteligente do sistema | FastAPI, Intent Router, Sessions, Timers, UseCases, arquitetura limpa | 🚧 Em andamento |
| 2 | Robô Lumi (Voz + Interface Física) | Implementar interação por voz e controle do robô | STT, TTS, Wake-word, Backend Client, loop principal | 🚧 Em andamento |
| 3 | Motor Culinário | Criar o sistema de acompanhamento de receitas | Fluxo de receitas, etapas, timers automáticos, contexto | ⏳ Planejada |
| 4 | IA Avançada | Integrar IA híbrida e otimizada | AI Providers, fallback, prompt engineering, cache | 🚧 Em andamento |
| 5 | Robô Físico | Construir o protótipo físico | Raspberry Pi, áudio, display, carcaça 3D | ⏳ Planejada |
| 6 | Polimento & Portfólio | Finalização e apresentação profissional | Refatoração, testes, documentação final, vídeos | ⏳ Planejada |

---

### 📌 Status Atual

**Fase 1 e Fase 2 em desenvolvimento simultâneo.**

---

## 🖼️ Mídia — Fotos & Vídeos

> Esta seção conterá **fotos reais, vídeos e demonstrações** do desenvolvimento e montagem física da LUMI.

---

## 🎯 Objetivo do Projeto

Este projeto foi criado como um **projeto âncora de portfólio**, com o objetivo de demonstrar:

| Habilidade | Descrição |
|---------------|--------------|
| 🧠 Engenharia de Software | Arquitetura limpa, design modular |
| ⚙️ Desenvolvimento Backend | APIs, persistência, serviços |
| 🤖 IA Aplicada | Uso real, otimização de custos |
| 🎙️ Sistemas de Voz | Integração STT + TTS |
| 🔧 Robótica | Integração hardware + software |
| 🎨 Design de Produto | UX, emoção e experiência |

---

## 👨‍💻 Autor

Desenvolvido por **Diogo Teodoro**  
Estudante de Sistemas de Informação  
Entusiasta em Backend e IA 

---

<p align="center">
  🚀 Construído com paixão, curiosidade e muito café.
</p>


