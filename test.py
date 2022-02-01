import markdown
html = markdown.markdown("""
blockdiag {
  A -> B -> C;
}

```
blockdiag {
  A -> B;
}
```

```blockdiag
blockdiag {
  A -> B;
}
```
""", extensions=['fenced_code', 'markdown_blockdiag_code'])
print(html)
