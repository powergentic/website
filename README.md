# my-jekyll-site/my-jekyll-site/README.md

# My Jekyll Site

This is a simple Jekyll site structure designed for easy customization and deployment. Below are the details regarding the setup and usage of this project.

## Project Structure

- `_config.yml`: Configuration file for the Jekyll site containing site settings.
- `_includes/`: Contains reusable HTML snippets.
  - `head.html`: Head section of the HTML with meta tags and stylesheets.
  - `header.html`: Navigation bar and header elements.
  - `footer.html`: Footer section of the HTML.
- `_layouts/`: Contains layout templates for the site.
  - `default.html`: Main layout defining the structure of the pages.
- `_posts/`: Directory for Jekyll posts (Markdown files for blog posts).
- `assets/`: Contains static assets.
  - `css/styles.css`: Custom styles for the site.
  - `js/main.js`: Custom JavaScript for interactivity.
- `index.html`: Main page of the site using the default layout.
  
## Setup Instructions

1. **Install Jekyll**: Make sure you have Ruby and Bundler installed. Then, install Jekyll by running:
   ```
   gem install jekyll bundler
   ```

2. **Clone the Repository**: Clone this repository to your local machine:
   ```
   git clone <repository-url>
   cd my-jekyll-site
   ```

3. **Install Dependencies**: Run the following command to install the necessary dependencies:
   ```
   bundle install
   ```

4. **Run the Jekyll Server**: Start the Jekyll server to preview your site:
   ```
   bundle exec jekyll serve
   ```

5. **Access Your Site**: Open your browser and go to `http://localhost:4000` to view your site.

## Usage

- To create a new post, add a Markdown file in the `_posts/` directory following the naming convention `YEAR-MONTH-DAY-title.md`.
- Customize the site by editing the `_config.yml` file and modifying the HTML/CSS files in the `_includes/`, `_layouts/`, and `assets/` directories.

&copy; 2025 Powergentic.ai. All rights reserved.