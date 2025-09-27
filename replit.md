# Byte Blog

## Overview

Byte Blog is a static educational website focused on computer technology tips and knowledge sharing. Created by a learning software and hardware developer, the site serves as a platform to share tech insights, tutorials, and resources. The website features a simple blog structure with sections for blogs, tips, and general information about technology topics, particularly emphasizing the importance of understanding hardware for software development.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Static HTML Structure**: Uses traditional HTML5 with semantic markup for content organization
- **CSS Styling**: Single shared stylesheet (`style.css`) provides consistent styling across all pages
- **Navigation System**: JavaScript-based navigation using `onclick` events and `window.location.href` for page routing
- **Responsive Design**: Meta viewport tags ensure mobile compatibility

### Content Organization
- **Modular Page Structure**: Separate directories for different content types (`blogs/`, `tips/`)
- **Shared Components**: Consistent header navigation across all pages with relative path handling
- **Content Presentation**: Dedicated CSS classes for different content types (blog content, centered text, small text)

### Design Patterns
- **Template-Based Layout**: All pages follow a consistent header-content structure
- **Color-Coded Navigation**: Green header buttons for easy identification
- **Content Categorization**: Clear separation between blogs, tips, and informational pages

## External Dependencies

### Hosting Platform
- **GitHub Pages**: Currently hosted at `https://pro-the-pro.github.io/Byte-Blog/` for static site deployment

### Technology Stack
- **Pure HTML/CSS/JavaScript**: No external frameworks or libraries
- **No Database**: Content is stored as static HTML files
- **No Backend Services**: Entirely client-side rendered content

### Browser Dependencies
- **Standard Web APIs**: Relies on basic browser navigation and DOM manipulation
- **CSS3 Features**: Uses modern CSS properties like `border-radius` and flexible layouts