document.addEventListener('DOMContentLoaded', function() {
  if (typeof mermaid !== 'undefined') {
    // Determine theme based on Material for MkDocs theme
    const isDarkMode = document.querySelector('[data-md-color-scheme="slate"]') !== null ||
                       (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches);
    
    mermaid.initialize({ 
      startOnLoad: true,
      theme: isDarkMode ? 'dark' : 'default',
      securityLevel: 'loose'
    });
    mermaid.contentLoaded();
  }
});
