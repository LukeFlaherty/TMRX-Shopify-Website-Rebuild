(() => {
  const body = document.body;
  const cartDrawer = document.querySelector('[data-cart-drawer]');
  const mobileMenu = document.querySelector('[data-mobile-menu]');
  const menuToggle = document.querySelector('[data-menu-toggle]');

  const setOpenState = (element, isOpen, className) => {
    if (!element) return;
    element.hidden = !isOpen;
    element.classList.toggle(className, isOpen);
    body.classList.toggle('tmrx-lock-scroll', isOpen);
  };

  document.querySelectorAll('[data-cart-open]').forEach((button) => {
    button.addEventListener('click', () => setOpenState(cartDrawer, true, 'is-open'));
  });

  document.querySelectorAll('[data-cart-close]').forEach((button) => {
    button.addEventListener('click', () => setOpenState(cartDrawer, false, 'is-open'));
  });

  if (menuToggle) {
    menuToggle.addEventListener('click', () => {
      const willOpen = !mobileMenu?.classList.contains('is-open');
      menuToggle.setAttribute('aria-expanded', String(willOpen));
      setOpenState(mobileMenu, willOpen, 'is-open');
    });
  }

  document.querySelectorAll('[data-menu-close]').forEach((button) => {
    button.addEventListener('click', () => {
      menuToggle?.setAttribute('aria-expanded', 'false');
      setOpenState(mobileMenu, false, 'is-open');
    });
  });

  document.addEventListener('keydown', (event) => {
    if (event.key !== 'Escape') return;
    menuToggle?.setAttribute('aria-expanded', 'false');
    setOpenState(cartDrawer, false, 'is-open');
    setOpenState(mobileMenu, false, 'is-open');
  });

  document.querySelectorAll('[data-product-carousel]').forEach((carousel) => {
    const rail = carousel.querySelector('[data-product-rail]');
    const count = carousel.querySelector('[data-product-count]');
    const progressItems = carousel.querySelectorAll('.tmrx-carousel-progress span');
    const cards = rail ? Array.from(rail.children) : [];

    if (!rail || !count || cards.length === 0) return;

    const updateCarouselState = () => {
      const cardWidth = cards[0].getBoundingClientRect().width || 1;
      const gap = parseFloat(getComputedStyle(rail).columnGap || getComputedStyle(rail).gap || 0);
      const currentIndex = Math.min(cards.length - 1, Math.max(0, Math.round(rail.scrollLeft / (cardWidth + gap))));
      const current = String(currentIndex + 1).padStart(2, '0');
      const total = String(cards.length).padStart(2, '0');

      count.textContent = `${current}/${total}`;
      progressItems.forEach((item, index) => {
        item.classList.toggle('is-active', index === currentIndex);
      });
    };

    rail.addEventListener('scroll', updateCarouselState, { passive: true });
    window.addEventListener('resize', updateCarouselState);
    updateCarouselState();
  });
})();
