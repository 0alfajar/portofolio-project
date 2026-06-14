# Collection Methodology

## Tools Used

### YouTube Transcripts
- **Tool:** `youtube-transcript-api` v1.2.4 (Python)
- **Method:** Calls YouTube's internal (undocumented) transcript API — same one YouTube's web client uses
- **API Key:** None required
- **Rate limiting:** 1.5 seconds between requests
- **Success rate:** 37/37 videos (100%)
- **Output formats:** JSON (timestamped segments) + Markdown (readable full text)

### LinkedIn Posts
- **Method:** Google search with `site:linkedin.com/posts [expert name]` queries
- **Limitation:** LinkedIn blocks direct scraping; content reconstructed from search snippets
- **Posts collected:** 49 posts across 10 experts
- **Output:** Markdown files organized by expert

### Blog Articles & Other Materials
- **Method:** Web search + extraction from expert websites
- **Sources:** vireovideo.com, swayone.io, microconf.com, tkkader.com
- **Output:** Markdown summaries with key takeaways

## Data Volume Summary
| Content Type | Items | Total Characters |
|-------------|-------|-----------------|
| YouTube transcripts | 37 videos | ~750K+ chars |
| LinkedIn posts | 49 posts | ~25K chars |
| Blog articles/frameworks | 4 docs | ~8K chars |
| **Total** | **90 items** | **~861K+ chars** |

## Limitations
1. LinkedIn content is summaries from search snippets, not full post text (LinkedIn blocks extraction)
2. Blog articles are summarized, not full-text (some extraction backends unavailable)
3. Transcript quality varies — auto-generated captions may have errors
4. Some experts are more YouTube-active than LinkedIn-active, so their LinkedIn files contain adjacent SaaS/community/content posts rather than YouTube-specific posts


## Reproducibility

The transcript collection script is included at `research/other/transcript_collection_script.py`. A video/source inventory is included at `research/other/video_inventory.csv`.
