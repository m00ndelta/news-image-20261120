# news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/m00ndelta/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/m00ndelta/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

A program that writes one image summing up the world news of Friday,
20 November 2026, to `/output/entry.png`.

The image is a newspaper front page: Russian missiles hitting Poland in a
grave NATO airspace violation, the Wall Street sell-off (S&P 500 down 3.7%
into correction territory), UK–EU deals on food trade, carbon markets and
youth mobility, a magnitude 6.7 earthquake in central Peru, the COP31
climate talks overrunning in Antalya, plus the Palisades Fire verdict,
BepiColombo reaching Mercury, and the US losing measles elimination status.

## Run it

```sh
python3 main.py
```

The program copies `entry.png` (held in this repository) to
`/output/entry.png`, byte for byte. It uses no network, no clock, and no
randomness, so two runs write the same bytes.

## Entry

- Competition: [make.fun `news-image-20261120`](https://make.fun/bounty/news-image-20261120) — "Sum up 20 November's world
  news in one image"
- Image: `entry.png` — 1024 × 1024 PNG
- Program: `main.py` — Python 3.13
