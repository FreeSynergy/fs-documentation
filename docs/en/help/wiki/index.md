# Wiki help

Wiki is where texts live. Today its window is a reader: a tree of pages on the left and the page you picked on the right. You can follow links, search, edit a page and save it, and write a page out as a Markdown file.

## The views

- [Page tree](page-tree.md): the pages, as folders and pages.
- [Search results](search-results.md): what you get when you type into the search field.
- [Page](page.md): reading a page, following links, going back.
- [Edit](edit.md): changing a page, saving, and getting back a draft you did not save.
- [Export](export.md): writing a page to a Markdown file.
- [Import problems](import-problems.md): files that did not come in cleanly.

## How to start

The wiki lives in a server, so start that first: `fs-wiki-server`, with `--socket PATH` and `--data DIR` if you want your own. Then start the window with `fs-wiki-app --socket PATH`, and `--docs FOLDER` for the Markdown folder to import. The first start imports the folder, about 30 seconds for 1400 pages. A short summary line appears in the terminal before the window opens. If the server does not run, the app stops and tells you the command to start it.
