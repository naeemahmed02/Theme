document.addEventListener('DOMContentLoaded', function() {
    // Add smooth scrolling for TOC links
    document.querySelectorAll('.toc-content a').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});
