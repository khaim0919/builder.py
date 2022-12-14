# builder.py
An extensible static site generation package for the real world. 

## Quick Start Guide

1. **Add a folder that starts with an `_`** (just `_` works too!) contents will be put into that folder but with the `_` stripped, so `_/blog` will be put into `/blog/`. `_` goes to the root directory and they all preserve file structure! (This works well if you make the build to folder for these the subdomain, and thats how it will likely be interpreted. 
2. **Add `builder.py` and `builder.config` to your root directory** (you can just copy the defult, it will work in most cases) 
3. **Run builder.py** (`python builder.py` using a terminal) 

**Thats it!** You can now do with them what you want, commit them to your web server, use them for whatever you want! Builder.py supports a wide range of markdown, and if its missing something you can just modify the code or add an extension for it!

## Suported Markdown 

- `*italics*`  
- `**bold**`  
- `__underlined__`  
- `[links](url "label")`'  
- `# Headers` (Number of hashtags specifies trhe level, `# ` is h1, `## ` is h2, etc. The space IS NEEDED, otherwise its a tag)   
- `--` emdash (`—`)  
- `> ` blockquotes

### Work in Progress Markdown
- `[id links][id]` (make sire you add `[id]: url "label"` somewhere in your document!)  
- `[[Pipeable Wikilinks|wikilinks]]` -- Takes the content inside of it and links to that! You can use a pipe (`|` character to specify otherwise (`this content will be displayed|and-it-will-link-here`). You can use absolute (`[[/path/to/file]]`) relative from base (`[[thing]]`) For example if you are on example.com/blog/post-1 and there is a wikilink to `[[post-2]]` you will go to example.com/blog/post-2, but if it was `[[/post-2]]` you would go to example.com/post-2!
- `[abbrs]("Abbriviations")` -- WARNING: The label is NOT VISBLE to screen readers  
- `^superscript`  
- `^^subscript`  
- `#tags` or indexing  
- `[HTML Obfuscated emails](mailto:email@example.co,)`   
- `![image label](url)`
- `![id images][id]`

```
> [!callouts] 
> are not currently
> supported :(
```

```
- nested
  - unordered
  - lists 
- are a 
  - work 
    - in 
      - progress
```

```
1. nested
  1. ordered
  2. lists 
2. are 
  1. a
  2. work 
  3. in 
    1. progress
```

### With Extensions... 
- `:emojis: and :unicode: character auto replacement!`  
