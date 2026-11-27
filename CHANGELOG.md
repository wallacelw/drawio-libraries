# Changelog

## [v4.4] - 2026-11-26

### Changed

- **Workflow 3 rewritten around AI CLI agents** (opencode, Claude Code)
  instead of GitHub Copilot: documents the opencode VS Code extension
  (`sst-dev.opencode`) or integrated terminal, the drawio skill install, the
  optional `@drawio/mcp` tool server, the Claude Code drawio plugin, and how
  agents can embed shapes directly from `src/icons/` and `src/groups/`

### Removed

- `.vscode/mcp.json` (only consumed by VS Code's native Copilot integration;
  CLI agents configure the drawio MCP server at user level instead)

## [v4.3] - 2026-11-26

### Changed

- Simplified the README install instructions to a single **add-all** option per
  workflow: one-click link on the web, release zip on draw.io Desktop, and the
  committed workspace config in VS Code. The per-category install table was
  removed; per-library links are still available through `tools/links.py`
  (`--format json` or `plain`)

## [v4.2] - 2026-11-26

### Changed

- **Removed the All-in-One library**: draw.io shows each library file as one
  flat section in the Shapes panel, so a single big file meant one long
  ungrouped list. Every workflow now uses the 15 per-category libraries —
  each appears as its own group:
  - the VS Code workspace config (`.vscode/settings.json`) loads all 15
    libraries, one sidebar group per category
  - draw.io Desktop offline installs open the files from `color/` (one-time)
  - the one-click table and install-all link are unchanged

## [v4.1] - 2026-11-26

### Added

- **All-in-One library** (`all-in-one/HWC All-in-One (color).xml`): every icon
  and group in a single file — one file to open in draw.io Desktop offline,
  one entry in the VS Code extension config, one one-click link
- **Three documented workflows** in the README (English and Portuguese):
  draw.io on the web (one-click), draw.io Desktop on Windows 11 (online or
  offline, including `winget install JGraph.Draw`), and VS Code
- **VS Code workspace config**: `.vscode/settings.json` auto-loads the
  All-in-One library into the Draw.io Integration extension,
  `.vscode/mcp.json` adds the official draw.io MCP server (inline AI diagrams
  in Copilot chat), `.vscode/extensions.json` recommends the extension
- README guidance for AI agents: drawio skill setup for OpenCode and
  Claude Code, and editing `.drawio` files as plain XML

### Changed

- CI now validates the All-in-One library too; releases package it alongside
  the per-category libraries

## [v4.0] - 2026-11-25

### Added

- **One-click installation**: the README now has a table with links that open
  app.diagrams.net with each library (or all of them at once) loaded straight
  from the jsDelivr CDN — no download, no unzip, one click
- **MRS cluster group** (Groups library): outer container with Master, Core and
  Task node-group panels and example node chips
- Artificial Intelligence: **ModelArts Studio (MaaS)**, **ModelArts Versatile**,
  **CloudRobo**
- Compute and Containers: **CCE Autopilot**, **CloudDC**
- Developer Services: **CodeArts Doer**
- Public source tree (`src/`) and build pipeline (`tools/`): every icon is now
  an editable SVG file; `tools/build.py` regenerates the XML libraries and
  `--check` validates them
- CI validates all libraries on every push; releases are built and published
  automatically on tags
- `LICENSE` (MIT, code and docs) and `NOTICE` (Huawei icon attribution)

### Changed

- Pangu renamed to **Pangu Large Models**
- Fixed icon title typos: Cloud Application Egine → Engine (CAE), Log Tank
  Servce → Service (LTS), Data Encryption Worshop → Workshop (DEW),
  FGPA → FPGA (FACS)
- README rewritten (English and Portuguese) with one-click, URL, offline and
  VS Code install instructions

### Removed

- **Legacy line (black and white) libraries** — they were no longer maintained
- Security: **Situation Awareness (SA)** — service retired; SecMaster is the
  go-forward name

## [v3.2] - 2025-01-30

### Added

- **First version to be published**
- **Flexus icon library**
- Storage/**Scalable File Service (SFS) Turbo**
- Management and Governance: **Cloud Operations Center (COC)**, **Resource Governance Center (RGC)**
- Compute and Containers/Dedicated Computing Cluster (DCC)
- Artificial Intelligence: City Intelligent Twins (iCityS), Octopus, Smart OCR
- Analytics/DataArts Insight (Modern BI)
- Security and Compliance: CodeArts Inspector, Network Detection and Response (NDR)
- Developer Services/CodeArts: Board, Defect, Governance, Modeling, Release

### Changed

- **Analytics:**
  - Data Warehouse Service (DWS) renamed to GaussDB(DWS)
  - DataArts renamed to DataArts Studio
  - Log renamed to Log Analysis Service (LOG)
- **Databases:**
  - GaussDB openGAUSS renamed to GaussDB
  - TaurusDB (GaussDB for MySQL) renamed to TaurusDB
  - GaussDB for NoSQL renamed to GeminiDB
  - GaussDB for Cassandra/Influx/Mongo/Redis renamed to GeminiDB for Cassandra/Influx/Mongo/Redis
- Compute and Containers grouped into single library
- Application, Middleware, Blockchain and App Service grouped into Middleware library
- Security and Compliance/SSL Certificate Manager (SCM) renamed to Cloud Certificate Manager (CCM)
- Content Delivery, Edge Computing, IoT, aPaaS and Video grouped into single Misc library
- Intelligence EdgeSite (IES) renamed to CloudPond (IES)
- Artificial Intelligence/Image Moderation renamed to Moderation (Image)
- Artificial Intelligence/Text Moderation renamed to Moderation (Text)
- Business Applications/Mail renamed to Enterprise Mail
- Business Applications/HaydnCSF renamed to InnoStage Workbench (HaydnCSF)
- Line/Other library renamed to Misc and incorporated icons from Content Delivery, Edge Computing and Video

### Fixed

- Groups: Huawei Cloud, Region, VPC and Subnet elements are now ungrouped, so
  icons placed inside them will not move when you resize the bounding rectangle
- Security and Compliance/Key Management Service (KMS) icon name

### Removed

- Huawei Cloud group with Huawei icon (due to not being legible)
- Artificial Intelligence: Custom OCR, DataArts Insight (Modern BI), HeatingGo, WaterGo
- Storage/Dedicated Enterprise Storage Service (DESS)
- Security and Compliance/Vulnerability Scan Service (VSS)
- Developer Services: Classroom, DevSecurity, Flow, Astro Zero
- Security and Compliance/Huawei IT Service (HIS)
- Compute: Hyper-Elastic Cloud Server (HECS), HECS Light (replaced by Flexus)

## [v3.1] - 2024-11-16

- Added CCE Group
- Added MgC Edge icon
- Added IAM Identity Center (IIC) icon
- Fixed Migration Center (MgC) icon (now with round corners)
- Changed Kaitian to MacroVerse
- Small updates

## [v3.0] - 2024-03-08

- Added Color icons
- Added Groups library
- Removed "Extended" library with one icon (moved to "Application" category)

## [v2.0] - 2023-08-22

- Icons resized to 40x40, to fit default draw.io grid size
- Added more icons, including Extended Service icons
- Libraries are now generated in an automated way

## [v1.1] - 2022-11-24

Fixed configuration lines instructions

## [v1.0] - 2022-10-13

Initial version
