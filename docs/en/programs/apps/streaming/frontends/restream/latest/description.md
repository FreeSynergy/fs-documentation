# Restream - Description

## Overview

Restream is a commercial multistreaming service: it accepts one stream and distributes it
to many platforms at the same time. It also offers a browser studio, a unified chat, event
planning and analytics — without your own infrastructure.

## What Restream does

An encoder (OBS, ffmpeg) or the Restream Studio sends one stream to the ingest address
named in the dashboard. Restream copies that stream to all connected targets, bundles the
platforms' chats, records and measures viewer numbers. The service scales the distribution
itself.

## Advantages

- **ready immediately**: no servers, no TLS certificates, no ports
- **platform coupling by login** instead of juggling stream keys
- **studio in the browser** — production without local encoder hardware
- **chat from one place** across all platforms
- **analytics included** instead of built by yourself

## Differentiation from other systems

### Restream vs. the Docker Restreamer

- the Restreamer is **self-hosted** (nginx-rtmp + web UI) and distributes to your own targets
- Restream is SaaS: more comfort, but data sovereignty and configuration access fall away
- cost model: subscription plans instead of infrastructure costs

### Restream vs. Wowza / Ant Media Server

- Wowza and AMS are **server software** (a platform to operate yourself, incl. transcoding and API)
- Restream offers no transcoding setup and no server access, in exchange for immediate platform connection
- Anyone needing white label or their own infrastructure chooses Wowza/AMS/MediaMTX

### Restream vs. direct platform ingests

- instead of separate upstream keys per platform, only **one** ingest
- in exchange, dependence on a third party and its availability
- platform features (e.g. Superchats) stay with the target platform

## Technical details

- **Backend**: the provider's closed SaaS infrastructure
- **Database**: not inspectable; account data, targets and events live in the account
- **Frontend**: web dashboard and studio (browser), embeddable player
- **Authentication**: account login (e-mail/password, 2FA); APIs with an OAuth access token
- **Hosting**: only at the provider — self-operation is not possible

## Who Restream suits

- creators and small teams who want to send to many platforms at the same time without infrastructure effort
- events with browser production and guest invitations
- Less suitable for: privacy-driven setups, white-label products, protocol/port control, or very long streaming times (plan limits)
