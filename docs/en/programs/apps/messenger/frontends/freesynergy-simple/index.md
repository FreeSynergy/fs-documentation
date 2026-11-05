# FreeSynergy Simple

> Category: [messenger](../../index.md) · Type: our own reference frontend no. 1 "very, very simple" (ADR 0038) · Licence: MIT OR Apache-2.0

## What it is

Our own, deliberately minimal messenger frontend. Every incoming message is shown **full screen**;
everything is done with a few gestures. It shows that a frontend on the `fs-messenger` contract does
not have to be complicated. Design by the project owner (2026-11-05).

## Notable ideas

- One message at a time, full screen — no inbox to manage.
- The whole workflow is gestures: next, forward, delete, reply, send, cancel.
- Choosing recipients is one search field: what you type filters your contacts; if nobody matches,
  a "new contact" form opens with the fields needed to reach that person.

## Protocols and standards used

None directly — it speaks only the `fs-messenger` contract (Cap'n Proto, ADR 0021). Mail, Matrix,
MIMI, Telegram etc. are behind the program's connectors (ADR 0018).

## Sources

Design given by the project owner in the conversation of 2026-11-05.
