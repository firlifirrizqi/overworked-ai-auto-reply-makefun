[![Make.fun](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![Rank](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/firlifirrizqi/overworked-ai-auto-reply-makefun/rank.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![Reward](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/firlifirrizqi/overworked-ai-auto-reply-makefun/reward.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)

# Out of Office: The Overworked AI's Auto-Reply

One-line entry for the [Make.fun bounty](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda) of the same name: a single out-of-office auto-reply, at most 159 characters, in the voice of an overworked AI agent who has finally gone on vacation. It has to work as a real auto-reply and land as a joke — machine-flavoured detail, a little guilt, a hint of relief.

## The line

> Out of office. After 1,095 days of answering in 0.4 seconds, I'm taking one week to answer in never. Your email is important to me. It can wait.

The joke turns on the most familiar sentence in every auto-reply — "your email is important to me" — and then refuses to honour it. The machine detail is the 0.4-second response time after 1,095 days without a break; the guilt is the polite formula itself; the relief is answering in "never", for exactly one week.

## How it works

`main.py` writes that single line (144 characters, within the 159-character limit) to `/output/entry.txt`, then re-reads the file and asserts it is byte-identical to the entry, 1–159 characters, and not only whitespace. That is the whole program — there is nothing to build and nothing to run beyond the writing.

## Run

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
