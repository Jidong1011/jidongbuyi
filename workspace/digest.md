AI Builders Digest — 2026-06-17

## X / TWITTER

### Swyx (aiDotEngineer)
He highlighted the key split in AI engineering today between fast, experimental "slop cannon" workflows and more rigorous engineering approaches, sharing links to his recent talks on harness engineering and the importance of slowing down to build more reliable systems.
https://x.com/swyx/status/2044939001405350235

### Kevin Weil (VP Science @OpenAI)
Announced GPT-Rosalind, OpenAI's first frontier model purpose-built for scientific research across biology, drug discovery, and translational medicine, available via trusted access for qualified customers. He also noted that the new Codex computer use capabilities are "shockingly good".
https://x.com/kevinweil/status/2044862783947448611
https://x.com/kevinweil/status/2045004924682195027

### Peter Yang (Product @Roblox)
Shared his agent workflow where he uses a separate eval agent to run yes/no checks on the first agent's output, looping to fix issues until all checks pass. He also noted that he wants Claude and Codex apps to add easier native markdown editing capabilities for fine-tuning instructions.
https://x.com/petergyang/status/2044998456062906422
https://x.com/petergyang/status/2045007422084051168

### Cat Wu (Claude Code + cowork @AnthropicAI)
Announced that Opus 4.7 with xhigh effort level is now the default for Claude Code, and shared tips for better results: add verification workflows to your claude.md file, as Opus 4.7 is much better at validating its own work. She also noted Anthropic is centralizing all their product updates in a single "What's New" section in their docs.
https://x.com/_catwu/status/2044808539663978970
https://x.com/_catwu/status/2044815645699928273

### Thariq (Claude Code @AnthropicAI)
Shared that Anthropic is adding a curated "What's New" digest section to their docs, running monthly "what we shipped" webinars for users, and updating the /usage command in Claude Code to give users better visibility into their consumption and costs.
https://x.com/trq212/status/2044893584961556767
https://x.com/trq212/status/2044893586333032627

### Amjad Masad (CEO @Replit)
Announced Replit deployments to the EU are now available, and they're running a 50% off promotion for their platform, especially useful for running parallel agents to accelerate project work.
https://x.com/amasad/status/2044844802077069375
https://x.com/amasad/status/2044846551072419994

### Guillermo Rauch (CEO @Vercel)
Launched Workflow SDK, a new backend framework for building reliable agent and LLM applications that handles retries, rate limits, and durability out of the box, with first-class multi-cloud and self-hosting support. He noted it solves the common pain point of unreliable LLM and third-party service calls that often cause agent failures.
https://x.com/rauchg/status/2044858872842826102

### Alex Albert (Research @AnthropicAI)
Highlighted his favorite new features in Opus 4.7: better async task following, more predictable effort levels for token control, no more downscaling of high-res images, and noticeably better taste in UI, slide, and document generation.
https://x.com/alexalbert__/status/2044788914813292583

### Aaron Levie (CEO @Box)
Shared that the new Codex computer use capabilities are a major leap for knowledge worker agents, allowing them to execute long-running background tasks across multiple apps, with the Box plugin enabling automation of almost any enterprise content workflow.
https://x.com/levie/status/2044855448722100720

### Ryo Lu (Design @Cursor_ai)
Shared his model workflow: Opus 4.7 for planning, Composer 2 for building and iterations, and Codex/GPT-5.4 for hard bugs, all within Cursor. He also announced he's working on "Baby Glass", a new prototyping environment at Cursor that lets designers quickly test ideas in code using shared components from the Cursor 3 interface.
https://x.com/ryolu_/status/2044789186130256062
https://x.com/ryolu_/status/2044982132859400342

### Garry Tan (CEO @YCombinator)
Announced updates to his GBrain tool, including security fixes, better end-to-end Gemini Live tests for GBrain Voice, and improvements to the /ship skill for more robust deployments.
https://x.com/garrytan/status/2045002844508766510
https://x.com/garrytan/status/2045020411805700110

### Zara Zhang (Builder)
Shared her philosophy that the best uses of her time are deep conversations, deep reading, and deep experimentation with AI. She also turned her popular frontend slides repo into a video, and noted that "HTML is eating everything" with the rise of HTML videos as a native web capability.
https://x.com/zarazhangrui/status/2044891980178792560
https://x.com/zarazhangrui/status/2044849748579164328

### Peter Steinberger (OpenClaw)
Noted that OpenClaw's public security disclosures are an early indicator of broader security risks coming from the wider AI agent ecosystem, rather than a sign of OpenClaw being particularly insecure. He also shared updates from ClawCon Michigan which had almost 2000 attendees.
https://x.com/steipete/status/2044888081141223442
https://x.com/steipete/status/2044935917417205796

