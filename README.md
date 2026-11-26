# Huawei Cloud services icons libraries for draw.io

🌐 **Language**: **English** | [Português](./README.pt.md)

[draw.io](https://www.drawio.com/) is a free and open source cross-platform graph
drawing software developed in HTML5 and JavaScript. Its interface can be used to
create diagrams such as flowcharts, wireframes, UML diagrams, organizational
charts and network diagrams.

Using the provided libraries you can draw [Huawei Cloud](https://www.huaweicloud.com/intl/en-us/)
system architectures.

The libraries are organized by service category (Compute, Networking, Databases,
Analytics, and so on), plus a **Groups** library with architecture container
shapes (Huawei Cloud, Region, AZ, VPC, Subnet, Security Group, CCE, AS Group and
the **MRS cluster**). All icons are the color icons you see in the Console and in
the product pages.

> ℹ️ The old black-and-white **line** libraries were removed in v4.0.

## 🚀 Workflow 1 — draw.io on the web (one click)

Open [app.diagrams.net](https://app.diagrams.net) with **all 15 libraries
loaded at once** — each category appears as its own group in the left
**Shapes** panel. Nothing to download or unzip:

[**Add all libraries to draw.io**](https://app.diagrams.net/?splash=0&libs=0&clibs=Uhttps%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fwallacelw%2Fdrawio-libraries%40v4.3%2Fcolor%2FHWC%20Analytics%20%28color%29.xml;Uhttps%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fwallacelw%2Fdrawio-libraries%40v4.3%2Fcolor%2FHWC%20Artificial%20Intelligence%20%28color%29.xml;Uhttps%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fwallacelw%2Fdrawio-libraries%40v4.3%2Fcolor%2FHWC%20Business%20Applications%20%28color%29.xml;Uhttps%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fwallacelw%2Fdrawio-libraries%40v4.3%2Fcolor%2FHWC%20Compute%20and%20Containers%20%28color%29.xml;Uhttps%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fwallacelw%2Fdrawio-libraries%40v4.3%2Fcolor%2FHWC%20Databases%20%28color%29.xml;Uhttps%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fwallacelw%2Fdrawio-libraries%40v4.3%2Fcolor%2FHWC%20Developer%20Services%20%28color%29.xml;Uhttps%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fwallacelw%2Fdrawio-libraries%40v4.3%2Fcolor%2FHWC%20Flexus%20%28color%29.xml;Uhttps%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fwallacelw%2Fdrawio-libraries%40v4.3%2Fcolor%2FHWC%20Groups.xml;Uhttps%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fwallacelw%2Fdrawio-libraries%40v4.3%2Fcolor%2FHWC%20Management%20and%20Governance%20%28color%29.xml;Uhttps%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fwallacelw%2Fdrawio-libraries%40v4.3%2Fcolor%2FHWC%20Middleware%20%28color%29.xml;Uhttps%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fwallacelw%2Fdrawio-libraries%40v4.3%2Fcolor%2FHWC%20Migration%20%28color%29.xml;Uhttps%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fwallacelw%2Fdrawio-libraries%40v4.3%2Fcolor%2FHWC%20Misc%20%28color%29.xml;Uhttps%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fwallacelw%2Fdrawio-libraries%40v4.3%2Fcolor%2FHWC%20Networking%20%28color%29.xml;Uhttps%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fwallacelw%2Fdrawio-libraries%40v4.3%2Fcolor%2FHWC%20Security%20and%20Compliance%20%28color%29.xml;Uhttps%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fwallacelw%2Fdrawio-libraries%40v4.3%2Fcolor%2FHWC%20Storage%20%28color%29.xml)

The link loads the libraries from [jsDelivr](https://www.jsdelivr.com/)
pinned to the latest release tag, so it always serves the published version.

## 💿 Workflow 2 — draw.io Desktop on Windows 11 (online or offline)

1. Install [draw.io Desktop](https://github.com/jgraph/drawio-desktop/releases)
   (`winget install JGraph.Draw`) if you don't have it yet.
2. Download the latest release zip from the [Releases](../../releases) page
   and extract it.
3. In draw.io, click **File > Open Library from > Device…** and open each XML
   from the `color/` folder — a one-time setup (draw.io takes one file at a
   time). Every category then appears as its own group in the Shapes panel.
4. To remove a library later, click the **X** beside its name in the Shapes panel.

![Adding libraries to draw.io](img/drawio-install-library.gif)

## 🧩 Workflow 3 — VS Code (editor + AI agents)

Open this repository as a workspace in VS Code and you get:

1. **The editor**: install the
   [Draw.io Integration](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio)
   extension (`hediet.vscode-drawio`) — VS Code offers it automatically via
   the workspace extension recommendation. `.drawio` files open as editable
   diagrams, and the diagram XML stays plain text, so it diffs and merges like
   any other file.
2. **The shapes**: the committed `.vscode/settings.json` loads all 15
   per-category libraries into the editor's shape sidebar — each category
   (Analytics, Databases, Networking, Groups, …) appears as its own group,
   with no manual library setup.
3. **AI diagrams in chat (GitHub Copilot)**: the committed `.vscode/mcp.json`
   adds the official draw.io MCP server. Ask Copilot to draw something
   ("draw an MRS cluster architecture") and the diagram renders inline in
   the chat.
4. **AI agents with the drawio skill**:
   - **OpenCode**: drop the
     [drawio skill](https://github.com/jgraph/drawio-mcp/tree/main/plugins/claude-code)
     into `~/.config/opencode/skills/drawio/` and the `@drawio/mcp` tool
     server into the `mcp_servers` of your `opencode.json`, then ask the agent
     to create `.drawio` files — they render in the editor tab next to the
     chat.
   - **Claude Code**: `/plugin marketplace add jgraph/drawio-mcp` then
     `/plugin install drawio@drawio`.
   - Any agent can also read and edit `.drawio` files as plain XML — the
     diagram view refreshes as the file changes.

## 🌟 Architecture examples

![Architecture 1](img/architecture-1.png)

![Architecture 2](img/architecture-2.png)

## 📚 Library contents

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

## 🗂 Groups (container shapes)

The **HWC Groups** library contains architecture container shapes:
**Huawei Cloud**, **Region**, **Availability Zone (AZ)**, **Virtual Private
Cloud (VPC)**, **Subnet**, **Security Group**, **Cloud Container Engine (CCE)**,
**Auto Scaling Group** and the **MRS cluster** (with Master / Core / Task node
groups). Groups are intentionally *not* containers: icons placed inside them do
not move when you resize the bounding rectangle.

## 🛠 Repository structure and contributing

```
src/icons/<Category>/<Service>.svg   # source SVG icons (editable)
src/groups/<Group>.xml               # group shape templates
src/manifest.json                    # icon order and metadata per library
tools/extract.py                     # extract existing .xml libraries into src/
tools/build.py                       # rebuild color/ from src/ (use --check to validate)
tools/links.py                       # regenerate the one-click install links
color/                               # generated draw.io libraries, one per category
.vscode/                             # draw.io extension, MCP server and library config
```

To add or update an icon: drop the SVG in `src/icons/<Category>/`, add it to
`src/manifest.json`, run `python3 tools/build.py`, and open a pull request.
Please keep SVGs square (72×72 viewBox recommended) and use the official
service name as the title.

## 📄 License and notices

The code and documentation in this repository are licensed under the MIT
License — see [LICENSE](./LICENSE).

Icon artwork and service names are © Huawei Technologies Co., Ltd. They are
collected from Huawei Cloud public product pages and redistributed here for
architecture-diagram interoperability, with no claim of ownership or official
endorsement. **Huawei Cloud** and the service names are trademarks of Huawei —
see [NOTICE](./NOTICE).

## 📝 Changelog

See [CHANGELOG.md](./CHANGELOG.md).
