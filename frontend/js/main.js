document.addEventListener('DOMContentLoaded', () => {
    
    /* --- Sticky Header Logic --- */
    const header = document.querySelector('.main-header');
    
    // Check scroll position on load and on scroll
    const checkScroll = () => {
        if (window.scrollY > 50) {
            header.style.padding = '0.5rem 0';
            header.style.boxShadow = 'var(--shadow-diffused)';
        } else {
            header.style.padding = '1rem 0';
            header.style.boxShadow = 'none';
        }
    };
    
    window.addEventListener('scroll', checkScroll);
    checkScroll(); // Initialize

    /* --- Mobile Menu Toggle --- */
    const mobileBtn = document.getElementById('mobileMenuBtn');
    const mainNav = document.getElementById('mainNav');
    
    if (mobileBtn && mainNav) {
        mobileBtn.addEventListener('click', () => {
            mainNav.classList.toggle('active');
            
            // Toggle icon from hamburger to close
            if (mainNav.classList.contains('active')) {
                mobileBtn.innerHTML = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>';
            } else {
                mobileBtn.innerHTML = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>';
            }
        });
    }
});
