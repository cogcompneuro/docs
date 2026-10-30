DOIs have been assigned to all accepted Proceedings papers, and are available under your
paper's metadata as `DOI`.

Copy this DOI, which is of the form `10.32470/00aa11bb`, then switch your template to the
proceedings (camera-ready) option so the DOI is rendered in the tagline on the first
page.

In the LaTeX template, set these in the document preamble:

```latex
\documentclass[proceedings]{ccn}
\ccndoi{10.32470/00aa11bb}  % required; assigned by CCN
```

In the Typst template, set these in the `ccn` show rule:

```typst
#show: ccn.with(
  mode: "proceedings",
  doi: "10.32470/00aa11bb",  // required; assigned by CCN
  // ...
)
```
