import type { ReactNode } from "react";
import Head from "@docusaurus/Head";
import { translate } from "@docusaurus/Translate";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import Layout from "@theme/Layout";

import Hero from "../components/Hero";

export default function Home(): ReactNode {
  const { siteConfig } = useDocusaurusContext();

  return (
    <Layout
      title={siteConfig.title}
      description={translate({
        message: "Welcome to our website!",
        id: "home.description",
      })}
    >
      <Head>
        <title>{siteConfig.title}</title>
      </Head>
      <main>
        <Hero />
      </main>
    </Layout>
  );
}
