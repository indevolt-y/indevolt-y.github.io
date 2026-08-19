import { themes as prismThemes } from "prism-react-renderer";
import type { Config } from "@docusaurus/types";
import type * as Preset from "@docusaurus/preset-classic";
import stripDocumentImages from "./plugins/strip-document-images";

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const isChineseLocale =
  process.env.DOCUSAURUS_CURRENT_LOCALE === "zh";

const developerCenterLink = {
  label: "Developer Center",
  to: "docs/developer",
};

const documentVersionLink = {
  label: "Doc Version",
  to: "docs/doc-version",
};

const config: Config = {
  title: "INDEVOLT Developer Docs",
  tagline:
    "Explore comprehensive documentation for INDEVOLT, including guides, tutorials, and API references.",
  favicon: "img/favicon.ico",
  headTags: [
    {
      tagName: "link",
      attributes: {
        rel: "llms-txt",
        href: "https://indevolt-y.github.io/llms.txt",
        type: "text/plain",
      },
    },
  ],

  // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
  future: {
    v4: true, // Improve compatibility with the upcoming Docusaurus v4
    experimental_faster: true,
  },

  // Set the production url of your site here
  url: "https://indevolt-y.github.io",
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: "/",

  markdown: {
    format: "mdx",
    mermaid: true,
  },

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: "indevolt-y",
  projectName: "indevolt-y.github.io",

  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "warn",
  plugins: [
    ["./plugins/tailwind-plugin.cjs", {}],
    [
      "@docusaurus/plugin-client-redirects",
      {
        createRedirects(existingPath: string) {
          const docVersionPath = "/docs/doc-version";
          const localDevicePanelPath =
            "/docs/developer/guides/opendata-local-device-panel";

          if (existingPath.endsWith(docVersionPath)) {
            return existingPath.replace(
              docVersionPath,
              "/docs/hardware/doc-version",
            );
          }

          if (existingPath.endsWith(localDevicePanelPath)) {
            return existingPath.replace(
              localDevicePanelPath,
              "/docs/developer/guides/macos-local-app",
            );
          }

          return undefined;
        },
      },
    ],
  ],
  themes: ["@docusaurus/theme-mermaid"],

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: "en",
    locales: ["de", "en", "fr", "nl", "zh"],
    localeConfigs: {
      de: {
        label: "Deutsch",
      },
      en: {
        label: "English",
      },
      fr: {
        label: "Français"
      },
      nl: {
        label: "Nederlands"
      },
      zh: {
        label: "简体中文",
      },
    },
  },

  presets: [
    [
      "classic",
      {
        docs: {
          sidebarPath: "./sidebars.ts",
          remarkPlugins: [stripDocumentImages],
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl: "https://github.com/INDEVOLT/indevolt-doc/tree/main",
        },
        blog: false,
        theme: {
          customCss: "./src/css/custom.css",
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    // Replace with your project's social car
    // image: "img/docusaurus-social-card.jpg",
    docs: {
      sidebar: {
        hideable: true,
      },
    },
    navbar: {
      logo: {
        alt: "Developers",
        src: "img/indevolt-light.svg",
        srcDark: "img/indevolt-dark.svg",
        width: 120
      },
      items: [
        {
          label: "Micro Storage",
          to: "docs/hardware/doc-intro",
          position: "left",
        },
        {
          label: "INDEVOLT App",
          to: "docs/app/introduction",
          position: "left",
        },
        ...(isChineseLocale
          ? [{ ...developerCenterLink, position: "left" as const }]
          : []),
        {
          ...documentVersionLink,
          position: "left",
        },
        {
          type: "localeDropdown",
          position: "right",
        },
      ],
    },
    footer: {
      logo: {
        href: "/",
        src: "img/footer_light.svg",
        srcDark: "img/footer_dark.svg",
        alt: "INDEVOLT Documentation | INDEVOLT Docs",
        height: "36px",
      },
      links: [
        {
          title: "Docs",
          items: [
            {
              label: "Micro Storage",
              to: "docs/hardware/doc-intro"
            },
            {
              label: "INDEVOLT App",
              to: "docs/app/introduction"
            },
            ...(isChineseLocale ? [developerCenterLink] : []),
            documentVersionLink,
          ]
        },
        {
          title: "Product",
          items: [
            {
              label: "INDEVOLT",
              href: "https://www.indevolt.com/",
            },
          ],
        },
        {
          title: "Company",
          items: [
            {
              label: "About Us",
              href: "https://www.indevolt.com/pages/about-us/",
            },
          ],
        },
      ],
      copyright:
        "Copyright © 2026 Power Genius. All rights reserved.",
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: {
        plain: prismThemes.vsDark.plain,
        styles: [
          ...prismThemes.vsDark.styles,
          {
            types: ["function", "keyword"],
            style: {
              color: "#f25c7c",
            },
          },
        ],
      },
    },
    additionalLanguages: [
      "dart",
      "ruby",
      "groovy",
      "kotlin",
      "java",
      "swift",
      "objectivec",
      "json",
      "bash",
    ],
  } satisfies Preset.ThemeConfig,
};

export default config;
