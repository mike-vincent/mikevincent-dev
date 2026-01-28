---
title: "Building mikevincent.dev"
subtitle: "Architecture and design decisions"
date: 2026-01-27
tags: ["astro", "design", "webdev"]
image: "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800&h=400&fit=crop"
---

I rebuilt my personal site from scratch. Here's how it's put together.

**Stack**: Astro for static site generation. Markdown files with YAML frontmatter for blog posts. Plain CSS for styling. Deploys to GitHub Pages.

**Layout**: Mobile-first responsive design with two breakpoints at 500px and 1000px. The grid uses flexbox with a centered column that maxes out at 980px.

**Header**: Sticky positioning with a hide-on-scroll-down, show-on-scroll-up behavior. Glass effect using backdrop-filter blur. The scroll detection includes a 30px threshold to prevent flickering at page bottom.

**Typography**: SF Pro Text system font stack. Body text at 16px with 1.4 line-height. Titles at 20px. Muted secondary text using rgba for theme-aware opacity.

**Theming**: Dark and light modes with CSS custom properties. Theme state persists to localStorage. The toggle sits in the header with a sun/moon icon.

**Post cards**: Avatar aligned to title top using flex-start. Thumbnail images on mobile show full-width with text overlay. On tablet and up, thumbnails shift to a square format on the right side.

**View Transitions**: Astro's built-in view transitions API for smooth page navigation. Title elements have transition names for morphing effects between list and detail views.

**Dev.to Integration**: Posts are fetched from the dev.to API at build time. The list endpoint provides titles and descriptions but not full bodies, so those posts link externally.

**Performance**: Lazy loading for the post list shows 10 items initially with a "Show more" button. Next 5 posts are prefetched. Images use native lazy loading.

Source code is on GitHub.
