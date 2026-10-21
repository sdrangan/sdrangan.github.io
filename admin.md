# Site admin notes

Maintenance notes for the group website. This file is not published on the site.

## Previewing the site locally

### One-time setup

1. **Install Ruby with the DevKit** (PowerShell):

   ```
   winget install RubyInstallerTeam.RubyWithDevKit.3.3
   ```

   Use Ruby 3.3, not 3.4: GitHub Pages runs Jekyll 3.x, which has problems on
   Ruby 3.4. If the installer asks to run `ridk install`, accept the default
   (MSYS2 toolchain).

2. **Restart your terminal** (or all of VS Code, if using its terminal) so the
   `ruby` and `gem` commands are on the PATH.

3. **Install Bundler:**

   ```
   gem install bundler
   ```

4. **Install the site's gems** (from the repo root). This installs the same
   Jekyll version and plugins that GitHub Pages uses. Re-run it only if the
   `Gemfile` changes.

   ```
   bundle install
   ```

### Each time

5. **Start the preview server** (from the repo root):

   ```
   bundle exec jekyll serve --livereload
   ```

   Open <http://localhost:4000>. The page refreshes automatically when you save
   a file. Changes to `_config.yml` need a server restart (Ctrl+C, then run the
   command again).

   If a page suddenly shows up unstyled (plain blue links, huge images), the
   browser reloaded while Jekyll was mid-rebuild. Hard refresh with
   **Ctrl+Shift+R**.
