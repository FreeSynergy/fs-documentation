# FreeSynergy Simple 0.1 — Description

## Overview
A messenger for people who just want to read and answer their messages. No folders, no ribbons:
one message fills the screen, gestures do the rest. Works on touch devices first; every gesture has
an equivalent for mouse, keyboard and assistive technology (see [interaction](interaction.md)).

## What it does
- shows each new message full screen, unread first
- moves between unread messages, forwards, deletes, replies — by gesture
- writes replies and new messages in a plain text composer (simple editor, ADR 0039)
- picks recipients from contacts or creates a new contact on the fly
- always shows whether a message is encrypted; unencrypted ones are marked with a link to the guide (ADR 0018)

## Who it suits
People who are overwhelmed by mail programs; quick checking on the phone; a demo that a frontend can
be small.

## Differentiation
- vs. [FreeSynergy full](../../index.md) (reference frontend no. 2, planned): no folders, rules, search filters, multi-select
- vs. Outlook / Apple Mail: no list as the start screen; the message is the start screen
