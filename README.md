# YouTube Content Strategy for B2B SaaS Research Project

## Overview

This repository contains a research project on YouTube content strategy for B2B SaaS companies. The goal is to collect strong source material from real practitioners, organize it cleanly, and create a foundation for a future tactical playbook.

Chosen topic: **YouTube content strategy for B2B SaaS**

## Research question

How should a B2B SaaS company use YouTube to build trust, generate qualified demand, and support pipeline without relying on vanity metrics like total views or subscriber count?

## Why this topic matters

YouTube is still underused in B2B SaaS compared with blogs, LinkedIn, webinars, and newsletters. However, several SaaS founders and B2B video specialists show that YouTube can work as a long-term search, trust, and conversion channel.

Key reasons this topic is worth studying:

- YouTube content compounds over time.
- Videos can rank in both YouTube and Google search.
- Founder-led video builds trust faster than anonymous brand content.
- Small channels can still generate revenue if the audience has high buying intent.
- B2B SaaS teams can repurpose YouTube content into sales enablement, LinkedIn posts, newsletters, and blog content.

## Repository structure

```text
research/
├── sources.md
├── insights.md
├── linkedin-posts/
├── youtube-transcripts/
└── other/
```

### Directory purpose

| Path | Purpose |
|---|---|
| `research/sources.md` | List of all selected experts, links, reasons for inclusion, and key source material |
| `research/insights.md` | Early synthesis of patterns found in the research |
| `research/linkedin-posts/` | LinkedIn posts organized by author |
| `research/youtube-transcripts/` | YouTube transcripts organized by expert and video |
| `research/other/` | Supplementary materials, methodology, transcript script, and inventory CSV |

## Why I chose these experts

I chose these experts because they represent the main ways B2B SaaS companies can use YouTube: specialist YouTube agencies, SaaS founders who use YouTube as a growth channel, founder-led content operators, B2B SaaS community builders, and interview/data-led content operators. This gives the research enough range to support a practical playbook later, instead of only collecting generic marketing opinions.

Experts were selected based on four criteria:

1. They are practitioners, not only commentators.
2. They have direct experience with SaaS, B2B marketing, YouTube, video strategy, or founder-led content.
3. Their content is strong enough to support a practical future playbook.
4. The group includes different angles: agencies, SaaS founders, community builders, interview operators, and bootstrapped SaaS educators.

## Selected experts

| Expert | Category | Reason selected |
|---|---|---|
| Marlon Doll | YouTube strategy specialist | Founder of Vireo Video, focused on YouTube strategy for brands and SaaS |
| Josef Newton / Sway One | B2B video strategy specialist | Works directly on B2B SaaS video and YouTube strategy |
| Vasco Aires | SaaS founder using YouTube | Strong case study of SaaS revenue driven through YouTube content |
| Dan Martell | SaaS founder and creator | Large SaaS-focused YouTube audience and founder-led content system |
| TK Kader | B2B SaaS GTM educator | Uses long-form YouTube content to teach SaaS GTM and content strategy |
| Rob Walling | Bootstrapped SaaS authority | Long-form SaaS education and buyer-awareness content frameworks |
| Jason Lemkin | B2B SaaS community builder | Uses SaaStr video content to build category authority and community |
| Nathan Latka | SaaS interview and data operator | Uses founder interviews and SaaS metrics as a content engine |
| Joran Hofman | B2B SaaS founder and podcast host | Runs Grow Your B2B SaaS and documents SaaS growth topics |
| Arvid Kahl | Bootstrapped founder and audience builder | Strong source for founder-led content, audience building, and indie SaaS thinking |

## What I collected

I collected expert source profiles, YouTube transcripts, LinkedIn post summaries, supplementary articles/frameworks, a source inventory, and early synthesis notes. The goal was to gather enough material to later build a real B2B SaaS YouTube playbook.

| Material type | Count | Notes |
|---|---:|---|
| Experts | 10 | Mixed intentionally across YouTube specialists, SaaS founders, and B2B content operators |
| YouTube transcripts | 37 videos | Collected programmatically with `youtube-transcript-api` |
| LinkedIn posts | 49 posts | Organized by author in Markdown files |
| Supplementary documents | 5 files | Articles, frameworks, and methodology notes |
| Inventory file | 1 CSV | Tracks video/source type and transcript status |
| Synthesis document | 1 file | Early insights for future playbook development |

## Technical collection method

YouTube transcripts were collected programmatically using Python and `youtube-transcript-api`.

Each collected YouTube video has two files:

- `.json` file with timestamped transcript segments
- `.md` file with a readable full transcript

The script used for collection is included here:

```text
research/other/transcript_collection_script.py
```

The video/source inventory is included here:

```text
research/other/video_inventory.csv
```

## Important note about Josef Newton / Sway One

The Josef Newton section includes four source materials, but only one is a direct YouTube video with a transcript:

```text
NFAg8OM4C84
```

The other Josef/Sway One materials are a podcast, a LinkedIn post, and an article. They are included as supplementary research, not as transcript files. This is also documented in `research/other/video_inventory.csv`.

## Early research themes

The main patterns found so far:

1. B2B SaaS YouTube should optimize for qualified intent, not broad views.
2. Founder-led content builds trust faster than generic brand content.
3. YouTube can function as B2B search infrastructure, similar to SEO.
4. Content should map to buyer awareness stages.
5. Small channels can still produce meaningful SaaS pipeline if topics target high-intent buyers.
6. Interview-led and data-led formats can create authority for companies that do not want founder monologues.

More detail is available in:

```text
research/insights.md
```

## Future playbook potential

This research can support a future playbook covering:

1. How to choose a YouTube positioning angle for B2B SaaS
2. How to map topics to funnel stage and buyer awareness
3. Which video formats fit early-stage versus growth-stage SaaS
4. How to use founder-led content without becoming generic
5. How to connect YouTube views to demos, trials, and pipeline
6. How to repurpose YouTube videos into LinkedIn, blogs, newsletters, and sales assets
7. How to measure success beyond subscriber count
