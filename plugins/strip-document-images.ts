type MarkdownNode = {
  attributes?: Array<{
    name?: string;
    value?: string | {value?: string};
  }>;
  type?: string;
  name?: string | null;
  url?: string;
  value?: string;
  children?: MarkdownNode[];
};

const imageNodeTypes = new Set(["image", "imageReference"]);
const jsxNodeTypes = new Set(["mdxJsxFlowElement", "mdxJsxTextElement"]);
const allowedImagePaths = ["/img/developer/ai/"];

function isAllowedImage(node: MarkdownNode): boolean {
  const sourceAttribute = node.attributes?.find(
    (attribute) => attribute.name?.toLowerCase() === "src",
  );
  const attributeValue = sourceAttribute?.value;
  const htmlSource = node.value?.match(/\bsrc=["']([^"']+)["']/i)?.[1];
  const source =
    node.url ??
    (typeof attributeValue === "string"
      ? attributeValue
      : attributeValue?.value) ??
    htmlSource;

  return allowedImagePaths.some((path) => source?.includes(path));
}

function removeImages(node: MarkdownNode): void {
  if (!node.children) {
    return;
  }

  node.children = node.children.filter((child) => {
    const isMarkdownImage = imageNodeTypes.has(child.type ?? "");
    const isJsxImage =
      jsxNodeTypes.has(child.type ?? "") && child.name?.toLowerCase() === "img";
    const isHtmlImage =
      child.type === "html" && /<img\b/i.test(child.value ?? "");

    if (
      (isMarkdownImage || isJsxImage || isHtmlImage) &&
      !isAllowedImage(child)
    ) {
      return false;
    }

    removeImages(child);

    return child.type !== "paragraph" || (child.children?.length ?? 0) > 0;
  });
}

export default function stripDocumentImages() {
  return (tree: MarkdownNode): void => {
    removeImages(tree);
  };
}
