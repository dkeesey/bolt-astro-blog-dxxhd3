# Dean Keesey's Personal Site

A personal portfolio and blog built with Astro, React, and TailwindCSS.

## Development Workflow

1. Open project in bolt.new:
   - Prepend `https://bolt.new/` to your GitHub repo URL
   - Example: `https://bolt.new/yourusername/your-repo`

2. Make changes in bolt.new editor

3. Export changes:
   - Download the zip file from bolt.new
   - This contains all your modifications

4. Sync changes locally:
   ```bash
   # If using the alias
   bolt-sync path/to/downloaded/bolt-export.zip

   # Or run directly
   python3 bolt_sync.py path/to/downloaded/bolt-export.zip
   ```

5. Review and commit:
   - Check changes: `git diff`
   - Stage changes: `git add .`
   - Commit and push

Note: The sync script will:
- Create a backup branch for safety
- Extract the zip file
- Copy changes to your project
- Show git status
- Guide you through next steps

## Project Structure

Inside of your Astro project, you'll see the following folders and files:

```text
├── public/
├── src/
│   ├── components/
│   ├── content/
│   ├── layouts/
│   └── pages/
├── astro.config.mjs
├── README.md
├── package.json
└── tsconfig.json
```

Astro looks for `.astro` or `.md` files in the `src/pages/` directory. Each page is exposed as a route based on its file name.

There's nothing special about `src/components/`, but that's where we like to put any Astro/React/Vue/Svelte/Preact components.

The `src/content/` directory contains "collections" of related Markdown and MDX documents. Use `getCollection()` to retrieve posts from `src/content/blog/`, and type-check your frontmatter using an optional schema. See [Astro's Content Collections docs](https://docs.astro.build/en/guides/content-collections/) to learn more.

Any static assets, like images, can be placed in the `public/` directory.

## 🧞 Commands

All commands are run from the root of the project, from a terminal:

| Command                   | Action                                           |
| :------------------------ | :----------------------------------------------- |
| `npm install`             | Installs dependencies                            |
| `npm run dev`             | Starts local dev server at `localhost:4321`      |
| `npm run build`           | Build your production site to `./dist/`          |
| `npm run preview`         | Preview your build locally, before deploying     |
| `npm run astro ...`       | Run CLI commands like `astro add`, `astro check` |
| `npm run astro -- --help` | Get help using the Astro CLI                     |

## Credit

This theme is based off of the lovely [Bear Blog](https://github.com/HermanMartinus/bearblog/).