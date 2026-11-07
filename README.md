# Via Pulchritudinis

A Catholic Journal of Style and Beauty. The Beauty of Cathedrals in Everyday Fashion. Outfits drawn from the stone, glass, and gold of 50 cathedrals, basilicas, and shrines, each with its own interior and exterior photos, a measured palette, and a unique outfit, with what the popes and the Church have said about beauty, dress, and the body.

Static site for GitHub Pages. `index.html` holds the layout, `data.js` holds the churches, palettes, looks, and photo credits, and `img/` holds the photos.

Photos come from Wikimedia Commons and Flickr through Openverse, under CC BY, CC BY-SA, CC0, or public domain terms. Each photo is credited on its page and in the footer.

## Pages

The site has eight pages: Home, The Lookbook, How It Works, The Liturgical Year, Beauty & Faith, St. Pier Giorgio, The Directory, and Sources & Credits. They share `assets/site.css` and `assets/site.js`, and `data.js` holds the churches, palettes, looks, and photo credits.

The pages are generated from one layout. To change the header, footer, or a page, edit `_build/build.py` (and the text blocks in `_build/pages/`), then run `python3 _build/build.py` from the repository root.
