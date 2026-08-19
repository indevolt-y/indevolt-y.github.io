import React, { type ReactNode } from "react";
import { translate } from "@docusaurus/Translate";
import { useLocation } from "@docusaurus/router";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import OriginalLocaleDropdownNavbarItem from "@theme-original/NavbarItem/LocaleDropdownNavbarItem";
import DropdownNavbarItem from "@theme/NavbarItem/DropdownNavbarItem";
import IconLanguage from "@theme/Icon/Language";
import type { LinkLikeNavbarItemProps } from "@theme/NavbarItem";
import type { Props } from "@theme/NavbarItem/LocaleDropdownNavbarItem";

import styles from "./styles.module.css";

const developerPaths = [
  "/docs/developer",
  "/docs/developer/http",
  "/docs/developer/http-api",
  "/docs/developer/modbus",
  "/docs/developer/modbus-register-table",
  "/docs/developer/mqtt",
  "/docs/developer/mqtt-topic",
  "/docs/developer/mqtt-data-points",
  "/docs/developer/home-assistant",
  "/docs/developer/guides/build-indevolt-app-with-ai",
  "/docs/developer/guides/ai-assisted-development/expert-instructions",
  "/docs/developer/guides/opendata-local-device-panel",
];

const bilingualDeveloperPaths = new Set(developerPaths);

function getDeveloperPath(pathname: string): string | undefined {
  return developerPaths.find(
    (path) => pathname === path || pathname.endsWith(path),
  );
}

export default function LocaleDropdownNavbarItem({
  mobile,
  dropdownItemsBefore,
  dropdownItemsAfter,
  queryString = "",
  ...props
}: Props): ReactNode {
  const {
    i18n: { currentLocale, defaultLocale, locales, localeConfigs },
  } = useDocusaurusContext();
  const { pathname, search, hash } = useLocation();
  const developerPath = getDeveloperPath(pathname);
  const isBilingualDeveloperPath =
    developerPath !== undefined && bilingualDeveloperPaths.has(developerPath);
  const usesDeveloperLocaleRouting =
    developerPath !== undefined &&
    (currentLocale === "zh" ||
      (currentLocale === "en" && isBilingualDeveloperPath));

  if (!usesDeveloperLocaleRouting) {
    return (
      <OriginalLocaleDropdownNavbarItem
        {...props}
        mobile={mobile}
        dropdownItemsBefore={dropdownItemsBefore}
        dropdownItemsAfter={dropdownItemsAfter}
        queryString={queryString}
      />
    );
  }

  const localeItems = locales.map((locale): LinkLikeNavbarItemProps => {
    const localePrefix = locale === defaultLocale ? "" : `/${locale}`;
    const targetPath =
      locale === currentLocale
        ? pathname
        : isBilingualDeveloperPath && (locale === "zh" || locale === "en")
          ? `${localePrefix}${developerPath}`
          : `${localePrefix}/`;

    return {
      label: localeConfigs[locale]!.label,
      lang: localeConfigs[locale]!.htmlLang,
      to: `pathname://${targetPath}${search}${hash}${queryString}`,
      target: "_self",
      autoAddBaseUrl: false,
      className:
        locale === currentLocale
          ? mobile
            ? "menu__link--active"
            : "dropdown__link--active"
          : "",
    };
  });

  const items = [
    ...dropdownItemsBefore,
    ...localeItems,
    ...dropdownItemsAfter,
  ];
  const dropdownLabel = mobile
    ? translate({
        message: "Languages",
        id: "theme.navbar.mobileLanguageDropdown.label",
        description: "The label for the mobile language switcher dropdown",
      })
    : localeConfigs[currentLocale]!.label;

  return (
    <DropdownNavbarItem
      {...props}
      mobile={mobile}
      label={
        <>
          <IconLanguage className={styles.iconLanguage} />
          {dropdownLabel}
        </>
      }
      items={items}
    />
  );
}
