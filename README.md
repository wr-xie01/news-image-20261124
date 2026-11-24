# The World in One Day — 24 November 2026

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/wr-xie01/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/wr-xie01/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

A newspaper front page that sums up Tuesday 24 November 2026 in a
single 1024×1024 image. Every story on the page happened or was first
reported on 24 November 2026.

## The six stories

1. **GENEVA — Chess crown on the line.** Game 1 of the FIDE World
   Championship begins: defending champion Gukesh Dommaraju of India
   faces challenger Javokhir Sindarov of Uzbekistan over 14 games for
   the $2.5m world title.
2. **SEOUL — Russian jets spark island alert.** Several Russian military
   aircraft enter South Korea's air defence zone near Ulleung Island;
   jets scramble, residents take shelter, and Seoul summons Moscow's
   defence attaché. No airspace violation.
3. **KUALA LUMPUR — 6,803 more migrants to go home.** Malaysia will
   send 6,803 Myanmar nationals home in December, PM Anwar Ibrahim
   tells parliament — 1,500 by navy ships on 6–7 December, 5,303 by
   air — after the ICJ's genocide ruling.
4. **PYONGYANG — North Korea threatens Swiss office.** Kim Yo Jong says
   Pyongyang may shut Switzerland's new diplomatic office after Bern
   sanctioned a children's camp over the transfer of Ukrainian children.
5. **CANBERRA — Singapore vows: no chip back door.** PM Lawrence Wong,
   with Australia's Anthony Albanese, says Singapore is working with
   the US to stop firms rerouting American AI chips through Singapore.
6. **VILLAVICENCIO — Car bomb hits governor's office.** A blast outside
   the Meta department government building in Colombia wounds at least
   five; the president blames "narcoterrorism". No group claims it.

## How it is built

`generate_image.py` draws the front page with PIL (masthead, date band,
six story cards with simple icons, footer) and writes `entry.png`.
`main.py` copies `entry.png` to `$MAKEFUN_OUTPUT_DIR` (default
`/output`), checking the 1 MiB size limit and the 1024×1024 limit first.
Both runs write the same bytes.

Run it:

```sh
python3 generate_image.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
