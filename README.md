# blockdiag for SuperFences

This provides [blockdiag](http://blockdiag.com/en/blockdiag/index.html) rendering for [Python Markdown](http://pythonhosted.org/Markdown/) through the [SuperFences extension](https://facelessuser.github.io/pymdown-extensions/extensions/superfences/).

It is based on <https://github.com/gisce/markdown-blockdiag>.

## Install

```shell
pip install blockdiag-fences
```

## Use

Wrap your diagram in a code block, tagged with the name of the tool to convert it:


	```blockdiag
	blockdiag {
		A -> B -> C -> D;
		A -> E -> F -> G;
	}
	```

## MkDocs Integration

In your `mkdocs.yml` add this to `markdown_extensions`.

```yaml
markdown_extensions:
  - pymdownx.superfences:
    custom_fences:
      - name: blockdiag
        class: blockdiag
        format: !!python/name:blockdiag_fences.blockdiag.fence_img_format
      - name: seqdiag
        class: seqdiag
        format: !!python/name:blockdiag_fences.blockdiag.fence_img_format
```
