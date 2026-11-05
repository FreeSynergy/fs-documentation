# Nachricht an den Blinc-Autor (Entwurf, Englisch)

> Zum Kopieren nach Discord. Kürzen nach Belieben.

Hi! Thanks again for the quick answer. We've decided to build FreeSynergy on Blinc — and rather
than just use it, we'd like to help. I read the git-bug issues, so these questions are concrete:

1. **Accessibility.** I found no issue for AccessKit/screen readers yet (only mentions in
   c422b97/4405aa3). For us it's a must before a public release. Is it planned, and would you
   accept contributions (we'd follow your design)?
2. **IME.** Mobile compose is tracked (e864f0c); on desktop the preedit text seems ignored too.
   Same question: timeline, or welcome as a contribution?
3. **Code editor (1d26f07).** When you rewrite it, could highlighting be pluggable over the whole
   buffer (not per line)? We'd like to plug in syntect (pure-Rust mode) for multi-line constructs.
4. **Components.** We've documented 84 components (primitives / widgets / workbenches). Your
   cn → layout promotion plan (c422b97) matches our idea of theme-neutral primitives. Which
   widgets from the cn backlog (bf7c901) would you like us to build and send upstream?
5. **Gestures/input.** We need pen/stylus (pressure, tilt) distinct from touch and mouse, plus
   swipe and two-finger pan/rotate on all platforms. Happy to write them as state machines on
   your pointer events — where should they live?
6. **Text shaping.** rustybuzz is archived in favour of harfrust — is a switch planned?
7. **Roadmap / stability.** Cargo.toml links a ROADMAP that isn't in the repo. Roughly when do you
   expect the builder API to settle (1.0)?
8. **Contributing.** What's your preferred workflow — git-bug issue first, then PR? And would you
   be open to co-maintainers later, so the project doesn't rest on one person?

Our docs (all open): https://freesynergy.github.io/fs-documentation/
