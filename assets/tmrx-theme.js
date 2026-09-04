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

  document.querySelectorAll('[data-mobile-menu-accordion]').forEach((button) => {
    button.addEventListener('click', () => {
      const panel = button.nextElementSibling;
      const willOpen = button.getAttribute('aria-expanded') !== 'true';
      button.setAttribute('aria-expanded', String(willOpen));
      if (panel) panel.hidden = !willOpen;
    });
  });

  document.addEventListener('keydown', (event) => {
    if (event.key !== 'Escape') return;
    menuToggle?.setAttribute('aria-expanded', 'false');
    setOpenState(cartDrawer, false, 'is-open');
    setOpenState(mobileMenu, false, 'is-open');
  });

  const collectionCopy = {
    all: {
      title: 'Shop All Supplements',
      description: 'Explore TRUE MATRx full range of clean, practitioner-grade supplements.'
    },
    bestsellers: {
      title: 'Bestsellers',
      description: 'Shop the clean supplements customers reach for first.'
    },
    protein: {
      title: 'Protein Powder Supplements',
      description: 'Fuel your body with TRUE MATRx clean protein formulas made with purposeful ingredients and no artificial additives.'
    },
    recovery: {
      title: 'Build Muscle & Recover',
      description: 'Support strength, recovery, and lean muscle with clean formulas built for consistent training.'
    },
    'pre-workout': {
      title: 'Pre-Workout Supplements',
      description: 'Shop clean pre-workout and performance support designed for energy, focus, and endurance.'
    },
    wellness: {
      title: 'Health & Wellness Supplements',
      description: 'Build a daily foundation with clean wellness formulas for whole-body support.'
    },
    'weight-loss': {
      title: 'Weight Loss Supplements',
      description: 'Support body recomposition with clean nutrition and metabolism-focused formulas.'
    }
  };

  const collectionTitle = document.querySelector('[data-collection-title]');
  const collectionDescription = document.querySelector('[data-collection-description]');
  const collectionPills = document.querySelectorAll('[data-collection-pill]');
  const collectionProducts = document.querySelectorAll('[data-collection-product]');
  const collectionEmpty = document.querySelector('[data-collection-empty]');

  if (collectionPills.length && collectionProducts.length) {
    const params = new URLSearchParams(window.location.search);
    const requestedCategory = params.get('tmrx_category') || 'all';
    const activeCategory = collectionCopy[requestedCategory] ? requestedCategory : 'all';
    const activeCopy = collectionCopy[activeCategory];
    let visibleCount = 0;

    collectionPills.forEach((pill) => {
      pill.classList.toggle('is-active', pill.dataset.collectionPill === activeCategory);
    });

    if (collectionTitle) collectionTitle.textContent = activeCopy.title;
    if (collectionDescription) collectionDescription.textContent = activeCopy.description;

    collectionProducts.forEach((product) => {
      const categories = product.dataset.collectionProduct.split(/\s+/);
      const isVisible = activeCategory === 'all' || categories.includes(activeCategory);
      product.hidden = !isVisible;
      if (isVisible) visibleCount += 1;
    });

    if (collectionEmpty) collectionEmpty.hidden = visibleCount > 0;
  }

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
