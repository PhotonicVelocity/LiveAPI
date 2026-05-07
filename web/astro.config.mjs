// @ts-check
import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";

// https://astro.build/config
export default defineConfig({
  site: "https://photonicvelocity.github.io",
  base: "/LiveAPI",
  integrations: [
    starlight({
      title: "LiveAPI",
      description:
        "Reference for the Ableton Live Object Model (LOM) — types, behavior, and quirks.",
      social: [
        {
          icon: "github",
          label: "GitHub",
          href: "https://github.com/PhotonicVelocity/LiveAPI",
        },
      ],
      sidebar: [
        // Root index.mdx (splash hero page) is reachable via the site
        // title at the top of the sidebar; no separate "Overview" entry
        // needed.
        {
          label: "Modules",
          autogenerate: { directory: "modules" },
          collapsed: false,
        },
      ],
      // Right-side TOC down to member level (H3) — Sphinx/Blender style.
      // Members and sections both show up; the page content is its own
      // navigation surface.
      tableOfContents: { minHeadingLevel: 2, maxHeadingLevel: 3 },
      customCss: ["./src/styles/custom.css"],
    }),
  ],
});
