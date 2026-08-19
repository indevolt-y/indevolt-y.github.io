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

const legacyDeveloperPaths: Record<string, string> = {
  "/docs/developer": "/docs/hardware/open-data/introduction",
  "/docs/developer/http": "/docs/hardware/open-data/http",
  "/docs/developer/http-api": "/docs/hardware/open-data/http-api",
  "/docs/developer/modbus": "/docs/hardware/open-data/modbus",
  "/docs/developer/modbus-register-table":
    "/docs/hardware/open-data/modbus-register-table",
  "/docs/developer/mqtt": "/docs/hardware/open-data/mqtt",
  "/docs/developer/mqtt-topic": "/docs/hardware/open-data/mqtt-topic",
  "/docs/developer/mqtt-data-points":
    "/docs/hardware/open-data/mqtt-data-points",
  "/docs/developer/home-assistant":
    "/docs/hardware/open-data/home-assistant",
};

function getDeveloperPath(pathname: string): string | undefined {
  return Object.keys(legacyDeveloperPaths).find(
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

  if (currentLocale !== "zh" || !developerPath) {
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
        : `${localePrefix}${legacyDeveloperPaths[developerPath]}`;

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
