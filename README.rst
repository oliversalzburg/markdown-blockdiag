Markdown blockdiag code
=======================

.. image:: https://travis-ci.org/gisce/markdown-blockdiag.svg?branch=master
    :target: https://travis-ci.org/gisce/markdown-blockdiag


This is the `blockdiag <http://blockdiag.com/en/blockdiag/index.html>`_
extension for `Python Markdown <http://pythonhosted.org/Markdown/>`_

Install
-------

.. code-block::

  $ pip install markdown-blockdiag-code

Use
---

In your markdown text you can define the block

.. code-block::
  ```blockdiag
  blockdiag {
      A -> B -> C -> D;
      A -> E -> F -> G;
  }
  ```


Testing
-------


.. code-block::

  $ pip install coverage
  $ python setup.py test


MkDocs Integration
------------------

In your mkdocs.yml add this to markdown_extensions.

.. code-block::

  markdown_extensions:
    - pymdownx.superfences:
        custom_fences:
          - name: blockdiag
            class: blockdiag
            format: !!python/name:markdown_blockdiag_code.blockdiag.fence_img_format
          - name: seqdiag
            class: seqdiag
            format: !!python/name:markdown_blockdiag_code.blockdiag.fence_img_format