### Dan Shipper (CEO @Every)
Shared he ran a "philosopher draft" asking which historical philosopher each AI lab would hire, and noted that the recent Mythos announcement may have been a strategic move to ensure the Trump administration keeps existing contracts with Anthropic.
https://x.com/danshipper/status/2044890935637549380
https://x.com/danshipper/status/2044864110391710144

### Aditya Agarwal (General Partner @SouthPkCommons)
Lighthearted take asking if he now has to rewrite all his code with the new Opus 4.7 capabilities.
https://x.com/adityaag/status/2044861137720918371

### Sam Altman (CEO @OpenAI)
Announced major updates to Codex, including full computer use capabilities that let it run Mac apps in parallel without interrupting user work, in-app browsing, and the ability to learn from experience to proactively suggest tasks for users.
https://x.com/sama/status/2044858862042591378
https://x.com/sama/status/2044858863246323811

### Claude (AI assistant @AnthropicAI)
Announced Claude Opus 4.7 is now available, with new features including an xhigh effort level for finer control over reasoning vs latency, task budgets for cost management across long runs, and the new /ultrareview command in Claude Code that runs dedicated code reviews. Auto mode is now extended to Max users for longer uninterrupted tasks.
https://x.com/claudeai/status/2044785264313221470
https://x.com/claudeai/status/2044785266590622185
https://x.com/claudeai/status/2044785272617939282

## OFFICIAL BLOGS

### Anthropic Engineering: Scaling Managed Agents: Decoupling the brain from the hands
Anthropic shared their architecture for Claude Managed Agents, which decouples agent components (session log, harness, execution sandbox) into independent interfaces to keep up with evolving model capabilities. The design solves the problem of stale infrastructure assumptions that go out of date as models improve, similar to how operating systems abstracted hardware decades ago.
Decoupling the harness (the "brain") from sandboxes (the "hands") cut p50 time-to-first-token by 60% and p95 by over 90%, as containers are only provisioned when needed rather than for every session. The architecture also improves security by ensuring credentials never reach the sandbox where Claude's generated code runs, using token proxies and repository-specific auth.
"Managed Agents is a meta-harness, unopinionated about the specific harness that Claude will need in the future. Rather, it is a system with general interfaces that allow many different harnesses."
https://www.anthropic.com/engineering/managed-agents

### Claude Blog: Claude Managed Agents: get to production 10x faster
Anthropic launched Claude Managed Agents, a suite of composable APIs for building and deploying cloud-hosted agents at scale, now in public beta. The platform handles infrastructure concerns like secure sandboxing, state management, permissioning, and error recovery, letting teams go from prototype to production in days rather than months.
In internal testing, Managed Agents improved task success rates by up to 10 points over standard prompting loops, especially on harder problems. Notable customers already using the platform include Notion (for Custom Agents), Rakuten (enterprise agents across departments), Asana (AI Teammates), and Sentry (debugging agent that writes and opens PRs for bugs).
"Whether you're building single-task runners or complex multi-agent pipelines, you can focus on the user experience, not the operational overhead."
https://claude.com/blog/claude-managed-agents

## PODCASTS

### Latent Space: Notion’s Token Town: 5 Rebuilds, 100+ Tools, MCP vs CLIs and the Software Factory Future — Simon Last & Sarah Sachs of Notion
**The Takeaway**: Notion's AI team built their custom agent platform by prioritizing flexible, tool-agnostic abstractions and distributed ownership to keep up with rapidly evolving model capabilities, avoiding the pitfalls of tightly coupled infrastructure and centralized prompt management.
Simon Last (Notion AI engineering lead) and Sarah Sachs (Notion AI product lead) shared their lessons learned from rebuilding Notion's agent platform five times over the past two years. They found that early assumptions about model capabilities often went stale, leading them to decouple their agent harness (the "brain") from execution sandboxes (the "hands") and session logs, allowing components to be swapped independently without breaking existing workflows.
They moved away from centralized prompt management where only a small team could edit few-shot prompts, enabling any team to own their tool definitions while maintaining quality guardrails. This shift cut time-to-first-token by 60% (p50) and over 90% (p95), and allowed them to roll out custom agents with over 100 tools for Notion users.
Their key philosophy: "Our job isn't to build the best wearable to capture meeting notes. Our job is to build the best place where meeting notes live."
https://www.youtube.com/@LatentSpacePod

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders