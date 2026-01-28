---
title: "Building mikevincent.dev"
subtitle: "A personal site built with Claude Code in one session"
date: 2026-01-27
tags: ["astro", "claude", "webdev"]
image: "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800&h=400&fit=crop"
---

I rebuilt my personal site today using Claude Code. Started from scratch with Astro and ended up with something I'm happy with.

The setup is simple: Astro for static site generation, markdown files for blog posts, and CSS for styling. No frameworks, no build complexity.

Key features that came together:

- Sticky header that hides on scroll, reappears when you scroll up
- View transitions for smooth page navigation
- Dev.to integration that pulls in my Python articles
- Lazy loading with "Show more" for the post list
- Dark/light theme toggle
- Responsive layout with two breakpoints (500px, 1000px)

The dev.to integration was interesting. The list API gives titles and descriptions but not full article bodies. So external posts link directly to dev.to while local posts render here.

Everything lives in a single CSS file. No Tailwind, no CSS-in-JS. Just classes and media queries.

The whole thing took one afternoon. Claude Code handled the iteration loop: I'd describe what I wanted, see the result, adjust. Repeat until it looked right.

Source code is on GitHub. The site deploys to GitHub Pages.
