# Byte Blog

## Overview
Byte Blog is a static HTML/CSS tech blog website focused on computer hardware and software development topics. The blog provides educational content about computer components and their relationship to software development.

## Project Structure
- `index.html` - Homepage with welcome message and navigation
- `blogs/` - Blog posts directory
  - `blogs.html` - Blog listing page
  - `whyLearningHardware.html` - Blog post about hardware importance
- `tips/` - Tips section directory  
  - `tips.html` - Tips page (placeholder content)
- `about.html` - About page with blog information
- `style.css` - Shared CSS styling for all pages

## Technical Setup
- **Type**: Static HTML/CSS website
- **Server**: Python built-in HTTP server
- **Port**: 5000 (bound to 0.0.0.0 for Replit compatibility)
- **Deployment**: Configured for autoscale deployment target

## Current Features
- Clean, responsive design with header navigation
- Blog post system with individual articles
- Consistent styling across all pages
- Working navigation between all sections

## Recent Changes (Sept 27, 2025)
- Imported from GitHub repository
- Set up Python HTTP server workflow on port 5000
- Configured deployment settings for production
- Verified all pages load correctly in Replit environment

## Deployment Configuration
- Target: Autoscale (suitable for static websites)
- Run command: `python -m http.server 5000 --bind 0.0.0.0`
- No build step required (static files)