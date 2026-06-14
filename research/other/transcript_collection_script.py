"""Collect YouTube transcripts for B2B SaaS YouTube strategy research.

Tool used: youtube-transcript-api
Install: pip install youtube-transcript-api

Output:
- JSON: timestamped transcript segments
- Markdown: readable full transcript

Note: This script is included to document the API/tooling process used for collection.
"""

from youtube_transcript_api import YouTubeTranscriptApi
import json
import os
import time

api = YouTubeTranscriptApi()
BASE_DIR = os.path.join("research", "youtube-transcripts")

VIDEOS = {
    "marlon-doll": {
        "OBK5DZJZnjs": "Your SaaS Channel Needs This YouTube Strategy",
        "EotgIYmE2oY": "This System Turns YouTube Into A 24-7 Sales Machine",
        "gAjmXdjppLk": "Fixing a Major Brands YT Channel On The Spot - Square Audit",
        "F_h6a8fGTLY": "How to Get Your YouTube Videos Recommended by AI",
        "Qhg09bbhN5w": "CEO Ranks Every YouTube Growth Strategy for Educational Channels",
    },
    "dan-martell": {
        "44CfRbavZYQ": "How to start a SaaS business",
        "5F_lUwNYdAI": "How Dan Martell Scaled 100M SaaS Companies",
        "sBZmzlJu8oM": "Dan Martell Reveals the SECRET To Running A SaaS Company",
    },
    "tk-kader": {
        "HQZMyxBvz_0": "Best SaaS Marketing Playbook to Hit 10M ARR in 2026",
        "RO2ifYXL5d0": "Best SaaS Marketing Strategies For 2026",
        "SVA1BWly8eo": "B2B Marketing Strategy - How To Get More Leads With Ideal Customer",
        "fge6vPNz2Kc": "Content Marketing for B2B That Works",
        "YxAd96vLzCc": "If I Started in 2026 Heres My B2B SaaS Content Strategy",
    },
    "rob-walling": {
        "mGu-2suChAg": "The Future of SaaS - 2025 Trends You NEED to Know",
        "GNR61V6ihxE": "Ill Help You Build a Million Dollar SaaS Business",
        "mYMeLw3HinQ": "SaaS Predictions for 2026 - Reflections on 2025",
        "S-qDGDqkSHI": "9 Startup Predictions for 2025",
    },
    "vasco-aires": {
        "wPLME69m8Zs": "Copy My 1000000 SaaS Strategy or stay broke",
        "hgonN8ZywPk": "How my SaaS made 62400 in 20 Days",
        "O59vIfG1cTs": "This will 3X my SaaS Revenue - strategy revealed",
        "CIhXoNV-dPY": "my SaaS made 1.7K in 1 day - marketing strategy revealed",
    },
    "arvid-kahl": {
        "2YsCcJg3QkE": "Marketing for Founders Who Hate Marketing",
        "5xt6S5mes-I": "Vibe Coding Wont Kill SaaS",
        "X96ufYBx-r4": "Making Your Business Sellable Even If You Never Plan To",
        "EHJQy6vY30A": "AI is a Threat to SaaS Multiples",
    },
    "jason-lemkin": {
        "4CjJnhmPy3o": "The 2025 SaaS Vibe Check - What Founders Need to Know Right Now",
        "iAI-htMWvBw": "The Best SaaS Marketing Strategy for 2026",
        "CvS3tJFmunY": "2025 State of SaaS - Trends and Predictions",
        "f0L_l4pc4rU": "What Really Matters in SaaS in 2025",
    },
    "nathan-latka": {
        "6E79GMfbEBo": "He Built a BORING SaaS That Makes Him 9M yr",
        "U2RAjHVdHZM": "4M yr SaaS Founder - How To Add 100000 in ARR Every Month",
        "ApZVuqfX7BQ": "How He Built a 14M Yr SaaS in a Boring Niche",
    },
    "joran-hofman": {
        "XQZl9nOOjDc": "How to grow your B2B SaaS to 10K MRR - Advice from 20 experts",
        "EXAdYGVRaC8": "How to grow your B2B SaaS to 10M ARR - Advice from 20 experts",
        "wi7gtMUSqto": "Affiliate Marketing for B2B SaaS companies",
        "-Yq_YOHUuKY": "How to grow your B2B SaaS to 10M ARR - Season 4",
    },
    "josef-newton-sway-one": {
        "NFAg8OM4C84": "Leveraging In-House On Camera Content for B2B Companies",
    },
}

for expert_slug, videos in VIDEOS.items():
    expert_dir = os.path.join(BASE_DIR, expert_slug)
    os.makedirs(expert_dir, exist_ok=True)

    for video_id, title in videos.items():
        transcript = api.fetch(video_id, languages=["en"])
        segments = [
            {"start": round(s.start, 1), "duration": round(s.duration, 1), "text": s.text}
            for s in transcript
        ]

        with open(os.path.join(expert_dir, f"{video_id}.json"), "w", encoding="utf-8") as f:
            json.dump({"video_id": video_id, "title": title, "segments": segments}, f, ensure_ascii=False, indent=2)

        full_text = " ".join(segment["text"] for segment in segments)
        with open(os.path.join(expert_dir, f"{video_id}.md"), "w", encoding="utf-8") as f:
            f.write(f"# {title}\n\n")
            f.write(f"**Video ID:** {video_id}\n")
            f.write(f"**URL:** https://www.youtube.com/watch?v={video_id}\n")
            f.write(f"**Segments:** {len(segments)}\n\n")
            f.write("---\n\n## Full Transcript\n\n")
            f.write(full_text)

        print(f"Collected {video_id}: {len(segments)} segments")
        time.sleep(1.5)
