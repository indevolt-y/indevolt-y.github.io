import React, { useEffect } from "react";
import OriginalFooter from "@theme-original/Footer";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";

const FOOTER_EXTERNAL_LINKS: Record<string, Record<string, string>> = {
  en: {
    product: "https://www.indevolt.com/",
    about_us: "https://www.indevolt.com/pages/about-us/",
  },
  fr: {
    product: "http://fr.indevolt.com/",
    about_us: "https://fr.indevolt.com/pages/about-us/",
  },
  zh: {
    product: "https://www.indevolt.com/",
    about_us: "https://www.indevolt.com/pages/about-us/",
  },
  de: {
    product: "http://de.indevolt.com/",
    about_us: "https://de.indevolt.com/pages/about-us",
  },
};

const FOOTER_LINK_MATCHERS: Record<string, string> = {
  "https://www.indevolt.com/": "product",
  "https://www.indevolt.com/pages/about-us/": "about_us",
};

export default function FooterWrapper(props) {
  const { i18n } = useDocusaurusContext();

  const locale = i18n.currentLocale.split("-")[0];

  const localizedLinks =
    FOOTER_EXTERNAL_LINKS[locale] ??
    FOOTER_EXTERNAL_LINKS[i18n.defaultLocale];

  useEffect(() => {
    const footer = document.querySelector("footer");
    if (!footer) return;

    const anchors = footer.querySelectorAll<HTMLAnchorElement>("a[href]");

    anchors.forEach((a) => {
      const originalHref = a.getAttribute("href");
      if (!originalHref) return;

      const key = FOOTER_LINK_MATCHERS[originalHref];
      if (!key) return;

      const localizedHref = localizedLinks[key];
      if (!localizedHref) return;

      a.href = localizedHref;
    });
  }, [locale]);

  return <OriginalFooter {...props} />;
}