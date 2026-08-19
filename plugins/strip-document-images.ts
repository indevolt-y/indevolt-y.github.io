type MarkdownNode = {
  type?: string;
  name?: string | null;
  value?: string;
  children?: MarkdownNode[];
};

const imageNodeTypes = new Set(["image", "imageReference"]);
const jsxNodeTypes = new Set(["mdxJsxFlowElement", "mdxJsxTextElement"]);

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

    if (isMarkdownImage || isJsxImage || isHtmlImage) {
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
