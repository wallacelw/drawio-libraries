# Bibliotecas de ícones de serviços Huawei Cloud para draw.io

🌐 **Idioma**: [English](./README.md) | **Português**

[draw.io](https://www.drawio.com/) é um software multiplataforma livre e de
código aberto para desenho de gráficos, desenvolvido em HTML5 e JavaScript. Sua
interface pode ser usada para criar diagramas como fluxogramas, wireframes,
diagramas UML, organogramas e diagramas de rede.

Com as bibliotecas fornecidas você pode desenhar arquiteturas de sistemas
[Huawei Cloud](https://www.huaweicloud.com/intl/pt-br/).

As bibliotecas são organizadas por categoria de serviço (Computação, Redes,
Bancos de dados, Analytics etc.), além de uma biblioteca de **Grupos** com
formas de contêiner de arquitetura (Huawei Cloud, Região, AZ, VPC, Sub-rede,
Security Group, CCE, AS Group e o **cluster MRS**). Todos os ícones são os
ícones coloridos que você vê no Console e nas páginas de produto.

> ℹ️ As antigas bibliotecas em **linha** (preto e branco) foram removidas na
> v4.0.

## 🚀 Fluxo 1 — draw.io na web (um clique)

Abra o [app.diagrams.net](https://app.diagrams.net) com **todas as 15
bibliotecas carregadas de uma vez** — cada categoria aparece como seu próprio
grupo no painel **Formas** à esquerda. Nada para baixar ou descompactar:

[**Adicionar todas as bibliotecas ao draw.io**](https://app.diagrams.net/?splash=0&libs=0&clibs=Uhttps%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fwallacelw%2Fdrawio-libraries%40v4.4%2Fcolor%2FHWC%20Analytics%20%28color%29.xml;Uhttps%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fwallacelw%2Fdrawio-libraries%40v4.4%2Fcolor%2FHWC%20Artificial%20Intelligence%20%28color%29.xml;Uhttps%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fwallacelw%2Fdrawio-libraries%40v4.4%2Fcolor%2FHWC%20Business%20Applications%20%28color%29.xml;Uhttps%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fwallacelw%2Fdrawio-libraries%40v4.4%2Fcolor%2FHWC%20Compute%20and%20Containers%20%28color%29.xml;Uhttps%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fwallacelw%2Fdrawio-libraries%40v4.4%2Fcolor%2FHWC%20Databases%20%28color%29.xml;Uhttps%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fwallacelw%2Fdrawio-libraries%40v4.4%2Fcolor%2FHWC%20Developer%20Services%20%28color%29.xml;Uhttps%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fwallacelw%2Fdrawio-libraries%40v4.4%2Fcolor%2FHWC%20Flexus%20%28color%29.xml;Uhttps%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fwallacelw%2Fdrawio-libraries%40v4.4%2Fcolor%2FHWC%20Groups.xml;Uhttps%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fwallacelw%2Fdrawio-libraries%40v4.4%2Fcolor%2FHWC%20Management%20and%20Governance%20%28color%29.xml;Uhttps%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fwallacelw%2Fdrawio-libraries%40v4.4%2Fcolor%2FHWC%20Middleware%20%28color%29.xml;Uhttps%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fwallacelw%2Fdrawio-libraries%40v4.4%2Fcolor%2FHWC%20Migration%20%28color%29.xml;Uhttps%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fwallacelw%2Fdrawio-libraries%40v4.4%2Fcolor%2FHWC%20Misc%20%28color%29.xml;Uhttps%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fwallacelw%2Fdrawio-libraries%40v4.4%2Fcolor%2FHWC%20Networking%20%28color%29.xml;Uhttps%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fwallacelw%2Fdrawio-libraries%40v4.4%2Fcolor%2FHWC%20Security%20and%20Compliance%20%28color%29.xml;Uhttps%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fwallacelw%2Fdrawio-libraries%40v4.4%2Fcolor%2FHWC%20Storage%20%28color%29.xml)

O link carrega as bibliotecas do [jsDelivr](https://www.jsdelivr.com/)
fixadas na tag da versão mais recente, então ele sempre serve a versão
publicada.

## 💿 Fluxo 2 — draw.io Desktop no Windows 11 (online ou offline)

1. Instale o [draw.io Desktop](https://github.com/jgraph/drawio-desktop/releases)
   (`winget install JGraph.Draw`) se ainda não tiver.
2. Baixe o zip da release mais recente na página de
   [Releases](../../releases) e extraia-o.
3. No draw.io, clique em **File > Open Library from > Device…** e abra cada XML
   da pasta `color/` — configuração única (o draw.io aceita um arquivo por
   vez). Cada categoria então aparece como seu próprio grupo no painel de
   Formas.
4. Para remover uma biblioteca depois, clique no **X** ao lado do nome dela no
   painel de Formas.

![Adicionando bibliotecas ao draw.io](img/drawio-install-library.gif)

## 🧩 Fluxo 3 — VS Code + seu CLI de IA (opencode ou Claude Code)

O editor e o agente são ferramentas separadas que se encontram no arquivo
`.drawio`: o VS Code renderiza o diagrama, e seu agente de código — opencode
ou Claude Code, sem GitHub Copilot — cria e edita o arquivo.

### Configuração única

1. **Editor**: instale a extensão
   [Draw.io Integration](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio)
   (`hediet.vscode-drawio`) — o VS Code oferece automaticamente via
   recomendação de extensões do workspace. Arquivos `.drawio` abrem como
   diagramas editáveis, e o XML do diagrama continua sendo texto simples,
   com diff e merge como qualquer arquivo.
2. **Formas**: o `.vscode/settings.json` versionado carrega as 15 bibliotecas
   por categoria na barra lateral de formas do editor — cada categoria
   aparece como seu próprio grupo, sem configuração manual.
3. **Agente** — escolha um:
   - **opencode**: instale o CLI em [opencode.ai](https://opencode.ai),
     adicione a extensão oficial do VS Code (`sst-dev.opencode`, abre o
     opencode em um terminal dividido com `Ctrl+Esc`) — ou simplesmente
     execute `opencode` no terminal integrado. Depois dê a ele a skill
     drawio: copie a pasta da
     [skill drawio](https://github.com/jgraph/drawio-mcp/tree/main/plugins/claude-code)
     para `~/.config/opencode/skills/drawio/`. Opcionalmente adicione o
     servidor de ferramentas `@drawio/mcp` ao seu `opencode.json` para que os
     diagramas também abram no navegador:

     ```json
     "mcp_servers": {
       "drawio": { "type": "local", "command": ["npx", "-y", "@drawio/mcp"] }
     }
     ```

   - **Claude Code**: execute `claude` no terminal integrado (ou instale a
     extensão do VS Code) e adicione o plugin drawio:

     ```
     /plugin marketplace add jgraph/drawio-mcp
     /plugin install drawio@drawio
     ```

### Como funcionam juntos

- Peça um diagrama ao agente — *"crie um .drawio de uma arquitetura Huawei
  Cloud: um ELB na frente de dois servidores ECS, RDS atrás deles e um
  cluster MRS"*. Ele escreve o arquivo `.drawio` e o abre; a extensão
  renderiza em uma aba do editor.
- Itere no chat: o agente edita o XML do diagrama e o diagrama aberto
  atualiza conforme o arquivo muda — diffs e reviews funcionam como código.
- O agente pode usar as formas deste repositório diretamente:
  `src/icons/<Categoria>/<Serviço>.svg` são SVGs simples que ele pode
  embutir, e `src/groups/*.xml` são modelos de contêiner prontos (incluindo o
  cluster MRS) que ele pode copiar para os diagramas.

## 🌟 Exemplos de arquitetura

![Arquitetura 1](img/architecture-1.png)

![Arquitetura 2](img/architecture-2.png)

## 📚 Conteúdo das bibliotecas

- **Analytics (color)** — 13 shapes
- **Artificial Intelligence (color)** — 49 shapes
- **Business Applications (color)** — 20 shapes
- **Compute and Containers (color)** — 19 shapes
- **Databases (color)** — 17 shapes
- **Developer Services (color)** — 23 shapes
- **Flexus (color)** — 9 shapes
- **Groups** — 9 shapes
- **Management and Governance (color)** — 16 shapes
- **Middleware (color)** — 15 shapes
- **Migration (color)** — 5 shapes
- **Misc (color)** — 29 shapes
- **Networking (color)** — 12 shapes
- **Security and Compliance (color)** — 19 shapes
- **Storage (color)** — 13 shapes

## 🗂 Grupos (formas de contêiner)

A biblioteca **HWC Groups** contém formas de contêiner de arquitetura:
**Huawei Cloud**, **Região**, **Zona de Disponibilidade (AZ)**, **Virtual
Private Cloud (VPC)**, **Sub-rede**, **Security Group**, **Cloud Container
Engine (CCE)**, **Auto Scaling Group** e o **cluster MRS** (com grupos de nós
Master / Core / Task). Os grupos *não* são contêineres de propósito: ícones
colocados dentro deles não se movem quando você redimensiona o retângulo.

## 🛠 Estrutura do repositório e como contribuir

```
src/icons/<Categoria>/<Serviço>.svg   # ícones SVG de origem (editáveis)
src/groups/<Grupo>.xml                 # modelos de formas de grupo
src/manifest.json                     # ordem e metadados dos ícones por biblioteca
tools/extract.py                      # extrai as bibliotecas .xml existentes para src/
tools/build.py                        # reconstrói color/ a partir de src/ (use --check para validar)
tools/links.py                        # regenera os links de instalação com um clique
color/                                # bibliotecas draw.io geradas, uma por categoria
.vscode/                              # configuração da extensão draw.io e da biblioteca
```

Para adicionar ou atualizar um ícone: coloque o SVG em `src/icons/<Categoria>/`,
adicione-o ao `src/manifest.json`, execute `python3 tools/build.py` e abra um
pull request. Mantenha os SVGs quadrados (viewBox 72×72 recomendado) e use o
nome oficial do serviço como título.

## 📄 Licença e avisos

O código e a documentação deste repositório estão licenciados sob a licença MIT —
veja [LICENSE](./LICENSE).

A arte dos ícones e os nomes dos serviços são © Huawei Technologies Co., Ltd.
Foram coletados das páginas públicas de produtos da Huawei Cloud e são
redistribuídos aqui para interoperabilidade de diagramas de arquitetura, sem
qualquer alegação de propriedade ou endosso oficial. **Huawei Cloud** e os nomes
dos serviços são marcas da Huawei — veja [NOTICE](./NOTICE).

## 📝 Changelog

Veja [CHANGELOG.md](./CHANGELOG.md).
